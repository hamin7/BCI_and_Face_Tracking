import maya.cmds as cmds
import os
import random
import pymel.core as pm
import socket
import sys
import maya.mel as mm
import csv

recstart = 0
selectedBlend = ""
dataarray = []
gnumcurrenttime = 1
"""
menulabelarr = ['Brow Left UP','Brow Left Down','Brow Right UP','Brow Right Down','Brow Centering','Brow outer left down','Brow outer right down','Eye Close Left','Eye Close Right','Mouse Open',
                'Mouse Left Smile','Mouse Right Smile','Mouse Left Spread','Mouse Right Spread','Mouse Left Frawn','Mouse Right Frawn','Mouse Left Centering','Mouse Right Centering','Cheek Left UP',
                'Cheek Right UP']
"""


# Our mel global proc.
melproc = """
global proc portData(string $arg){
    python(("portData(\\"" + $arg + "\\")"));
}
"""
mm.eval(melproc)

def edit_cell(row, column, value):
    return 1




def startrealtimeexp(*args):
    global recstart
    global recend
    numrow = cmds.scriptTable('scrtable', query=True, rows=True)
    if len(selectedBlend) > 0 and numrow > 1:
        if recstart == 0:
            recstart = 1
            cmds.button( 'realtimecomm' ,edit=True, label = 'Stop Real Time Expression' )
	    #Start Comm
            cmds.commandPort(name="127.0.0.1:7777", echoOutput=False, noreturn=False,prefix="portData", returnNumCommands=True)
            cmds.commandPort(name=":7777", echoOutput=False, noreturn=False,prefix="portData", returnNumCommands=True)
        else:
            recstart = 0
            cmds.button( 'realtimecomm' ,edit=True, label = 'Start Real Time Expression' )
	    #Stop Comm
            deactivateCommandPort('127.0.0.1', '7777')




def delete_sel_row(*args):
    if recstart == 0:
        try:
            selected_row = cmds.scriptTable('scrtable', query=True, selectedRows=True)[0]
            if selected_row == None:
                print('Select Row to Delete')
            else:
                cmds.scriptTable('scrtable', edit=True,deleteRow=selected_row)
        except:
            print('Select Row to Delete')




def savepresetfile(*args):
    blendshapetxt = cmds.textField('selectedBlendShapeText', q=True, tx=True )
    filename = blendshapetxt + "_mayapipeline_setting.txt"
    o_file = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\"+ filename
	
    all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
	
    if all_rows < 2:
        return 0
	
    if not (cmds.file(o_file,query=True, exists=True)):
        tmp_csv_file = open(o_file, 'w' ,os.O_CREAT)
    else:
        tmp_csv_file = open(o_file, 'w')
    writer = csv.writer(tmp_csv_file, lineterminator='\n')

    all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
    for i in range(all_rows):			
        all_colums = cmds.scriptTable('scrtable', query=True, columns=True)
        data_list = []
        for j in range( all_colums - 1):
            if i == 0:
                blendshapetxt = cmds.textField('selectedBlendShapeText', q=True, tx=True )
                headbonenametxt = cmds.textField('HeadbonenameF', q=True, tx=True )
                headxtxt = cmds.textField('HeadbonenameXF', q=True, tx=True )
                headytxt = cmds.textField('HeadbonenameYF', q=True, tx=True )
                headztxt = cmds.textField('HeadbonenameZF', q=True, tx=True )
                porttxt = cmds.textField('Portnum', q=True, tx=True )
                data_list = [blendshapetxt, headbonenametxt, headxtxt, headytxt, headztxt, porttxt]

            else:
                cell_list = cmds.scriptTable('scrtable', cellIndex=(i,j + 1), query=True, cellValue=True)
                if j == 0:
                    if type(cell_list) == list:
                        cell_text = "".join(cell_list)
                        print(cell_text)
                    elif cell_list == None:
                        cell_text = u''
                    else:
                        cell_text = cell_list
                    data_list.append(cell_text)
                elif j == 1:
                    if type(cell_list) == list:
                        cell_text = "".join(cell_list)
                        print(cell_text)
                    elif cell_list == None:
                        cell_text = u''
                    else:
                        cell_text = cell_list
                    data_list.append(cell_text)
                else:
                    if type(cell_list) == list:
                        cell_text = "".join(cell_list)
                    elif cell_list == None:
                        cell_text = u''
                    else:
                        cell_text = cell_list
                    data_list.append(cell_text)
        writer.writerow(data_list)
    tmp_csv_file.close()
    cmds.warning( "Saved file (" +o_file+ ")" )




