#7777포트 
import maya.cmds as cmds
import maya.mel as mm

def activateCommandPort(host, port, type):
    path = host + ":" + port
    active = cmds.commandPort(path, q=True)
    if not active:
        cmds.commandPort(name=path, sourceType=type)
    else:
        print("%s is already active" % path)

def deactivateCommandPort(host, port):
    path = host + ":" + port
    active = cmds.commandPort(path, q=True)
    if active:
        cmds.commandPort(name=path, cl=True)
    else:
        print("%s is was not active" % path)

#Examples
#activateCommandPort('127.0.0.1', '7001', 'mel')
#activateCommandPort('127.0.0.1', '7002', 'python')
#deactivateCommandPort('127.0.0.1', '7001')
cmds.select( all=True )
cmds.cutKey(time=(0,108000))
cmds.select( clear=True )
cmds.play(state=False)
deactivateCommandPort('127.0.0.1', '7777')
#cmds.cutKey(time=(0,108000))
