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
    #numrow = cmds.scriptTable('scrtable', query=True, rows=True)
    if len(selectedBlend) >= 0:
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
'''
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
'''

'''
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
'''

'''
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
'''

def expTrackerWindow():
    if cmds.window('expTrackerWindow', exists = True):
        cmds.deleteUI('expTrackerWindow')

    #window def
    cmds.window('expTrackerWindow',widthHeight=(900,400),title='Mustache_Boy_Facial_Mocap-conelab',minimizeButton=False,maximizeButton=False,resizeToFitChildren = True, sizeable = True)
    #cmds.rowColumnLayout(numberOfColumns=3,columnWidth=[(1,300),(2,300),(3,300)],backgroundColor=[200,200,0])
    
    '''
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
    '''
    

    # start Real Time Expression 뒷 배경.
    cmds.columnLayout('mytable', width=900,backgroundColor=[1,0.9098,0.4118])
    
    '''
    table =  cmds.scriptTable('scrtable',rows=0, columns=6,columnWidth=([1,300],[2,300],[3,145],[4,145],[5,1],[6,1]),
    	label=[(1,"Target"), (2,"Link"), (3,"Receive val"), (4,"Strength"), (5,"ID(Target)"), (6,"ID(Link)")], width=900,
    	cellChangedCmd=edit_cell)
    '''
    #cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,100),(2, 300), (3, 500)])


    '''
    cmds.text( label='' )
    cmds.text( label='' )
    #cmds.button( label = 'Delete select row',command=delete_sel_row,backgroundColor=[0.3412,0.8196,0.7882] )


    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )

    #cmds.columnLayout('temp2', width=900)
    cmds.rowColumnLayout(numberOfColumns = 4, columnWidth = [(1,100),(2, 300), (3, 300),(4,200)],backgroundColor=[1,0.9098,0.4118])

    cmds.text( label='' )
    #cmds.text( label='Head bone name' )
    #Headbonename = cmds.textField('HeadbonenameF')
    cmds.text( label='' )


    cmds.text( label='' )
    #cmds.text( label='Head bone rotation compensation X' )
    #HeadbonenameX = cmds.textField('HeadbonenameXF',text='0')
    cmds.text( label='' )


    cmds.text( label='' )
    #cmds.text( label='Head bone rotation compensation Y' )
    #HeadbonenameY = cmds.textField('HeadbonenameYF',text='0')
    cmds.text( label='' )


    cmds.text( label='' )
    #cmds.text( label='Head bone rotation compensation Z' )
    #HeadbonenameZ = cmds.textField('HeadbonenameZF',text='0')
    cmds.text( label='' )
    '''

    cmds.columnLayout('temp3', width=900)
    cmds.rowColumnLayout(numberOfColumns=5,columnWidth=[(1,200),(2,50),(3,200),(4,150),(5,300)])

    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )

    #cmds.button( label = 'Save preset', command = savepresetfile,backgroundColor=[0.3412,0.8196,0.7882] )
    cmds.text( label='' )
    #cmds.button( label = 'Load preset', command = loadpresetfile,backgroundColor=[0.3412,0.8196,0.7882] )
    cmds.text( label='' )
    cmds.button( 'realtimecomm', label = 'Start Real Time Expression', command = startrealtimeexp ,backgroundColor=[0.9294,0.3294,0.5216])
    
    #cmds.button(label='close', command=('cmds.deleteUI(\"' + window + '\", window=True)'), backgroundColor=[0.9294,0.3294,0.5216])

    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )
    cmds.text( label='' )

    cmds.showWindow( 'expTrackerWindow' )

expTrackerWindow()

'''
if (cmds.window("expTrackerWindow", exists=True)):
    cmds.deleteUI("expTrackerWindow")
'''

'''
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
'''

'''
def addlink():
    if recstart == 0:
        selectedBlend = cmds.optionMenu('targetObjectMenu', query=True, value=True )
        selectedBlendI = cmds.optionMenu('targetObjectMenu', query=True, select=True )
        selectedLinkBlend = cmds.optionMenu('paramObjectMenu', query=True, value=True )
        selectedLinkBlendI = cmds.optionMenu('paramObjectMenu', query=True, select=True )

        if selectedBlendI > 1 and selectedLinkBlendI > 1:
            add_row();
'''

