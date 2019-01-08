# In Maya, via Python:
import maya.cmds as mc
import maya.mel as mm

tempT = 0
count = 0
#defineKeyFrame
def keyAnim1(pObjName, pTargetAttr, pVal):
    global count
    global tempT
    if count==0:
        pCurTime = mc.currentTime(query=True)
        temp = pCurTime
        mc.setKeyframe(pObjName, time=temp, attribute=pTargetAttr, value=pVal)
        tempT=temp
        count+=1
    else:
        mc.setKeyframe(pObjName, time=tempT, attribute=pTargetAttr, value=pVal)
        count+=1
        if count==8: count=0
    
def keyAnim2(pObjName, pTargetAttr, pVal):
    global count
    global tempT
    if count==0:
        pCurTime = mc.currentTime(query=True)
        temp = pCurTime
        mc.setKeyframe(pObjName, time=temp, attribute=pTargetAttr, value=pVal)
        tempT=temp
        count+=1
    else:
        mc.setKeyframe(pObjName, time=tempT, attribute=pTargetAttr, value=pVal)
        count+=1
        if count==12: count=0
    
#defineVar
ebList = ['Ctl_Eyebrows','Ctl_Eyebrows_L','Ctl_Eyebrows_R',
'Ctl_Eye_L','Ctl_Eye_R']
#emList = ['Ctl_Mouth','Ctl_Jaw','Ctl_Corner_Lips_L','Ctl_Corner_Lips_R']
moList = ['Mouth_Closed_Chin_Raised','Kiss','Smile_Lips_Closed','Frown','Lips_Inner',
'Mouth_Closed_Contracted_Jaw','Mouth_Opened_ClosedTeeth','Smile_Lips_Opened_Expr']
ebFrwY = [-1,-1,-1,0,0]
ebFrwX = [0,1,1,0,0]
ebRaiY = [0,0,0,0.5,0.5]
ebZero = [0,0,0,0,0]
ebSadd = [1,-1,-1,0,0]
moZero = [0,0,0,0,0,0,0,0,0.3,0,0]
moKis = [0,10,0,0,0,0,0,0,0.3,0,0]
moSml = [0,0,10,0,0,0,0,0,0.3,0,0]
moHap = [0,0,0,0,0,0,0,10,0,0,0]
moSad = [0,0,0,10,0,0,0,0,0,0,0]
moLip = [0,0,0,0,7,0,0,0,0.3,0,0]
moNem = [0,0,0,0,0,5,2,0,0.3,0,0]
moMoo = [0,0,0,0,0,0,0,0,-1.5,0,0]
moSmL = [0,0,0,0,0,0,0,0,0.3,10,0]
moSmR = [0,0,0,0,0,0,0,0,0.3,0,10]
moSul = [5,0,0,0,0,0,0,0,0,0,0]
# Our mel global proc.
melproc = """
global proc portData(string $arg){
    python(("portData(\\"" + $arg + "\\")"));
}
"""
mm.eval(melproc)

mc.playbackOptions(loop='continuous')
mc.playbackOptions(minTime='0sec', maxTime='3600sec')
#for i in ebList:mc.cutKey(i,time=(0,108000))
#for i in emList: mc.cutKey(i,time=(0,108000))
#mc.cutKey(time=(0,108000))
mc.currentTime(0, edit=True)