def loadpresetfile(*args):
    if recstart != 0:
        return 0
	
    presetfile = pm.fileDialog2(fileMode=1)
	
    if presetfile:	
        cmds.scriptTable('scrtable', edit=True, selectedRows=[])
		
        o_file = open(str(presetfile[0]), 'r')
        reader = csv.reader(o_file)
		
        all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
        for i in range(all_rows):
            cmds.scriptTable('scrtable', edit=True,deleteRow= i)
	
        row_no = 0
        for row in reader:
            if row_no > 0:
                cmds.scriptTable('scrtable', edit=True,insertRow=row_no)
                cmds.scriptTable('scrtable', cellIndex=(row_no,1), edit=True, cellValue=row[0])
                cmds.scriptTable('scrtable', cellIndex=(row_no,2), edit=True, cellValue=row[1])
                cmds.scriptTable('scrtable', cellIndex=(row_no,3), edit=True, cellValue="0")
                cmds.scriptTable('scrtable', cellIndex=(row_no,4), edit=True, cellValue=row[3])
                cmds.scriptTable('scrtable', cellIndex=(row_no,5), edit=True, cellValue=row[4])
                cmds.scriptTable('scrtable', cellIndex=(row_no,6), edit=True, cellValue=row[5])
            else:
                cmds.textField('selectedBlendShapeText', edit=True, text=row[0] )
                cmds.textField('HeadbonenameF', edit=True, text=row[1] )
                cmds.textField('HeadbonenameXF', edit=True, text=row[2] )
                cmds.textField('HeadbonenameYF', edit=True, text=row[3] )
                cmds.textField('HeadbonenameZF', edit=True, text=row[4] )
                #cmds.textField('Portnum', edit=True, text=row[5] )
                loadTargetList()
            row_no = 1 + row_no
        o_file.close()




def expTrackerWindow():
    if cmds.window('expTrackerWindow', exists = True):
        cmds.deleteUI('expTrackerWindow')

    #window def
    cmds.window('expTrackerWindow',widthHeight=(900,400),title='expTracker-conelab',minimizeButton=False,maximizeButton=False,resizeToFitChildren = True, sizeable = True)
    #cmds.rowColumnLayout(numberOfColumns=3,columnWidth=[(1,300),(2,300),(3,300)],backgroundColor=[200,200,0])
    
