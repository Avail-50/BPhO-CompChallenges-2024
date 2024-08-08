using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Projectile : MonoBehaviour
{
    public Button go;
    public Transform start;
    public Transform end;

    [SerializeField] private bool nowGo = false;
    [SerializeField] private bool going = false;

    public GameObject newProjectile;


    void Awake()
    {
        go.onClick.AddListener(NoParameterOnClick);
    }

    // Update is called once per frame
    void Update()
    {
        if (nowGo == true)
        {
            going = true;
            // creates new projectile object
            GameObject Missile = Instantiate(newProjectile, start.position, transform.rotation);
            nowGo = false;
        }
    }

    void NoParameterOnClick()
    {
        if (!going)
            nowGo = true;
    }

}
