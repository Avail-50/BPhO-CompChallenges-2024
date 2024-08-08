using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Path : MonoBehaviour
{

    public float spin = 16.7f / 3600;
    private long earthScaleGM = 3953309000000;
    [SerializeField] private float r;

    public float startSpeed;

    public float angle;

    public Vector3 start;
    public Vector3 end;
    public Vector3 earth;

    private float verticalSpeed;
    private float horizontalSpeed;
    private float verticalAcceleration;

    void Awake()
    {
        Debug.Log(transform.position);

        start = GameObject.Find("Origin").transform.position;
        end = GameObject.Find("Destination").transform.position;
        earth = GameObject.Find("Sphere").transform.position;

        horizontalSpeed = startSpeed * Mathf.Cos(angle);
        verticalSpeed = startSpeed * Mathf.Sin(angle);
        transform.rotation = Quaternion.LookRotation(end, -earth);
        r = (transform.position - earth).magnitude;
        verticalAcceleration = -earthScaleGM / r;


    }

    // Update is called once per frame
    void FixedUpdate()
    {
        transform.rotation = Quaternion.LookRotation(end, -earth);

        transform.Translate(new Vector3(0, verticalSpeed, horizontalSpeed) * 0.02f);

        verticalSpeed += verticalAcceleration * 0.02f;
        verticalAcceleration = -earthScaleGM / r;

    }
}