#select an existing blendShape node
    cmds.rowColumnLayout(numberOfColumns=6,columnWidth=[(1,150),(2,25),(3,300),(4,25),(5,200),(6,200)],backgroundColor=[1,0.9843,0.7961])
    cmds.text( label='Blend Shape node name : ' ,align='right' )
    cmds.text( label='' )
    selectedBlendShapeTextField = cmds.textField( 'selectedBlendShapeText' ,backgroundColor=[1,1,1])
    cmds.text( label='' )
    cmds.button( label = 'Load Targets', command = 'loadTargetList()', width=20, align='left',backgroundColor=[0.3412,0.8196,0.7882])
    cmds.text( label='' )
    
    cmds.columnLayout('temp1', width=900)
    cmds.rowColumnLayout(numberOfColumns=6,columnWidth=[(1,300),(2,40),(3,300),(4,40),(5,200),(6,20)])
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )

	
    targetList = cmds.optionMenu( 'targetObjectMenu', label='Target: ',backgroundColor=[1,0.9098,0.4118])
    cmds.menuItem(label=' ' )
    cmds.text( label='' )
    paramList = cmds.optionMenu( 'paramObjectMenu', label='Link: ',backgroundColor=[1,0.9098,0.4118] )
    cmds.menuItem(label='Please select param' )
    cmds.menuItem(label='Brow Left UP')
    cmds.menuItem(label='Brow Left Down')
    cmds.menuItem(label='Brow Right UP')
    cmds.menuItem(label='Brow Right Down')
    cmds.menuItem(label='Brow Centering')
    cmds.menuItem(label='Brow outer left down')
    cmds.menuItem(label='Brow outer right down')
    cmds.menuItem(label='Eye Close Left')
    cmds.menuItem(label='Eye Close Right')
    cmds.menuItem(label='Mouse Open')
    cmds.menuItem(label='Mouse Left Smile')
    cmds.menuItem(label='Mouse Right Smile')
    cmds.menuItem(label='Mouse Left Spread')
    cmds.menuItem(label='Mouse Right Spread')
    cmds.menuItem(label='Mouse Left Frawn')
    cmds.menuItem(label='Mouse Right Frawn')
    cmds.menuItem(label='Mouse Left Centering')
    cmds.menuItem(label='Mouse Right Centering')
    cmds.menuItem(label='Cheek Left UP')
    cmds.menuItem(label='Cheek Right UP')
    cmds.text( label='' )
    cmds.button( label = 'Add link', command = 'addlink()' ,backgroundColor=[0.3412,0.8196,0.7882])
    cmds.text( label='' )
    
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    
    cmds.columnLayout('mytable', width=900,backgroundColor=[1,0.9098,0.4118])

    table =  cmds.scriptTable('scrtable',rows=0, columns=6,columnWidth=([1,300],[2,300],[3,145],[4,145],[5,1],[6,1]),
    	label=[(1,"Target"), (2,"Link"), (3,"Receive val"), (4,"Strength"), (5,"ID(Target)"), (6,"ID(Link)")], width=900,
    	cellChangedCmd=edit_cell)
	
    cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,100),(2, 300), (3, 500)])
	

    cmds.text( label='' )
    cmds.text( label='' )
    cmds.button( label = 'Delete select row',command=delete_sel_row,backgroundColor=[0.3412,0.8196,0.7882] )


    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )

    cmds.columnLayout('temp2', width=900)
    cmds.rowColumnLayout(numberOfColumns = 4, columnWidth = [(1,100),(2, 300), (3, 300),(4,200)],backgroundColor=[1,0.9098,0.4118])
    
    cmds.text( label='' )
    cmds.text( label='Head bone name' )
    Headbonename = cmds.textField('HeadbonenameF')
    cmds.text( label='' )


    cmds.text( label='' )
    cmds.text( label='Head bone rotation compensation X' )
    HeadbonenameX = cmds.textField('HeadbonenameXF',text='0')
    cmds.text( label='' )


    cmds.text( label='' )
    cmds.text( label='Head bone rotation compensation Y' )
    HeadbonenameY = cmds.textField('HeadbonenameYF',text='0')
    cmds.text( label='' )
	

    cmds.text( label='' )
    cmds.text( label='Head bone rotation compensation Z' )
    HeadbonenameZ = cmds.textField('HeadbonenameZF',text='0')
    cmds.text( label='' )

    cmds.columnLayout('temp3', width=900)
    cmds.rowColumnLayout(numberOfColumns=5,columnWidth=[(1,200),(2,50),(3,200),(4,150),(5,300)])
	
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
	
    cmds.button( label = 'Save preset', command = savepresetfile,backgroundColor=[0.3412,0.8196,0.7882] )
    cmds.text( label='' )
    cmds.button( label = 'Load preset', command = loadpresetfile,backgroundColor=[0.3412,0.8196,0.7882] )
    cmds.text( label='' )
    cmds.button( 'realtimecomm', label = 'Start Real Time Expression', command = startrealtimeexp ,backgroundColor=[0.9294,0.3294,0.5216])
	
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
	
    cmds.showWindow( 'expTrackerWindow' )



	
expTrackerWindow()

#function that loads target list to the UI

def loadTargetList():
    global selectedBlend
    selectedBlend = cmds.textField('selectedBlendShapeText', q=True, tx=True )
	
    existingItems = cmds.optionMenu( 'targetObjectMenu', q=True, itemListLong=True )
    if existingItems != None and existingItems != []:
        cmds.deleteUI(existingItems)
	
    cmds.menuItem(label='Please select blendShape', parent='targetObjectMenu')
	

    blendTargets = cmds.listAttr (selectedBlend + '.w', m = True)
    for target in blendTargets:
        cmds.menuItem(label='%s' %(target), parent='targetObjectMenu')


def addlink():
    if recstart == 0:
        selectedBlend = cmds.optionMenu('targetObjectMenu', query=True, value=True )
        selectedBlendI = cmds.optionMenu('targetObjectMenu', query=True, select=True )
        selectedLinkBlend = cmds.optionMenu('paramObjectMenu', query=True, value=True )
        selectedLinkBlendI = cmds.optionMenu('paramObjectMenu', query=True, select=True )
		
        if selectedBlendI > 1 and selectedLinkBlendI > 1:
            add_row();


