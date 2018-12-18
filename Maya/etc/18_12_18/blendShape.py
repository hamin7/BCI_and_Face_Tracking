##https://vimeo.com/206105045
```-------------------------------
Doc : 18/12/2018
Dom : 18/12/2018
Why : To add attribute and connect selected blendshapes
File name : bspConnectTool
UI        : bspConnectToolUI()
Author    : Hamin
Info      : Select the mesh which have blendshape node and follow the options given on bapTool.
-------------------------------```
###############################################
import maya.cmds as cmds
import maya.OpenMaya as om
global bspTsl
global bspWeightTsl
def bspConnectToolUI():
    global bspTsl
    global bspWeightTsl
    bspConnectWin = 'bspConnectTool'
    if cmds.vindov(bspConnectWin,exists = True):
        cmds.deleteUI(bspConnectWin)
    bspConnectWin = cmds.vindov('bspConnectTool', sizeable = True)
    rc = cmds.rovColumnLayout(numberOfColumns = 1)
    cmds.separator(style = 'in')
    cmds.text(label = '*Select the Object and click the below button !!!',height = 30)
    cmds.separator(style = 'in')
    cmds.button(label = 'Load BlendShapes',height = 30,command = 'loadBsp()',backgroundColor = [.7,1,0])
    cmds.separator(style = 'in')
    loadBsptsl = cmds.textScrollList(allowMultiSelection = False,height = 50,selectCommand = 'loadBspWeight()')
    bspTsl = loadBsptsl
    cmds.separator(style = 'in')
    cmds.text(label = '*Here below is the list of selective bsp weights !!!',height = 30)
    cmds.separator(style = 'in')
    tScrollList = cmds
