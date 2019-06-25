using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class firstStar : MonoBehaviour {


    public GameObject star;
    public GameObject icon;
    private bool tf;

    Vector3[] scales = new[] { new Vector3(0.18f, 0.18f, 0.18f), new Vector3(0.25f, 0.25f, 0.25f) };

    Color[] colors = new[] { new Color(0.4f, 0.4f, 0.4f), new Color(0.8f, 0.8f, 0.8f) };

    public int checker_1, checker_2; //(0,1) == 끝났다가 재시작하는 시점, (1,0) == 시작한 것이 끝나는 시점, (1,1) ==  trial 진행되는 중, (0,0) == 3초간의 pause
    float temp1, temp2;
    int currentScale = 0;
    public string start, end;
    public TextMesh tm = null;

    public int trial = 0;

    string[] numbers = { "1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4", " " };

    // Use this for initialization
    void Start () {


        


        //배열 순서 뒤섞기
        shuffle(numbers);

        //IEnumerator
        StartCoroutine(switching());

        //Scale 값
        //Debug.Log( scales[0].ToString() +  scales[1].ToString());
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

    void shuffle(string[] numbers)
    {
        for (int t = 0; t < numbers.Length - 1; t++)
        {
            string tmp = numbers[t];
            int r = Random.Range(t, numbers.Length - 1);

            numbers[t] = numbers[r];
            numbers[r] = tmp;
        }
    }

    IEnumerator switching()
    {

        while (trial < 21)
        {
            //Debug.Log(Time.time);
        
            {
                temp2 = Time.time;
            }

            //yield return new WaitForSecondsRealtime(0.049f);//빠른버전

            //*yield return StartCoroutine(WaitFor.Frames(4));
            yield return StartCoroutine(WaitFor.Frames(8));

            star.GetComponent<Transform>().localScale = scales[currentScale];
            star.GetComponent<SpriteRenderer>().color = colors[currentScale];

            tf = !tf;
            //icon.gameObject.SetActive(!tf);
            currentScale += 1;
            currentScale %= 2;

            if (currentScale == 0)
            {
                temp1 = Time.time;
         
                //Debug.Log(temp1 - temp2);
            }

            if (currentScale == 1 && Time.time % 6 < 0.5) //8의 배수마다, 즉 8초마다 pause
            {
                //ENDING POINT
                checker_1 = 1;
                checker_2 = 0;

                yield return new WaitForSeconds(0.01f);

                //1~4 랜덤 숫자 제시
                tm.text = numbers[trial];

                //trial 횟수
                trial++;

                //선택된 랜덤 숫자에 따라 start, end 값 다르게
                if (tm.text == "1")
                {
                    start = "a";
                    end = "e";
                }
                else if (tm.text == "2")
                {
                    start = "b";
                    end = "f";
                }
                else if (tm.text == "3")
                {
                    start = "c";
                    end = "g";
                }
                else if (tm.text == "4")
                {
                    start = "d";
                    end = "h";
                }


                //3초간 pause
                checker_1 = 0;
                checker_2 = 0;

                
                yield return new WaitForSecondsRealtime(2f);

                //STARTING POINT    
                checker_1 = 0;
                checker_2 = 1;

                yield return new WaitForSeconds(0.01f); //0.01초 delay해주어야만 Update()의 한 프레임에서 캐치함


                checker_1 = 1;
                checker_2 = 1;

            }

        }

    }
}
