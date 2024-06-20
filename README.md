<h1># Corrosion Detection System:</h1>

- <h3>Central Control Unit: The system uses a Raspberry Pi 4 as the main control unit.</h3>
- <h3>Camera Module: Equipped with a Raspberry Pi Camera Module for live video streaming and capturing footage of target areas.</h3>
- <h3>Servo Motors: Includes two servo motors (SG90 and MG996R) for precise camera movement, allowing 180-degree horizontal and vertical panning.</h3>
- <h3>Motor Driver Unit: Controls the propulsion of the ROV and the movement of the camera.</h3>
- <h3>Algorithm Execution: Raspberry Pi runs a morphological algorithm using Python and OpenCV libraries to analyze live video feeds for signs of corrosion.</h3>
- <h3>Detection Criteria: The algorithm identifies corrosion based on discoloration and texture irregularities.</h3>
- <h3>Real-time Feedback: Detected corrosion instances are displayed immediately on a screen.</h3>
- <h3>Remote Access: Remote monitoring and control are possible through the RealVNC Viewer application, allowing operators to adjust the camera orientation and view the live feed.</h3>
- <h3>Power Supply: Uses LM2596 DC-DC step-down power supply modules to convert a 12V DC input to a 5V DC output, ensuring stable power for the Raspberry Pi and servo motors.</h3>
- <h3>Safety Features: LM2596 modules offer overcurrent protection, thermal shutdown, and reverse polarity protection.</h3>
- <h3>Compact Setup: All components are integrated into the ROV chassis for a streamlined and efficient configuration.</h3>
- <h3>Image Processing: Converts RGB images to HSV color space to effectively identify corrosion.</h3>
- <h3>Color Range Definition: Sets specific HSV color ranges to detect corrosion areas accurately.</h3>
- <h3>Binary Mask Creation: Generates a binary mask to highlight corroded regions in white.</h3>
- <h3>Contour Detection: Uses contour detection algorithms to visualize and delineate corroded areas, aiding in proactive maintenance.</h3>

<h1># System and sample output:</h1>

![Tank Dimension](https://github.com/prahulk46a/CoroVision/assets/98529455/b751c1c5-4d2e-4312-a011-fe4e6277b10e)
<h2>Above is the complex structure of Tanks in Merchant ships.</h2>



![Circuit Diagram](https://github.com/prahulk46a/CoroVision/assets/98529455/67358d89-1896-4c55-8005-88590beea93f)
<h2>Circuit Diagram of our system</h2>



![System](https://github.com/prahulk46a/CoroVision/assets/98529455/f465f292-5c1d-48c1-9df9-24f4d0261c0c)
<h2>This is our Entire system for detection of corrosion.</h2>



![LiveStream](https://github.com/prahulk46a/CoroVision/assets/98529455/0ac8e7bc-12ee-4274-a721-998c1f289e1b)



![Corrodetection](https://github.com/prahulk46a/CoroVision/assets/98529455/ec701eb5-be63-4f62-bb43-879d2cce3e45)
<h2>Live Corrosion detection.</h2>
