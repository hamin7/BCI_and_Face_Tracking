using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class second : MonoBehaviour {

    Vector3[] scales = new[] { new Vector3(0.03f, 0.03f, 0.03f), new Vector3(0.04f, 0.04f, 0.04f) };

    Color[] colors = new[] { new Color(0.4f, 0.4f, 0.4f), new Color(0.8f, 0.8f, 0.8f) };

    Color[] IconColors = new[] { new Color(0f, 0f, 0f), new Color(1f, 1f, 1f) };

    //2,3 번자극의 Command 아이콘은 1,4와 달리 자식 객체로 종속되어 있지 않아서 별도로 크기 변화 시켜줘야함

    Vector3[] IconScales = new Vector3[2];

    //Commands_Robot 의 turbo 명령어 아이콘 세개 이어붙이는 예외 경우 처리

    public SpriteRenderer[] turbos = new SpriteRenderer[2];
 


    int currentScale;
    public string start, end;
    float secCount;

    public SpriteRenderer[] Commands;

    SpriteRenderer Command;
    Transform GOtransform;
    SpriteRenderer GOspriterenderer;


    void Start () {
        currentScale = 0;

        start = "01";
        end = "10";

        GOtransform = gameObject.GetComponent<Transform>();
        GOspriterenderer = gameObject.GetComponent<SpriteRenderer>();
        IconScales[0] = new Vector3(0.02f, 0.02f, 1f);
    }

    private void OnEnable()
    {
        //StartCoroutine(Switching());
        StartCoroutine(revisedSwitching());
    }

    IEnumerator revisedSwitching()
    {
        if (MarkerControl.SelectedMarker == "Robot")
        {

            Command = Commands[0];
            Commands[1].color = new Color(0f, 0f, 0f, 0f);
            Commands[2].color = new Color(0f, 0f, 0f, 0f);
        }
        else if (MarkerControl.SelectedMarker == "Hum")
        {

            Command = Commands[1];
            Commands[0].color = new Color(0f, 0f, 0f, 0f);
            Commands[2].color = new Color(0f, 0f, 0f, 0f);

            turbos[0].color = new Color(0f, 0f, 0f, 0f);
            turbos[1].color = new Color(0f, 0f, 0f, 0f);
        }
        else if (MarkerControl.SelectedMarker == "Air")
        {

            Command = Commands[2];
            Commands[1].color = new Color(0f, 0f, 0f, 0f);
            Commands[0].color = new Color(0f, 0f, 0f, 0f);

            turbos[0].color = new Color(0f, 0f, 0f, 0f);
            turbos[1].color = new Color(0f, 0f, 0f, 0f);
        }

        //IconScales[0] = Command.transform.localScale;
        IconScales[1] = IconScales[0] * 1.33f;

        yield return new WaitForSeconds(6f);

        //secCount = Time.time;

        while (true)
        {
            yield return StartCoroutine(WaitFor.Frames(7));
            //gameObject.GetComponent<Transform>().localScale = scales[currentScale];
            //gameObject.GetComponent<SpriteRenderer>().color = colors[currentScale];
            GOtransform.localScale = scales[currentScale];
            GOspriterenderer.color = colors[currentScale];
            Command.color = IconColors[currentScale];
            Command.transform.localScale = IconScales[currentScale];

            //Commands_Robot 의 turbo 명령어 아이콘 세개 이어붙이는 예외 경우 처리
            if (Command.name == "turbo")
            {
                turbos[0].color = IconColors[currentScale];
                turbos[1].color = IconColors[currentScale];
            }


            currentScale += 1;
            currentScale %= 2;

            if (currentScale == 1 && first.tempTime - first.secCount > 2.5f)
            {

                yield return new WaitForSecondsRealtime(6f);

                //pause 후 시작시점에 secCount 새값 할당
                //secCount = Time.time;
            }
        }

    }
    IEnumerator Switching()
    {
        //Command 아이콘 참조는 start 에서 하면 안됨 - MarkerControl.Selected.. 정적변수 아직 null 인 시점이라서 
        if (MarkerControl.SelectedMarker == "Robot")
        {
           
            Command = Commands[0];
            Commands[1].color = new Color(0f, 0f, 0f, 0f);
            Commands[2].color = new Color(0f, 0f, 0f, 0f);
        }
        else if (MarkerControl.SelectedMarker == "Hum")
        {
            
            Command = Commands[1];
            Commands[0].color = new Color(0f, 0f, 0f, 0f);
            Commands[2].color = new Color(0f, 0f, 0f, 0f);

            turbos[0].color = new Color(0f, 0f, 0f, 0f);
            turbos[1].color = new Color(0f, 0f, 0f, 0f);
        }
        else if (MarkerControl.SelectedMarker == "Air")
        {
            
            Command = Commands[2];
            Commands[1].color = new Color(0f, 0f, 0f, 0f);
            Commands[0].color = new Color(0f, 0f, 0f, 0f);

            turbos[0].color = new Color(0f, 0f, 0f, 0f);
            turbos[1].color = new Color(0f, 0f, 0f, 0f);
        }

        IconScales[0] = Command.transform.localScale;
        IconScales[1] = IconScales[0] * 1.33f;

        yield return new WaitForSeconds(3f);

        while (true)
        {
            yield return StartCoroutine(WaitFor.Frames(7));
            //gameObject.GetComponent<Transform>().localScale = scales[currentScale];
            //gameObject.GetComponent<SpriteRenderer>().color = colors[currentScale];
            GOtransform.localScale = scales[currentScale];
            GOspriterenderer.color = colors[currentScale];
            Command.color = IconColors[currentScale];
            Command.transform.localScale = IconScales[currentScale];

            //Commands_Robot 의 turbo 명령어 아이콘 세개 이어붙이는 예외 경우 처리
            if (Command.name == "turbo")
            {
                turbos[0].color = IconColors[currentScale];
                turbos[1].color = IconColors[currentScale];
            }
            

            currentScale += 1;
            currentScale %= 2;

            if (currentScale == 1 && Time.time % 8 < 0.5)
            {

                yield return new WaitForSecondsRealtime(5f);

            }
        }
    }

    /*FRAME COUNT*/
    public static class WaitFor
    {
        public static IEnumerator Frames(int frameCount)
        {
            /*if (frameCount <= 0)
            {
                throw new ArgumentOutOfRangeException("frameCount", "Cannot wait for less that 1 frame");
            }*/

            while (frameCount > 0)
            {
                frameCount--;
                yield return null;
            }
        }
    }
}
