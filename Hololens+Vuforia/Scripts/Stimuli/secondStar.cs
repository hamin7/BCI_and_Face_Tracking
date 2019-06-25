using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class secondStar : MonoBehaviour {
    public GameObject star;
    public GameObject icon;
    private bool tf;

    int currentScale = 0;
    Vector3[] scales = new[] { new Vector3(0.18f, 0.18f, 0.18f), new Vector3(0.25f, 0.25f, 0.25f) };
    Color[] colors = new[] { new Color(0.4f, 0.4f, 0.4f), new Color(0.8f, 0.8f, 0.8f) };

    public firstStar firstStar;


    // Use this for initialization
    void Start () {
        //IEnumerator
        StartCoroutine(Switching());
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

    IEnumerator Switching()
    {
        while (firstStar.trial < 21)
        {
            if (currentScale == 0)
            {
                if (Time.time % 6 < 0.5)
                {
                    yield return new WaitForSecondsRealtime(2f);
                }
                //*yield return StartCoroutine(WaitFor.Frames(3));
                
            }
            //*else
                //*yield return StartCoroutine(WaitFor.Frames(4));
            yield return StartCoroutine(WaitFor.Frames(7));
            currentScale++;
            currentScale %= 2;
            tf = !tf;
            //icon.gameObject.SetActive(tf);
            star.GetComponent<Transform>().localScale = scales[currentScale];
            star.GetComponent<SpriteRenderer>().color = colors[currentScale];


        }
    }
   
}