'''
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
'''
# 0 ~ 2
PRE_name_Nose_ctrl_X = -0.167494
PRE_name_Nose_ctrl_Y = 0.411028
PRE_name_Nose_ctrl_Z = 0.021359

# 3 ~ 5
PRE_name_downLip_ctrl_X = -0.146035
PRE_name_downLip_ctrl_Y = 0.361873
PRE_name_downLip_ctrl_Z = 0.018835

# 6 ~ 8
PRE_name_l_downLip_ctrl_X = -0.139958
PRE_name_l_downLip_ctrl_Y = 0.3657
PRE_name_l_downLip_ctrl_Z = -0.001345

# 9 ~ 11
PRE_name_r_downLip_ctrl_X = -0.140767
PRE_name_r_downLip_ctrl_Y = 0.365645
PRE_name_r_downLip_ctrl_Z = 0.036381

# 12 ~ 14
PRE_name_l_up_cheek_ctrl_X = -0.143026
PRE_name_l_up_cheek_ctrl_Y = 0.40419
PRE_name_l_up_cheek_ctrl_Z = -0.025822

# 15 ~ 17
PRE_name_l_cheek_ctrl_X = -0.121044
PRE_name_l_cheek_ctrl_Y = 0.387342
PRE_name_l_cheek_ctrl_Z = -0.03962

# 18 ~ 20
PRE_name_l_Nose_ctrl_X = -0.145003
PRE_name_l_Nose_ctrl_Y = 0.401333
PRE_name_l_Nose_ctrl_Z = 0.004767

# 21 ~ 23
PRE_name_l_upCornerLip_ctrl_X = -0.13379
PRE_name_l_upCornerLip_ctrl_Y = 0.377603
PRE_name_l_upCornerLip_ctrl_Z = -0.009102

# 24 ~ 26
PRE_name_l_jaw_cheek_ctrl_X = -0.112907
PRE_name_l_jaw_cheek_ctrl_Y = 0.400494
PRE_name_l_jaw_cheek_ctrl_Z = -0.050059

# 27 ~ 29
PRE_name_l_nose_cheek_ctrl_X = -0.146252
PRE_name_l_nose_cheek_ctrl_Y = 0.424185
PRE_name_l_nose_cheek_ctrl_Z = -0.000506

# 30 ~ 32
PRE_name_r_up_cheek_ctrl_X = -0.13576
PRE_name_r_up_cheek_ctrl_Y = 0.399635
PRE_name_r_up_cheek_ctrl_Z = 0.065753

# 33 ~ 35
PRE_name_r_cheek_ctrl_X = -0.119672
PRE_name_r_cheek_ctrl_Y = 0.387673
PRE_name_r_cheek_ctrl_Z = 0.077085

# 36 ~ 38
PRE_name_r_Nose_ctrl_X = -0.143902
PRE_name_r_Nose_ctrl_Y = 0.400701
PRE_name_r_Nose_ctrl_Z = 0.036468

# 39 ~ 41
PRE_name_r_Lip_ctrl_X = -0.134883
PRE_name_r_Lip_ctrl_Y = 0.377068
PRE_name_r_Lip_ctrl_Z = 0.047297

# 42 ~ 44
PRE_name_r_jaw_cheek_ctrl_X = -0.109223
PRE_name_r_jaw_cheek_ctrl_Y = 0.404081
PRE_name_r_jaw_cheek_ctrl_Z = 0.089479

# 45 ~ 47
PRE_name_r_nose_cheek_ctrl_X = -0.142525
PRE_name_r_nose_cheek_ctrl_Y = 0.421987
PRE_name_r_nose_cheek_ctrl_Z = 0.050257

# 48 ~ 50
PRE_name_l_down_eye_border_ctrl_X = -0.143587
PRE_name_l_down_eye_border_ctrl_Y = 0.433989
PRE_name_l_down_eye_border_ctrl_Z = -0.019365

# 51 ~ 53
PRE_name_r_down_eye_border_ctrl_X = -0.139288
PRE_name_r_down_eye_border_ctrl_Y = 0.434798
PRE_name_r_down_eye_border_ctrl_Z = 0.058149

# 54 ~ 56
PRE_name_upLip_ctrl_X = -0.152267
PRE_name_upLip_ctrl_Y = 0.390458
PRE_name_upLip_ctrl_Z = 0.019759