# Our Python function that can be changed to do whatever we want:
def portData(arg):
    """
    Read the 'serial' data passed in from the commandPort
    """

    recVal = str(arg)
    
    #cases of expression
    if recVal=="eye_brow_down_nose_wrinkle": 
        for i in range(5):
            if i==0:
                keyAnim1(ebList[i],'Eyebrows_Frown', 10)
                keyAnim1(ebList[i], 'Eyebrows_Raised', 0)    
                keyAnim1('Ctl_Eye_L', 'Eyelid_Dn_Raised', 0)
                keyAnim1('Ctl_Eye_R', 'Eyelid_Dn_Raised', 0) 
            keyAnim1(ebList[i], 'translateY', ebFrwY[i])
            if i!=1: keyAnim1(ebList[i], 'translateX', ebFrwX[i])
    elif recVal=="eye_brow_down":
        for i in range(5):
            if i==0:
                keyAnim1(ebList[i], 'Eyebrows_Frown', 0)
                keyAnim1(ebList[i], 'Eyebrows_Raised', 0)  
                keyAnim1('Ctl_Eye_L', 'Eyelid_Dn_Raised', 0)
                keyAnim1('Ctl_Eye_R', 'Eyelid_Dn_Raised', 0) 
            keyAnim1(ebList[i], 'translateY', ebFrwY[i])
            if i!=1: keyAnim1(ebList[i], 'translateX', ebFrwX[i])
    elif recVal=="eye_brow_up":
        for i in range(5):
            if i==0:
                keyAnim1(ebList[i], 'Eyebrows_Frown', 0)
                keyAnim1(ebList[i], 'Eyebrows_Raised', 10)  
                keyAnim1('Ctl_Eye_L', 'Eyelid_Dn_Raised', 0)
                keyAnim1('Ctl_Eye_R', 'Eyelid_Dn_Raised', 0) 
            keyAnim1(ebList[i], 'translateY', ebRaiY[i])
            if i!=1: keyAnim1(ebList[i], 'translateX', ebZero[i])
    elif recVal=="neutral_e":
        for i in range(5):
            if i==0:
                keyAnim1(ebList[i], 'Eyebrows_Frown', 0)
                keyAnim1(ebList[i], 'Eyebrows_Raised', 0) 
                keyAnim1('Ctl_Eye_L', 'Eyelid_Dn_Raised', 0)
                keyAnim1('Ctl_Eye_R', 'Eyelid_Dn_Raised', 0) 
            keyAnim1(ebList[i], 'translateY', ebZero[i])        
            if i!=1: keyAnim1(ebList[i], 'translateX', ebZero[i])
    elif recVal=="eye_brow_happy":
        for i in range(5):
            if i==0:
                keyAnim1(ebList[i], 'Eyebrows_Frown', 0)
                keyAnim1(ebList[i], 'Eyebrows_Raised', 0) 
                keyAnim1('Ctl_Eye_L', 'Eyelid_Dn_Raised', 10)
                keyAnim1('Ctl_Eye_R', 'Eyelid_Dn_Raised', 10) 
            keyAnim1(ebList[i], 'translateY', ebZero[i])        
            if i!=1: keyAnim1(ebList[i], 'translateX', ebZero[i])
    elif recVal=="eye_brow_sad":
        for i in range(5):
            if i==0:
                keyAnim1(ebList[i], 'Eyebrows_Frown', 0)
                keyAnim1(ebList[i], 'Eyebrows_Raised', 0) 
                keyAnim1('Ctl_Eye_L', 'Eyelid_Dn_Raised', 0)
                keyAnim1('Ctl_Eye_R', 'Eyelid_Dn_Raised', 0) 
            keyAnim1(ebList[i], 'translateY', ebSadd[i])        
            if i!=1: keyAnim1(ebList[i], 'translateX', ebSadd[i])
    elif recVal=="kiss":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moKis[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moKis[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moKis[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moKis[i])
    elif recVal=="lip_corner_up_both":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moSml[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moSml[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moSml[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moSml[i])
    elif recVal=="lip_happy":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moHap[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moHap[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moHap[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moHap[i])
    elif recVal=="lip_stretch_down":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moSad[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moSad[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moSad[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moSad[i])
    elif recVal=="lip_tighten":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moLip[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moLip[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moLip[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moLip[i])
    elif recVal=="clench":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moNem[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moNem[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moNem[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moNem[i])
    elif recVal=="lip_open":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moMoo[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moMoo[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moMoo[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moMoo[i])
    elif recVal=="lip_corner_up_left":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moSmL[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moSmL[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moSmL[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moSmL[i])
    elif recVal=="lip_corner_up_right":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moSmR[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moSmR[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moSmR[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moSmR[i])
    elif recVal=="lip_sulky":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 10)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 10)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moSul[i])
            elif i==8: keyAnim2('Ctl_Jaw', 'translateY', moSul[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moSul[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moSul[i])
    elif recVal=="neutral_l":
        keyAnim2('Ctl_Puff_L', 'Cheeks_PuffedExpr', 0)
        keyAnim2('Ctl_Puff_R', 'Cheeks_PuffedExpr', 0)
        for i in range(11):
            if i<8: keyAnim2('Ctl_Mouth', moList[i], moZero[i])
            elif i==8: keyAnim2('Ctl_Jaw',  'translQateY', moZero[i])
            elif i==9: keyAnim2('Ctl_Corner_Lips_L', moList[2], moZero[i])
            else: keyAnim2('Ctl_Corner_Lips_R', moList[2], moZero[i])


# Open the commandPort.  The 'prefix' argument string is calling to the defined
# mel script above (which then calls to our Python function of the same name):
mc.commandPort(name="127.0.0.1:7777", echoOutput=False, noreturn=False,
               prefix="portData", returnNumCommands=True)
mc.commandPort(name=":7777", echoOutput=False, noreturn=False,
               prefix="portData", returnNumCommands=True)
