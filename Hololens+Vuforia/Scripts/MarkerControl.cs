using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MarkerControl : MonoBehaviour {

    //1. system OFF (reset) -어플실행시 초기상태 또는 UDP 9 들어왔을때 : 마커 Icon 비활성화. StimuliParent 비활성화 
    //2. system ON   - UDP 9 들어왔을때 토글 : 마커 Icon 활성화. 
    //3. onSelect - Boundingbox 에서 게이즈 3초 판별 시점 : 마커 Icon 비활성화. StimuliParent 활성화
    //4. return- 기기 명령어 4번에 해당하는 UDP 값 들어왔을때 : 마커 Icon 활성화. StimuliParent 비활성화 

    public static GameObject GazeCursor;

    public static GameObject[] Markers; //세개의 마커 

    public static string SelectedMarker = null; //Boundingbox에서 select처리된 마커의 이름

    public static GameObject stimuliParent; //자극들의 root 부모 

    public static bool isSystemOn; // ForTest_UDPresponder로 참조. 9 들어 왔을때  On(마커활성화)/Off(마커비활성화 및 초기화면)

    public static bool onSelect; //BoundBox(게이즈 응시 시간(프레임)카운트하여 select 판별)로 참조 -> UDPGeneration(참일때 UDP값 PC로 전송)

    void Start () {

        GazeCursor = GameObject.FindGameObjectWithTag("Respawn");

        Markers = GameObject.FindGameObjectsWithTag("Player");

        //마커 자체 비활성화/활성화 문제 있는듯. 대신에 boundingbox 컴포넌트가 포함된 Icon 참조
        for(int i = 0; i < 3; i++)
        {
            Markers[i] = Markers[i].transform.Find("Icon").gameObject;
        }

        //자극 객체 참조
        stimuliParent = GameObject.Find("StimuliParent");

        
        //자극 네개의 부모객체를 비활성화
        //에디터에서 활성화 되어 있는 자극은 root 부모로 활성화/비활성화 일괄로 할 수 있는듯- FPStext빼고 다 root 부모 따라서 활성화/비활성화됨
        stimuliParent.SetActive(false);


        //onSelect 기본 거짓값. 
        onSelect = false;
    

        //눈깜빡임 신호값 들어오기 전까지 기본 SystamOff 세팅
        SystemOFF();
        isSystemOn = false;


        //유니티 에디터 작업할 경우에는 UDP로 눈깜빡임 신호값 받아올수 없으므로 기본 SystemOn 세팅
#if UNITY_EDITOR
        SystemON();
        isSystemOn = true;
#endif

    }


    //UDP 9 들어올 때 ForTest_UDPresponder에서 호출되는 system 토글 
    public static void SystemON()
    {
        ActivateMarker(true);
        GazeCursor.SetActive(true);
    }
    public static void SystemOFF()
    {
        ActivateMarker(false);
        stimuliParent.SetActive(false);
        GazeCursor.SetActive(false);
    }

    //마커, 자극 활성화 컨트롤
    //Boundingbox와 ForText_UDPresponder에서 참조
    public static void ActivateMarker(bool activate)
    {
        foreach (GameObject marker in Markers)
        {
            marker.SetActive(activate);
        }
    }

    //자극 네개의 부모객체 활성화 컨트롤
    public static void ActivateStimuli(bool activate)
    {

        stimuliParent.SetActive(activate);

    }


}
