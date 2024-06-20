**Corrosion Detection System:**
- Central Control Unit: The system uses a Raspberry Pi 4 as the main control unit.
  
- Camera Module: Equipped with a Raspberry Pi Camera Module for live video streaming and capturing footage of target areas.
- Servo Motors: Includes two servo motors (SG90 and MG996R) for precise camera movement, allowing 180-degree horizontal and vertical panning.
- Motor Driver Unit: Controls the propulsion of the ROV and the movement of the camera.
- Algorithm Execution: Raspberry Pi runs a morphological algorithm using Python and OpenCV libraries to analyze live video feeds for signs of corrosion.
- Detection Criteria: The algorithm identifies corrosion based on discoloration and texture irregularities.
- Real-time Feedback: Detected corrosion instances are displayed immediately on a screen.
- Remote Access: Remote monitoring and control are possible through the RealVNC Viewer application, allowing operators to adjust the camera orientation and view the live feed.
- Power Supply: Uses LM2596 DC-DC step-down power supply modules to convert a 12V DC input to a 5V DC output, ensuring stable power for the Raspberry Pi and servo motors.
- Safety Features: LM2596 modules offer overcurrent protection, thermal shutdown, and reverse polarity protection.
- Compact Setup: All components are integrated into the ROV chassis for a streamlined and efficient configuration.
- Image Processing: Converts RGB images to HSV color space to effectively identify corrosion.
- Color Range Definition: Sets specific HSV color ranges to detect corrosion areas accurately.
- Binary Mask Creation: Generates a binary mask to highlight corroded regions in white.
- Contour Detection: Uses contour detection algorithms to visualize and delineate corroded areas, aiding in proactive maintenance.

**System and sample output:**

![Tank Dimension](https://github.com/prahulk46a/CoroVision/assets/98529455/b751c1c5-4d2e-4312-a011-fe4e6277b10e)


This are the complex Ship Structures.

![Circuit Diagram](https://github.com/prahulk46a/CoroVision/assets/98529455/67358d89-1896-4c55-8005-88590beea93f)


This is Circuit Diagram of our system

![System](https://github.com/prahulk46a/CoroVision/assets/98529455/f465f292-5c1d-48c1-9df9-24f4d0261c0c)


This is our Entire system for detection of corrosion.

![LiveStream](https://github.com/prahulk46a/CoroVision/assets/98529455/0ac8e7bc-12ee-4274-a721-998c1f289e1b)



![Corrodetection](https://github.com/prahulk46a/CoroVision/assets/98529455/ec701eb5-be63-4f62-bb43-879d2cce3e45)



Live Corrosion detection.
