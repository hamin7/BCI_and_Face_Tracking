import maya.cmds as cmds

cube_ = cmds.polyCube()
cube_shape = cmds.polyCube(n='shape_cube')
cmds.select(cube_shape[0], cube_[0])

cmds.blendShape ( n="Test_SHP")
cmds.delete('shape_cube')
cmds.select(cl=1)
joint_=cmds.joint()

cmds.select(cube_,joint_)
cmds.SmoothBindSkin()

cmds.select(cube_[0])
shapes=cmds.listRelatives(cmds.ls(sl=1),s=1)[0]
blendShape=cmds.listConnections(shapes,type="blendShape")

print blendShape