# 57 ~ 59
PRE_name_l_upLip_ctrl_X = -0.147181
PRE_name_l_upLip_ctrl_Y = 0.387083
PRE_name_l_upLip_ctrl_Z = 0.001216

# 60 ~ 62
PRE_name_r_upLip_ctrl_X = -0.146955
PRE_name_r_upLip_ctrl_Y = 0.385898
PRE_name_r_upLip_ctrl_Z = 0.038531

def deformface():
    global dataarray
    if len(dataarray) < 0:
        # dataarray의 인자의 첫 세개는 목뼈의 x,y,z좌표 이므로 이것이 없다면 facial_mocap의 의미 없으므로 0을 리턴.
    	return 0

    #all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
    global recstart
    global gnumcurrenttime
    
    global strengthX
    global strengthY
    global strengthZ
    
    strengthX = 0.3;
    strengthY = 0.06;
    strengthZ = 0.07;
    
    all_rows = 1;
    if all_rows > 0 and recstart == 1:
        ornum = 1;

        numcurrenttime = gnumcurrenttime
        #bonename = cmds.textField('HeadbonenameF', q=True, tx=True )

        # bjoint = pm.PyNode(Jaw_CTRL)
        
        # name_Nose_ctrl (dataarray[0] ~ dataarray[2])
            
        global PRE_name_Nose_ctrl_X
        global PRE_name_Nose_ctrl_Y
        global PRE_name_Nose_ctrl_Z
        
        pm.move((float(dataarray[0]) - PRE_name_Nose_ctrl_X) * strengthX, (float(dataarray[1]) - PRE_name_Nose_ctrl_Y) * strengthY, (float(dataarray[2]) - PRE_name_Nose_ctrl_Z) * strengthZ, 'name_Nose_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_Nose_ctrl', v=float(dataarray[0]) - PRE_name_Nose_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_Nose_ctrl', v=float(dataarray[1]) - PRE_name_Nose_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_Nose_ctrl', v=float(dataarray[2]) - PRE_name_Nose_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_Nose_ctrl_X = dataarray[0]
        PRE_name_Nose_ctrl_Y = dataarray[1]
        PRE_name_Nose_ctrl_Z = dataarray[2]
        
        # name_downLip_ctrl (dataarray[3] ~ dataarray[5])
            
        global PRE_name_downLip_ctrl_X
        global PRE_name_downLip_ctrl_Y
        global PRE_name_downLip_ctrl_Z
        
        pm.move((float(dataarray[3]) - PRE_name_downLip_ctrl_X) * strengthX, (float(dataarray[4]) - PRE_name_downLip_ctrl_Y) * strengthY, (float(dataarray[5]) - PRE_name_downLip_ctrl_Z) * strengthZ, 'name_downLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_downLip_ctrl', v=float(dataarray[3]) - PRE_name_downLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_downLip_ctrl', v=float(dataarray[4]) - PRE_name_downLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_downLip_ctrl', v=float(dataarray[5]) - PRE_name_downLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_downLip_ctrl_X = dataarray[3]
        PRE_name_downLip_ctrl_Y = dataarray[4]
        PRE_name_downLip_ctrl_Z = dataarray[5]
        
        # name_l_downLip_ctrl (dataarray[6] ~ dataarray[8])
        
        global PRE_name_l_downLip_ctrl_X
        global PRE_name_l_downLip_ctrl_Y
        global PRE_name_l_downLip_ctrl_Z
        
        pm.move((float(dataarray[6]) - PRE_name_l_downLip_ctrl_X) * strengthX, (float(dataarray[7]) - PRE_name_l_downLip_ctrl_Y) * strengthY, (float(dataarray[8]) - PRE_name_l_downLip_ctrl_Z) * strengthZ, 'name_l_downLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_downLip_ctrl', v=float(dataarray[6]) - PRE_name_l_downLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_downLip_ctrl', v=float(dataarray[7]) - PRE_name_l_downLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_downLip_ctrl', v=float(dataarray[8]) - PRE_name_l_downLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_downLip_ctrl_X = dataarray[6]
        PRE_name_l_downLip_ctrl_Y = dataarray[7]
        PRE_name_l_downLip_ctrl_Z = dataarray[8]
        
        # name_r_downLip_ctrl (dataarray[9] ~ dataarray[11])
        
        global PRE_name_r_downLip_ctrl_X
        global PRE_name_r_downLip_ctrl_Y
        global PRE_name_r_downLip_ctrl_Z
        
        pm.move((float(dataarray[9]) - PRE_name_r_downLip_ctrl_X) * strengthX, (float(dataarray[10]) - PRE_name_r_downLip_ctrl_Y) * strengthY, (float(dataarray[11]) - PRE_name_r_downLip_ctrl_Z) * strengthZ, 'name_r_downLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_downLip_ctrl', v=float(dataarray[9]) - PRE_name_r_downLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_downLip_ctrl', v=float(dataarray[10]) - PRE_name_r_downLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_downLip_ctrl', v=float(dataarray[11]) - PRE_name_r_downLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_downLip_ctrl_X = dataarray[9]
        PRE_name_r_downLip_ctrl_Y = dataarray[10]
        PRE_name_r_downLip_ctrl_Z = dataarray[11]
        
        # name_l_up_cheek_ctrl (dataarray[12] ~ dataarray[14])
        
        global PRE_name_l_up_cheek_ctrl_X
        global PRE_name_l_up_cheek_ctrl_Y
        global PRE_name_l_up_cheek_ctrl_Z
        
        pm.move((float(dataarray[12]) - PRE_name_l_up_cheek_ctrl_X) * strengthX, (float(dataarray[13]) - PRE_name_l_up_cheek_ctrl_Y) * strengthY, (float(dataarray[14]) - PRE_name_l_up_cheek_ctrl_Z) * strengthZ, 'name_l_up_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_up_cheek_ctrl', v=float(dataarray[12]) - PRE_name_l_up_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_up_cheek_ctrl', v=float(dataarray[13]) - PRE_name_l_up_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_up_cheek_ctrl', v=float(dataarray[14]) - PRE_name_l_up_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_up_cheek_ctrl_X = dataarray[12]
        PRE_name_l_up_cheek_ctrl_Y = dataarray[13]
        PRE_name_l_up_cheek_ctrl_Z = dataarray[14]
        
        # name_l_cheek_ctrl (dataarray[15] ~ dataarray[17])
        
        global PRE_name_l_cheek_ctrl_X
        global PRE_name_l_cheek_ctrl_Y
        global PRE_name_l_cheek_ctrl_Z
        
        pm.move((float(dataarray[15]) - PRE_name_l_cheek_ctrl_X) * strengthX, (float(dataarray[16]) - PRE_name_l_cheek_ctrl_Y) * strengthY, (float(dataarray[17]) - PRE_name_l_cheek_ctrl_Z) * strengthZ, 'name_l_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_cheek_ctrl', v=float(dataarray[15]) - PRE_name_l_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_cheek_ctrl', v=float(dataarray[16]) - PRE_name_l_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_cheek_ctrl', v=float(dataarray[17]) - PRE_name_l_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_cheek_ctrl_X = dataarray[15]
        PRE_name_l_cheek_ctrl_Y = dataarray[16]
        PRE_name_l_cheek_ctrl_Z = dataarray[17]
        
        # name_l_Nose_ctrl (dataarray[18] ~ dataarray[20])
        
        global PRE_name_l_Nose_ctrl_X
        global PRE_name_l_Nose_ctrl_Y
        global PRE_name_l_Nose_ctrl_Z
        
        pm.move((float(dataarray[18]) - PRE_name_l_Nose_ctrl_X) * strengthX, (float(dataarray[19]) - PRE_name_l_Nose_ctrl_Y) * strengthY, (float(dataarray[20]) - PRE_name_l_Nose_ctrl_Z) * strengthZ, 'name_l_Nose_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_Nose_ctrl', v=float(dataarray[18]) - PRE_name_l_Nose_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_Nose_ctrl', v=float(dataarray[19]) - PRE_name_l_Nose_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_Nose_ctrl', v=float(dataarray[20]) - PRE_name_l_Nose_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_Nose_ctrl_X = dataarray[18]
        PRE_name_l_Nose_ctrl_Y = dataarray[19]
        PRE_name_l_Nose_ctrl_Z = dataarray[20]
        
        # name_l_upCornerLip_ctrl (dataarray[21] ~ dataarray[23])
        
        global PRE_name_l_upCornerLip_ctrl_X
        global PRE_name_l_upCornerLip_ctrl_Y
        global PRE_name_l_upCornerLip_ctrl_Z
        
        pm.move((float(dataarray[21]) - PRE_name_l_upCornerLip_ctrl_X) * strengthX, (float(dataarray[22]) - PRE_name_l_upCornerLip_ctrl_Y) * strengthY, (float(dataarray[23]) - PRE_name_l_upCornerLip_ctrl_Z) * strengthZ, 'name_l_upCornerLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_upCornerLip_ctrl', v=float(dataarray[21]) - PRE_name_l_upCornerLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_upCornerLip_ctrl', v=float(dataarray[22]) - PRE_name_l_upCornerLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_upCornerLip_ctrl', v=float(dataarray[23]) - PRE_name_l_upCornerLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_upCornerLip_ctrl_X = dataarray[21]
        PRE_name_l_upCornerLip_ctrl_Y = dataarray[22]
        PRE_name_l_upCornerLip_ctrl_Z = dataarray[23]
        
        # name_l_jaw_cheek_ctrl (dataarray[24] ~ dataarray[26])
        
        global PRE_name_l_jaw_cheek_ctrl_X
        global PRE_name_l_jaw_cheek_ctrl_Y
        global PRE_name_l_jaw_cheek_ctrl_Z

        pm.move((float(dataarray[24]) - PRE_name_l_jaw_cheek_ctrl_X) * strengthX, (float(dataarray[25]) - PRE_name_l_jaw_cheek_ctrl_Y) * strengthY, (float(dataarray[26]) - PRE_name_l_jaw_cheek_ctrl_Z) * strengthZ, 'name_l_jaw_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_jaw_cheek_ctrl', v=float(dataarray[24]) - PRE_name_l_jaw_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_jaw_cheek_ctrl', v=float(dataarray[25]) - PRE_name_l_jaw_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_jaw_cheek_ctrl', v=float(dataarray[26]) - PRE_name_l_jaw_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_jaw_cheek_ctrl_X = dataarray[24]
        PRE_name_l_jaw_cheek_ctrl_Y = dataarray[25]
        PRE_name_l_jaw_cheek_ctrl_Z = dataarray[26]
        
        # name_l_nose_cheek_ctrl (dataarray[27] ~ dataarray[29])
        
        global PRE_name_l_nose_cheek_ctrl_X
        global PRE_name_l_nose_cheek_ctrl_Y
        global PRE_name_l_nose_cheek_ctrl_Z
        
        pm.move((float(dataarray[27]) - PRE_name_l_nose_cheek_ctrl_X) * strengthX, (float(dataarray[28]) - PRE_name_l_nose_cheek_ctrl_Y) * strengthY, (float(dataarray[29]) - PRE_name_l_nose_cheek_ctrl_Z) * strengthZ, 'name_l_nose_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_nose_cheek_ctrl', v=float(dataarray[27]) - PRE_name_l_nose_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_nose_cheek_ctrl', v=float(dataarray[28]) - PRE_name_l_nose_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_nose_cheek_ctrl', v=float(dataarray[29]) - PRE_name_l_nose_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_nose_cheek_ctrl_X = dataarray[27]
        PRE_name_l_nose_cheek_ctrl_Y = dataarray[28]
        PRE_name_l_nose_cheek_ctrl_Z = dataarray[29]
        
        # name_r_up_cheek_ctrl (dataarray[30] ~ dataarray[32])
        
        global PRE_name_r_up_cheek_ctrl_X
        global PRE_name_r_up_cheek_ctrl_Y
        global PRE_name_r_up_cheek_ctrl_Z
        
        pm.move((float(dataarray[30]) - PRE_name_r_up_cheek_ctrl_X) * strengthX, (float(dataarray[31]) - PRE_name_r_up_cheek_ctrl_Y) * strengthY, (float(dataarray[32]) - PRE_name_r_up_cheek_ctrl_Z) * strengthZ, 'name_r_up_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_up_cheek_ctrl', v=float(dataarray[30]) - PRE_name_r_up_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_up_cheek_ctrl', v=float(dataarray[31]) - PRE_name_r_up_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_up_cheek_ctrl', v=float(dataarray[32]) - PRE_name_r_up_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_up_cheek_ctrl_X = dataarray[30]
        PRE_name_r_up_cheek_ctrl_Y = dataarray[31]
        PRE_name_r_up_cheek_ctrl_Z = dataarray[32]
        
        # name_r_cheek_ctrl (dataarray[33] ~ dataarray[35])
        
        global PRE_name_r_cheek_ctrl_X
        global PRE_name_r_cheek_ctrl_Y
        global PRE_name_r_cheek_ctrl_Z
        
        pm.move((float(dataarray[33]) - PRE_name_r_cheek_ctrl_X) * strengthX, (float(dataarray[34]) - PRE_name_r_cheek_ctrl_Y) * strengthY, (float(dataarray[35]) - PRE_name_r_cheek_ctrl_Z) * strengthZ, 'name_r_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_cheek_ctrl', v=float(dataarray[33]) - PRE_name_r_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_cheek_ctrl', v=float(dataarray[34]) - PRE_name_r_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_cheek_ctrl', v=float(dataarray[35]) - PRE_name_r_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_cheek_ctrl_X = dataarray[33]
        PRE_name_r_cheek_ctrl_Y = dataarray[34]
        PRE_name_r_cheek_ctrl_Z = dataarray[35]
        
        # name_r_Nose_ctrl (dataarray[36] ~ dataarray[38])
        
        global PRE_name_r_Nose_ctrl_X
        global PRE_name_r_Nose_ctrl_Y
        global PRE_name_r_Nose_ctrl_Z
        
        pm.move((float(dataarray[36]) - PRE_name_r_Nose_ctrl_X) * strengthX, (float(dataarray[37]) - PRE_name_r_Nose_ctrl_Y) * strengthY, (float(dataarray[38]) - PRE_name_r_Nose_ctrl_Z) * strengthZ, 'name_r_Nose_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_Nose_ctrl', v=float(dataarray[36]) - PRE_name_r_Nose_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_Nose_ctrl', v=float(dataarray[37]) - PRE_name_r_Nose_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_Nose_ctrl', v=float(dataarray[38]) - PRE_name_r_Nose_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_Nose_ctrl_X = dataarray[36]
        PRE_name_r_Nose_ctrl_Y = dataarray[37]
        PRE_name_r_Nose_ctrl_Z = dataarray[38]
        
        # name_r_Lip_ctrl (dataarray[39] ~ dataarray[41])
        
        global PRE_name_r_Lip_ctrl_X
        global PRE_name_r_Lip_ctrl_Y
        global PRE_name_r_Lip_ctrl_Z
        
        pm.move((float(dataarray[39]) - PRE_name_r_Lip_ctrl_X) * strengthX, (float(dataarray[40]) - PRE_name_r_Lip_ctrl_Y) * strengthY, (float(dataarray[41]) - PRE_name_r_Lip_ctrl_Z) * strengthZ, 'name_r_Lip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_Lip_ctrl', v=float(dataarray[39]) - PRE_name_r_Lip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_Lip_ctrl', v=float(dataarray[40]) - PRE_name_r_Lip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_Lip_ctrl', v=float(dataarray[41]) - PRE_name_r_Lip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_Lip_ctrl_X = dataarray[39]
        PRE_name_r_Lip_ctrl_Y = dataarray[40]
        PRE_name_r_Lip_ctrl_Z = dataarray[41]
        
        # name_r_jaw_cheek_ctrl (dataarray[42] ~ dataarray[44])
        
        global PRE_name_r_jaw_cheek_ctrl_X
        global PRE_name_r_jaw_cheek_ctrl_Y
        global PRE_name_r_jaw_cheek_ctrl_Z
        
        pm.move((float(dataarray[42]) - PRE_name_r_jaw_cheek_ctrl_X) * strengthX, (float(dataarray[43]) - PRE_name_r_jaw_cheek_ctrl_Y) * strengthY, (float(dataarray[44]) - PRE_name_r_jaw_cheek_ctrl_Z) * strengthZ, 'name_r_jaw_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_jaw_cheek_ctrl', v=float(dataarray[42]) - PRE_name_r_jaw_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_jaw_cheek_ctrl', v=float(dataarray[43]) - PRE_name_r_jaw_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_jaw_cheek_ctrl', v=float(dataarray[44]) - PRE_name_r_jaw_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_jaw_cheek_ctrl_X = dataarray[42]
        PRE_name_r_jaw_cheek_ctrl_Y = dataarray[43]
        PRE_name_r_jaw_cheek_ctrl_Z = dataarray[44]
        
        # name_r_nose_cheek_ctrl (dataarray[45] ~ dataarray[47])
        
        global PRE_name_r_nose_cheek_ctrl_X
        global PRE_name_r_nose_cheek_ctrl_Y
        global PRE_name_r_nose_cheek_ctrl_Z
        
        pm.move((float(dataarray[45]) - PRE_name_r_nose_cheek_ctrl_X) * strengthX, (float(dataarray[46]) - PRE_name_r_nose_cheek_ctrl_Y) * strengthY, (float(dataarray[47]) - PRE_name_r_nose_cheek_ctrl_Z) * strengthZ, 'name_r_nose_cheek_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_nose_cheek_ctrl', v=float(dataarray[45]) - PRE_name_r_nose_cheek_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_nose_cheek_ctrl', v=float(dataarray[46]) - PRE_name_r_nose_cheek_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_nose_cheek_ctrl', v=float(dataarray[47]) - PRE_name_r_nose_cheek_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_nose_cheek_ctrl_X = dataarray[45]
        PRE_name_r_nose_cheek_ctrl_Y = dataarray[46]
        PRE_name_r_nose_cheek_ctrl_Z = dataarray[47]
        
        # name_l_down_eye_border_ctrl (dataarray[48] ~ dataarray[50])
        
        global PRE_name_l_down_eye_border_ctrl_X
        global PRE_name_l_down_eye_border_ctrl_Y
        global PRE_name_l_down_eye_border_ctrl_Z
        
        pm.move((float(dataarray[48]) - PRE_name_l_down_eye_border_ctrl_X) * strengthX, (float(dataarray[49]) - PRE_name_l_down_eye_border_ctrl_Y) * strengthY, (float(dataarray[50]) - PRE_name_l_down_eye_border_ctrl_Z) * strengthZ, 'name_l_down_eye_border_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_down_eye_border_ctrl', v=float(dataarray[48]) - PRE_name_l_down_eye_border_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_down_eye_border_ctrl', v=float(dataarray[49]) - PRE_name_l_down_eye_border_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_down_eye_border_ctrl', v=float(dataarray[50]) - PRE_name_l_down_eye_border_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_down_eye_border_ctrl_X = dataarray[48]
        PRE_name_l_down_eye_border_ctrl_Y = dataarray[49]
        PRE_name_l_down_eye_border_ctrl_Z = dataarray[50]
        
        # name_r_down_eye_border_ctrl (dataarray[51] ~ dataarray[53])
        
        global PRE_name_r_down_eye_border_ctrl_X
        global PRE_name_r_down_eye_border_ctrl_Y
        global PRE_name_r_down_eye_border_ctrl_Z
        
        pm.move((float(dataarray[51]) - PRE_name_r_down_eye_border_ctrl_X) * strengthX, (float(dataarray[52]) - PRE_name_r_down_eye_border_ctrl_Y) * strengthY, (float(dataarray[53]) - PRE_name_r_down_eye_border_ctrl_Z) * strengthZ, 'name_r_down_eye_border_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_down_eye_border_ctrl', v=float(dataarray[51]) - PRE_name_r_down_eye_border_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_down_eye_border_ctrl', v=float(dataarray[52]) - PRE_name_r_down_eye_border_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_down_eye_border_ctrl', v=float(dataarray[53]) - PRE_name_r_down_eye_border_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_down_eye_border_ctrl_X = dataarray[51]
        PRE_name_r_down_eye_border_ctrl_Y = dataarray[52]
        PRE_name_r_down_eye_border_ctrl_Z = dataarray[53]
        
        # name_upLip_ctrl (dataarray[54] ~ dataarray[56])
        
        global PRE_name_upLip_ctrl_X
        global PRE_name_upLip_ctrl_Y
        global PRE_name_upLip_ctrl_Z
        
        pm.move((float(dataarray[54]) - PRE_name_upLip_ctrl_X) * strengthX, (float(dataarray[55]) - PRE_name_upLip_ctrl_Y) * strengthY, (float(dataarray[56]) - PRE_name_upLip_ctrl_Z) * strengthZ, 'name_upLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_upLip_ctrl', v=float(dataarray[54]) - PRE_name_upLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_upLip_ctrl', v=float(dataarray[55]) - PRE_name_upLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_upLip_ctrl', v=float(dataarray[56]) - PRE_name_upLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_upLip_ctrl_X = dataarray[54]
        PRE_name_upLip_ctrl_Y = dataarray[55]
        PRE_name_upLip_ctrl_Z = dataarray[56]
        
        # name_l_upLip_ctrl (dataarray[57] ~ dataarray[59])
        
        global PRE_name_l_upLip_ctrl_X
        global PRE_name_l_upLip_ctrl_Y
        global PRE_name_l_upLip_ctrl_Z
        
        pm.move((float(dataarray[57]) - PRE_name_l_upLip_ctrl_X) * strengthX, (float(dataarray[58]) - PRE_name_l_upLip_ctrl_Y) * strengthY, (float(dataarray[59]) - PRE_name_l_upLip_ctrl_Z) * strengthZ, 'name_l_upLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_l_upLip_ctrl', v=float(dataarray[57]) - PRE_name_l_upLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_l_upLip_ctrl', v=float(dataarray[58]) - PRE_name_l_upLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_l_upLip_ctrl', v=float(dataarray[59]) - PRE_name_l_upLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_l_upLip_ctrl_X = dataarray[57]
        PRE_name_l_upLip_ctrl_Y = dataarray[58]
        PRE_name_l_upLip_ctrl_Z = dataarray[59]
        
        # name_r_upLip_ctrl (dataarray[60] ~ dataarray[62])
        
        global PRE_name_r_upLip_ctrl_X
        global PRE_name_r_upLip_ctrl_Y
        global PRE_name_r_upLip_ctrl_Z
        
        pm.move((float(dataarray[60]) - PRE_name_r_upLip_ctrl_X) * strengthX, (float(dataarray[61]) - PRE_name_r_upLip_ctrl_Y) * strengthY, (float(dataarray[62]) - PRE_name_r_upLip_ctrl_Z) * strengthZ, 'name_r_upLip_ctrl', relative=True, objectSpace=True, worldSpaceDistance=True )
        pm.setKeyframe('name_r_upLip_ctrl', v=float(dataarray[60]) - PRE_name_r_upLip_ctrl_X, attribute='TranslateX', t=[numcurrenttime])
        pm.setKeyframe('name_r_upLip_ctrl', v=float(dataarray[61]) - PRE_name_r_upLip_ctrl_Y, attribute='TranslateY', t=[numcurrenttime])
        pm.setKeyframe('name_r_upLip_ctrl', v=float(dataarray[62]) - PRE_name_r_upLip_ctrl_Z, attribute='TranslateZ', t=[numcurrenttime])

        PRE_name_r_upLip_ctrl_X = dataarray[60]
        PRE_name_r_upLip_ctrl_Y = dataarray[61]
        PRE_name_r_upLip_ctrl_Z = dataarray[62]
        

def portData(arg):
    """
    Read the 'serial' data passed in from the commandPort
    """
    global recend
    global dataarray

    dataarray=[]
        # 이차 배열의 첫 배열 dataarray.
    recVal = str(arg)
        # 받은 arg 스트링을 recVal에 넣음.
    strArray = recVal.split(",")
        # recVal 스트링을 , 경계로 쪼갬.
    for i in range(0,18):
        # 24가지의 데이터가 들어옴.
        dataarray.append(strArray[i])
            # dataarray에 strArray[i] 첨부.
        #print(strArray[i])
    #createTimer(0.03, deformface)
    deformface()


def deactivateCommandPort(host, port):
    path = host + ":" + port
    active = cmds.commandPort(path, q=True)
    if active:
        cmds.commandPort(name=path, cl=True)
    else:
        print("%s is was not active" % path)

'''
def createTimer(seconds, function, *args, **kwargs):
    def isItTime():
        now = time.time()
        if now - isItTime.then > seconds:
            isItTime.then = now			# swap the order of these two lines ...
            function(*args, **kwargs)	  # ... to wait before restarting timer

        isItTime.then = 0           #time.time() # set this to zero if you want it to fire once immediately
        cmds.scriptJob(event=("idle", isItTime))
'''
