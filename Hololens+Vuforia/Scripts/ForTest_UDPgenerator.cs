using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ForTest_UDPgenerator : MonoBehaviour {

    public GameObject UDPCommGameObject;

    public string DataString = "UDP is real.";


    public firstStar firstSphere;

    void Start()
    {
        if (UDPCommGameObject == null)
        {
            Debug.Log("ERR UDPGEN: UDPSender is required. Self-destructing.");
            Destroy(this);
        }
    }


    void Update()
    {

        if (firstSphere.checker_1 == 0 && firstSphere.checker_2 == 1)
        {
            DataString = firstSphere.start;
            Debug.Log("Starting Point: " + firstSphere.start + "\nDataString: " + DataString);

            if (DataString != null)
            {
                // UTF-8 is real
                var dataBytes = System.Text.Encoding.UTF8.GetBytes(DataString);
                UDPCommunication comm = UDPCommGameObject.GetComponent<UDPCommunication>();

                // #if is required because SendUDPMessage() is async
#if !UNITY_EDITOR
			comm.SendUDPMessage(comm.externalIP, comm.externalPort, dataBytes);
#endif
            }
        }


        if (firstSphere.checker_1 == 1 && firstSphere.checker_2 == 0)
        {
            DataString = firstSphere.end;
            Debug.Log("Ending Point: " + firstSphere.end + "\nDataString: " + DataString);

            if (DataString != null)
            {
                // UTF-8 is real
                var dataBytes = System.Text.Encoding.UTF8.GetBytes(DataString);
                UDPCommunication comm = UDPCommGameObject.GetComponent<UDPCommunication>();

                // #if is required because SendUDPMessage() is async
#if !UNITY_EDITOR
			comm.SendUDPMessage(comm.externalIP, comm.externalPort, dataBytes);
#endif
            }
        }


        /* ORIGINAL
         * 
         * if (DataString != null) {
			// UTF-8 is real
			var dataBytes = System.Text.Encoding.UTF8.GetBytes(DataString);
			UDPCommunication comm = UDPCommGameObject.GetComponent<UDPCommunication> ();

			// #if is required because SendUDPMessage() is async
			#if !UNITY_EDITOR
			comm.SendUDPMessage(comm.externalIP, comm.externalPort, dataBytes);
			#endif
		}*/

    }
}
