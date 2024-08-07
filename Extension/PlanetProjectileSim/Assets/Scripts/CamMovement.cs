using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CamMovement : MonoBehaviour
{
    public Transform target; //the camera's target, the player
    public float rotateSpeed;
    private float distance; //distance away from player
    //private Vector3 velocity = Vector3.zero; //used in SmoothDamp function
    //public float mouseSpeed;
    public float scrollSpeed;
    //private float preferedDistance;

    Camera cam;
    public LayerMask mask;

    public GameObject markerStart;
    public GameObject markerEnd;
    public Toggle checkboxStart;
    public Toggle checkboxEnd;

    // Start is called before the first frame update
    void Start()
    {
        distance = 170f;
        cam = Camera.main;
    }


    // Update is called once per frame
    void Update()
    {
        //gets movement of mouse (stores from 1 to -1), multiplies by mouseSpeed and rotates the camera by the amount

        if (Input.GetMouseButton(1)) //right mouse down
        {
            float v = rotateSpeed * -Input.GetAxis("Mouse Y");
            float h = rotateSpeed * Input.GetAxis("Mouse X");

            transform.RotateAround(target.transform.position, transform.right, v * Time.deltaTime);
            transform.RotateAround(target.transform.position, Vector3.up, h * Time.deltaTime);
            
        }

        // user can change prefered distance of camera from player
        if (Input.GetAxis("Mouse ScrollWheel") != 0)
        {

            float distanceChange = Input.GetAxis("Mouse ScrollWheel");
            if ((distance - distanceChange * scrollSpeed) > 27)
                distance -= distanceChange * scrollSpeed;

        }

        if (Input.GetMouseButtonDown(0)) //left mouse click
        {
            // Draw Ray
            //Vector3 mousePos = Input.mousePosition;
            //mousePos.z = distance;


            //mousePos = cam.ScreenToWorldPoint(mousePos);
            //Debug.DrawRay(transform.position, mousePos - transform.position, Color.blue);
            //Debug.Log("ray");

            Ray ray = cam.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit, distance, mask))
            {
                Debug.Log("rayHit" + hit.transform.name);
                //hit.transform.GetComponent<Renderer>().material.color = Color.red;

                if (checkboxEnd.isOn)
                    markerEnd.transform.position = hit.point;
                else if (checkboxStart.isOn)
                    markerStart.transform.position = hit.point;
            }


        }

        Vector3 player = target.position + (transform.position - target.position).normalized * distance;
        transform.position = player;

        transform.LookAt(target);
    }
}

