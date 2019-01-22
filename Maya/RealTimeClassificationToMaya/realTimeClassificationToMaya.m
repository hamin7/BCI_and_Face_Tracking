function realTimeClassificationToMaya();
persistent udpObj

load('classification_results.mat');

ButtonHandle = uicontrol('Style', 'PushButton', ...
                         'String', 'Stop loop', ...
                         'Callback', 'delete(gcbf)');
                     
if isempty(udpObj)% window backup Data √ ±‚»≠
%         myStop; %192.168.0.4
    try
    echotcpip('on',7777)
    catch ex
        if strcmp(ex.identifier,'instrument:echotcpip:running')
            echotcpip('off')
        end
    end
    udpObj = tcpip('166.104.29.148', 7777);
    if strcmp(udpObj.Status,'closed')
        fopen(udpObj);
    end
end


c = 0;
while (1)
c = c + 1;
    if ~ishandle(ButtonHandle)
        disp('Stopped by user');
        break;
    end
    
    emotion2Avartar(udpObj, yPdCv(c,:),1)
    
    pause(0.05);
end
fclose(udpObj);
echotcpip('off')
clear udpObj;
end