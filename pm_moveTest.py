import maya.cmds as pm

dataarray = [0.32,0.12,51.11]

'''
recVal = str(arg)

strArray = recVal.split(",")

for i in range(0,3):
    dataarray.append(strArray[i])
    print(strArray[i])
'''

cX = 0;
cX = 0;
cX = 0;

CrX = 0;
CrY = 0;
CrZ = 0;

pm.move(float(dataarray[0])*-1+CrX ,float(dataarray[1])*-1+CrY,float(dataarray[2])*-1+CrZ, 'Jaw_CTRL', absolute=True )
#if recnow ==1
pm.setKeyframe('Jaw_CTRL', v=float(dataarray[0])*-1+CrX, attribute='TranslateX', t=[numcurrenttime])
# numcurrenttime 증가시키는 함수는 어딨지?
pm.setKeyframe('Jaw_CTRL', v=float(dataarray[1])*-1+CrY, attribute='TranslateY', t=[numcurrenttime])
pm.setKeyframe('Jaw_CTRL', v=float(dataarray[2])*-1+CrZ, attribute='TranslateZ', t=[numcurrenttime])
