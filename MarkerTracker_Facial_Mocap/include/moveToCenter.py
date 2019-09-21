import maya.cmds as mc

def moveToCenter(sel, center = True):
    if len(sel)<=0:
        print "select one object"
    if center:
        mc.xform (sel, centerPivots = center)
    else:
        bbox = mc.exactWorldBoundingBox(sel)
        bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
        mc.xform(sel, piv=bottom, ws=True)
    mc.move(0,0,0, sel, rotatePivotRelative = True)
if (mc.window("moveToCenter", exists=True)):
    mc.deleteUI("moveToCenter")
window = mc.window(title="moveToCenter", widthHeight=(150, 64) )
mc.columnLayout( adjustableColumn=True)
center = mc.checkBox(label='Center')
mc.button(label='Move To Center', command= 'moveToCenter(mc.ls(sl=True), mc.checkBox(center, query=True, value=True))')
mc.button(label='close', command=('mc.deleteUI(\"' + window + '\", window=True)'))
mc.setParent( '..' )
mc.showWindow( window )