def add_row(*args):
    cmds.scriptTable('scrtable', edit=True, selectedRows=[])
	
    selectedBlend = cmds.optionMenu('targetObjectMenu', query=True, value=True )
    selectedBlendI = cmds.optionMenu('targetObjectMenu', query=True, select=True )
    selectedLinkBlend = cmds.optionMenu('paramObjectMenu', query=True, value=True )
    selectedLinkBlendI = cmds.optionMenu('paramObjectMenu', query=True, select=True )
	
    last_row_num = cmds.scriptTable('scrtable', query=True, rows=True)
    cmds.scriptTable('scrtable', edit=True,insertRow=last_row_num)
	
    cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 1], cv=selectedBlend)
    cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 2], cv=selectedLinkBlend)
    cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 3], cv='0')
    cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 4], cv='1')
    cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 5], cv=selectedBlendI)
    cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 6], cv=selectedLinkBlendI)



def deformface():
    global dataarray
    if len(dataarray) < 3:
    	return 0
		
    all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
    global recstart
    global gnumcurrenttime
    if all_rows > 1 and recstart == 1:
        ornum = 1;
		
        numcurrenttime = gnumcurrenttime
        bonename = cmds.textField('HeadbonenameF', q=True, tx=True )
		
        if len(bonename) > 0:
            cX = cmds.textField('HeadbonenameXF', q=True, tx=True )
            cY = cmds.textField('HeadbonenameYF', q=True, tx=True )
            cZ = cmds.textField('HeadbonenameZF', q=True, tx=True )
            CrX = 0;
            CrY = 0;
            CrZ = 0;
            if cX.replace(".","").isdigit():
                CrX = float(cX);
            if cY.replace(".","").isdigit():
                CrY = float(cY);
            if cZ.replace(".","").isdigit():
                CrZ = float(cZ);
			
            bjoint = pm.PyNode(bonename)
            pm.rotate(bjoint, [float(dataarray[0])*-1+CrX ,float(dataarray[1])*-1+CrY,float(dataarray[2])*-1+CrZ], euler= True,a=True, ws=False)
            #if recnow ==1
            pm.setKeyframe(bjoint, v=float(dataarray[0])*-1+CrX, attribute='rotateX', t=[numcurrenttime])
            pm.setKeyframe(bjoint, v=float(dataarray[1])*-1+CrY, attribute='rotateY', t=[numcurrenttime])
            pm.setKeyframe(bjoint, v=float(dataarray[2])*-1+CrZ, attribute='rotateZ', t=[numcurrenttime])
		
        for i in range(all_rows):
            all_colums = cmds.scriptTable('scrtable', query=True, columns=True)
            data_list = []
            for j in range(all_colums):
                cell_list = cmds.scriptTable('scrtable', cellIndex=(i,j), query=True, cellValue=True)
                if type(cell_list) == 'list':
                    cell_text = "".join(cell_list)
                elif cell_list == None:
                    cell_text = cell_list
                else:
                    cell_text = cell_list[0]

                data_list.append(cell_text)
			
            if i > 0 and len(dataarray) > 3:
                streng = 1.0
                if data_list[4].replace(".","").isdigit():
                    streng = float(data_list[4])
                #recdataDeformStreng = (((float(dataarray[int(data_list[6])-2+3]))+0.0)/100.0)*(streng+0.0)
                recdataDeformStreng = (((float(dataarray[int(data_list[6])-2+3]))+0.0)/33.0)*(streng+0.0)
                targetdefnum = int(data_list[5])-2;
                cmds.blendShape( selectedBlend, edit=True, w=[(targetdefnum, recdataDeformStreng)] )
                #if recnow ==1
                cmds.setKeyframe("%s.w[%i]" %(selectedBlend,targetdefnum),t=numcurrenttime)
				
                if random.random() < 0.2:
                    datastring = '%.4f' % recdataDeformStreng
                    cmds.scriptTable('scrtable', e=True, ci=[i, 3], cv=datastring)


def portData(arg):
    """
    Read the 'serial' data passed in from the commandPort
    """
    global recend
    global dataarray

    dataarray=[]
    recVal = str(arg)
    strArray = recVal.split(",")
    for i in range(0,23):
        dataarray.append(strArray[i])
        print(strArray[i])
    #createTimer(0.03, deformface)
    deformface()

    
def deactivateCommandPort(host, port):
    path = host + ":" + port
    active = cmds.commandPort(path, q=True)
    if active:
        cmds.commandPort(name=path, cl=True)
    else:
        print("%s is was not active" % path)


def createTimer(seconds, function, *args, **kwargs):
    def isItTime():
        now = time.time()
        if now - isItTime.then > seconds:
            isItTime.then = now			# swap the order of these two lines ...
            function(*args, **kwargs)	  # ... to wait before restarting timer

        isItTime.then = 0#time.time() # set this to zero if you want it to fire once immediately
        cmds.scriptJob(event=("idle", isItTime))
