using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Projectile : MonoBehaviour
{
    public Button go;
    public Transform start;
    public Transform end;

    public bool going = false;

    public float spin = 16.7f/3600;
    private long earthScaleGM = 3953309000000;
    [SerializeField] private float r;

    public GameObject newProjectile;


    void Awake()
    {
        go.onClick.AddListener(NoParameterOnClick);
    }

    // Update is called once per frame
    void Update()
    {
        if (going == true)
        {
            // creates new projectile object
            GameObject Missile = Instantiate(newProjectile, start.position, transform.rotation);
            LiftOff();
        }
    }

    void NoParameterOnClick()
    {
        going = true;
    }

    void LiftOff()
    {
        Debug.Log("lift off");
        going = false;
    }
}
