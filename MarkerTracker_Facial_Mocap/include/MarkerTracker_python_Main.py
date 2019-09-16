# keyRotation.py

import maya.cmds as cmds

def keyFullRotation( pObjectName, pStartTime, pEndTime, pTargetAttribute ):

    cmds.cutKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute )

    # cmds.cutkey( objectName, time = (startTime, endTime), attribute='rotateY')    # 첫 인수 objectName은 키를 제거하려는 객체의 이름. time 플래그는 시작 및 종료 시간을 정의하는 튜플.
        # attribute 플래그는 애니메이션 된 속성의 이름. (이 경우 변환된 노드의 y축 회전의 경우 rotateY)

    cmds.setKeyframe( pObjectName, time=pStartTime, attribute=pTargetAttribute, value=0 )

    # cmds.setKeyframe( objectName, time=startTime, attribute='rotateY', value=0 )
        # 첫 인수는 키를 추가하려는 객체의 이름. time 플래그는 키가 설정되는 프레임을 결정.
        # attribute=pTargetAttribute는 애니메이션하려는 대상 속성의 이름.
        # value=0은 플래그에 주어진 시간에 키 값을 결정.
    # cmds.setKeyframe( objectname, time=endTime, attribute='rotateY', value=360 )

    cmds.setKeyframe( pObjectName, time=pEndTime, attribute=pTargetAttribute, value=360 )

    cmds.selectKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True )

    cmds.keyTangent( inTangentType='linear', outTangentType='linear' )


selectionList = cmds.ls( selection=True, type='transform' )

if len( selectionList ) >= 1:

    # print 'Selected items: %s' % ( selectionList )

    startTime = cmds.playbackOptions( query=True, minTime=True ) # 스크립트에서 작업을 자동화하기 위해 시간 슬라이더의 시작 및 종료 시간 필요. query 및 minTime=True로 설정 된 cmds.playbackOptions 호출하여 액세스.
    endTime = cmds.playbackOptions( query=True, maxTime=True ) # maxTime 플래그가 True로 설정되어 종료 시간 확보.

    for objectName in selectionList:

        # objectTypeResult = cmds.objectType( objectName )

        # print '%s type: %s' % ( objectName, objectTypeResult )

        keyFullRotation( objectName, startTime, endTime, 'rotateY' )


else:

    print 'Please select at least one object'
