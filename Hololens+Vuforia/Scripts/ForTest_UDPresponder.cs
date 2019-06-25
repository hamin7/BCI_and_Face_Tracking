using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ForTest_UDPresponder : MonoBehaviour {

    /// <summary>
    /// PC로부터 오는 UDP값에 따라 어플 전체를 총괄해야하는 스크립트. 
    /// 싱글톤역할 ..!
    /// 
    /// </summary>

    public TextMesh TextFromUDP = null;


    //ORIGNAL SAMPLE CODE - show UDP value in 3D text//
    public void ResponseToUDPPacket(string fromIP, string fromPort, byte[] data)
    {
        string dataString = System.Text.Encoding.UTF8.GetString(data);

        if (TextFromUDP != null)
        {
            TextFromUDP.text = dataString;

        }

    }

    //-----------------------------CUSTOM FUNCTION---------------------------------//


    public void ProcessManage(string fromIP, string fromPort, byte[] data)
    {
        string dataString = System.Text.Encoding.UTF8.GetString(data);

        Debug.Log("UDP value " + dataString + "received in ProcessManage()");

        //ShowDataInText(dataString);


        //if (dataString == '9'.ToString())
        if (dataString == "MiddleWare#HanYang#TurnSignal")
        {
            MarkerControl.isSystemOn = !MarkerControl.isSystemOn;
            ShowDataInText(MarkerControl.isSystemOn.ToString());

            if (MarkerControl.isSystemOn == true)
            {
                MarkerControl.SystemON();
            } else if (MarkerControl.isSystemOn == false)
            {
                MarkerControl.SystemOFF();
            }
        }

        //if (dataString == '4'.ToString())
        if (dataString == "MiddleWare#HanYang#RVC#Home" || dataString == "MiddleWare#HanYang#AirCleaner#Home")
        {
            /*MarkerControl.ActivateMarker(true);// 이게 왜 실행이 안되는지가 문제
            MarkerControl.ActivateStimuli(false);*/

            //SystemON, OFF는 잘되니까 이렇게 처리하자
            MarkerControl.SystemOFF();
            MarkerControl.SystemON();
        }

    }  


 
    
    //UDP 값 잘 들어왔는지 확인하기 위한 3D 텍스트
    public void ShowDataInText(string dataString)
    {
        
        if (TextFromUDP != null)
            {
            TextFromUDP.text = dataString;

            if(dataString == "true")
                TextFromUDP.color = new Color(255f, 0f, 0f);
            else if(dataString == "false")
                TextFromUDP.color = new Color(0f, 0f, 255f);
        }
    }


    

}
