<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Voice + Gesture PC Assistant</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #f5f7fa;
            color: #1f2937;
            line-height: 1.6;
        }

        header {
            background: #111827;
            color: white;
            padding: 50px 20px;
            text-align: center;
        }

        header h1 {
            margin: 0 0 10px;
            font-size: 42px;
        }

        header p {
            margin: 0;
            font-size: 18px;
            color: #d1d5db;
        }

        .container {
            max-width: 1100px;
            margin: 40px auto;
            padding: 0 20px;
        }

        section {
            background: white;
            margin-bottom: 25px;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
        }

        h2 {
            margin-top: 0;
            color: #111827;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
        }

        h3 {
            color: #374151;
            margin-top: 25px;
        }

        code {
            background: #f1f5f9;
            padding: 3px 6px;
            border-radius: 4px;
            font-family: Consolas, monospace;
        }

        pre {
            background: #111827;
            color: #e5e7eb;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: Consolas, "Courier New", monospace;
            font-size: 14px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        th,
        td {
            padding: 12px;
            border: 1px solid #d1d5db;
            text-align: left;
        }

        th {
            background: #f3f4f6;
        }

        ul,
        ol {
            padding-left: 25px;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 15px;
        }

        .feature {
            padding: 20px;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            background: #f9fafb;
        }

        .feature h3 {
            margin-top: 0;
        }

        .command {
            background: #f9fafb;
            border-left: 4px solid #2563eb;
            padding: 15px;
            margin: 15px 0;
        }

        .warning {
            background: #fff7ed;
            border-left: 4px solid #f97316;
            padding: 15px;
            margin: 15px 0;
        }

        .success {
            background: #f0fdf4;
            border-left: 4px solid #22c55e;
            padding: 15px;
            margin: 15px 0;
        }

        footer {
            background: #111827;
            color: #d1d5db;
            text-align: center;
            padding: 30px 20px;
            margin-top: 40px;
        }

        .badge {
            display: inline-block;
            background: #e5e7eb;
            color: #374151;
            padding: 5px 10px;
            margin: 4px;
            border-radius: 20px;
            font-size: 13px;
        }

        @media (max-width: 700px) {
            header h1 {
                font-size: 30px;
            }

            section {
                padding: 20px;
            }

            pre {
                font-size: 12px;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>Voice + Gesture PC Assistant</h1>
    <p>
        A Python-based multimodal contactless Windows PC controller
    </p>
</header>

<div class="container">

    <!-- FEATURES -->
    <section>
        <h2>Features</h2>

        <div class="feature-grid">

            <div class="feature">
                <h3>🎤 Voice Control</h3>
                <p>
                    Control your Windows PC using natural voice commands.
                </p>
            </div>

            <div class="feature">
                <h3>🖐️ Gesture Control</h3>
                <p>
                    Control volume and media using hand gestures.
                </p>
            </div>

            <div class="feature">
                <h3>🔊 Volume Control</h3>
                <p>
                    Increase, decrease, mute, unmute and set volume percentage.
                </p>
            </div>

            <div class="feature">
                <h3>📸 Screenshot</h3>
                <p>
                    Capture screenshots using a voice command.
                </p>
            </div>

            <div class="feature">
                <h3>🎵 Media Control</h3>
                <p>
                    Control play/pause, next and previous tracks.
                </p>
            </div>

            <div class="feature">
                <h3>🖥️ Application Control</h3>
                <p>
                    Open applications such as Chrome, Notepad and Calculator.
                </p>
            </div>

        </div>
    </section>

    <!-- GESTURE TABLE -->
    <section>
        <h2>Gesture Controls</h2>

        <table>
            <thead>
                <tr>
                    <th>Gesture</th>
                    <th>Action</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <td>👍 Thumb Up</td>
                    <td>Increase Volume</td>
                </tr>

                <tr>
                    <td>👎 Thumb Down</td>
                    <td>Decrease Volume</td>
                </tr>

                <tr>
                    <td>✊ Fist</td>
                    <td>Mute Audio</td>
                </tr>

                <tr>
                    <td>✌️ Two Fingers</td>
                    <td>Play / Pause</td>
                </tr>
            </tbody>
        </table>
    </section>

    <!-- ARCHITECTURE -->
    <section>
        <h2>System Architecture</h2>

<pre>
                              USER
                               |
                +--------------+--------------+
                |                             |
                v                             v
           MICROPHONE                      WEBCAM
                |                             |
                v                             v
       Speech Recognition                OpenCV
                |                             |
                v                             v
         Voice Command                 MediaPipe
                |                             |
                |                             v
                |                      Hand Landmarks
                |                             |
                |                             v
                |                    Gesture Detection
                |                             |
                +-------------+---------------+
                              |
                              v
                       COMMAND ENGINE
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
          Windows           Media          Browser
          Control           Control        Control
              |               |               |
              +---------------+---------------+
                              |
                              v
                         PC ACTION
</pre>
    </section>

    <!-- TECHNOLOGIES -->
    <section>
        <h2>Technologies Used</h2>

        <span class="badge">Python</span>
        <span class="badge">OpenCV</span>
        <span class="badge">MediaPipe</span>
        <span class="badge">SpeechRecognition</span>
        <span class="badge">PyAudio</span>
        <span class="badge">PyCaw</span>
        <span class="badge">Comtypes</span>
        <span class="badge">PyAutoGUI</span>
        <span class="badge">Pyttsx3</span>

        <h3>Python</h3>
        <p>
            Main programming language used for the application.
        </p>

        <h3>OpenCV</h3>
        <ul>
            <li>Webcam capture</li>
            <li>Video processing</li>
            <li>Image processing</li>
            <li>User interface rendering</li>
        </ul>

        <h3>MediaPipe</h3>
        <ul>
            <li>Hand detection</li>
            <li>Hand landmark detection</li>
            <li>Finger tracking</li>
            <li>Gesture recognition</li>
        </ul>

        <h3>SpeechRecognition</h3>
        <p>
            Converts spoken commands into text.
        </p>

        <h3>PyAudio</h3>
        <p>
            Captures audio from the microphone.
        </p>

        <h3>PyCaw</h3>
        <p>
            Controls the Windows system audio volume.
        </p>

        <h3>Comtypes</h3>
        <p>
            Provides the Windows COM interface required by PyCaw.
        </p>

        <h3>PyAutoGUI</h3>
        <p>
            Used for screenshot capture and desktop interaction.
        </p>

        <h3>Pyttsx3</h3>
        <p>
            Provides text-to-speech feedback.
        </p>
    </section>

    <!-- REQUIREMENTS -->
    <section>
        <h2>Requirements</h2>

        <h3>Hardware</h3>

        <ul>
            <li>Windows PC or Laptop</li>
            <li>Webcam</li>
            <li>Microphone</li>
            <li>Speakers or Headphones</li>
        </ul>

        <h3>Software</h3>

        <ul>
            <li>Windows 10 or Windows 11</li>
            <li>Python 3.12</li>
            <li>Internet connection for the current speech recognition implementation</li>
        </ul>
    </section>

    <!-- DEPENDENCIES -->
    <section>
        <h2>Python Dependencies</h2>

<pre>
numpy==1.26.4
opencv-python==4.11.0.86
mediapipe==0.10.21
pycaw
comtypes
SpeechRecognition
PyAudio
pyautogui
pyttsx3
</pre>
    </section>

    <!-- PROJECT STRUCTURE -->
    <section>
        <h2>Project Structure</h2>

<pre>
voice_gesture_assistant/
│
├── assistant.py
├── requirements.txt
├── README.md
└── screenshots/
</pre>

        <p>
            The <code>screenshots</code> directory is automatically created
            when a screenshot is captured.
        </p>
    </section>

    <!-- INSTALLATION -->
    <section>
        <h2>Installation</h2>

        <h3>1. Clone the Repository</h3>

<pre>
git clone &lt;repository-url&gt;
cd voice_gesture_assistant
</pre>

        <h3>2. Create a Python Environment</h3>

        <h4>Using Conda</h4>

<pre>
conda create -n voice_gesture python=3.12 -y
conda activate voice_gesture
</pre>

        <h4>Using Python Virtual Environment</h4>

<pre>
python -m venv venv
venv\Scripts\activate
</pre>

        <h3>3. Install Dependencies</h3>

<pre>
python -m pip install -r requirements.txt
</pre>

        <h3>4. Verify Python</h3>

<pre>
python --version
</pre>

        <p>Expected:</p>

<pre>
Python 3.12.x
</pre>
    </section>

    <!-- NUMPY -->
    <section>
        <h2>NumPy Compatibility</h2>

        <div class="warning">
            This project uses NumPy 1.26.4 for compatibility with the
            selected MediaPipe/OpenCV environment.
        </div>

        <p>
            Check the installed version:
        </p>

<pre>
python -c "import numpy; print(numpy.__version__)"
</pre>

        <p>Expected:</p>

<pre>
1.26.4
</pre>

        <p>
            If NumPy was upgraded to version 2.x, restore the compatible version:
        </p>

<pre>
python -m pip install --force-reinstall --no-deps numpy==1.26.4
</pre>
    </section>

    <!-- MEDIAPIPE -->
    <section>
        <h2>MediaPipe Compatibility</h2>

<pre>
python -c "import mediapipe as mp; print(mp.__version__); print(hasattr(mp, 'solutions'))"
</pre>

        <p>Expected:</p>

<pre>
0.10.21
True
</pre>

        <p>
            If MediaPipe produces a
            <code>module 'mediapipe' has no attribute 'solutions'</code>
            error:
        </p>

<pre>
python -m pip uninstall mediapipe -y
python -m pip install mediapipe==0.10.21
</pre>
    </section>

    <!-- OPENCV -->
    <section>
        <h2>OpenCV Verification</h2>

<pre>
python -c "import cv2; print(cv2.__version__)"
</pre>

        <p>Expected:</p>

<pre>
4.11.0
</pre>
    </section>

    <!-- PYCAW -->
    <section>
        <h2>PyCaw Verification</h2>

<pre>
python -c "from pycaw.pycaw import AudioUtilities; print('PyCaw OK')"
</pre>

        <p>Expected:</p>

<pre>
PyCaw OK
</pre>

        <p>
            The current implementation uses:
        </p>

<pre>
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume
</pre>

        <p>
            Avoid older implementations using:
        </p>

<pre>
devices.Activate(...)
</pre>
    </section>

    <!-- RUN -->
    <section>
        <h2>Running the Application</h2>

<pre>
python assistant.py
</pre>

        <p>
            The application will:
        </p>

        <ol>
            <li>Start the webcam.</li>
            <li>Initialize MediaPipe.</li>
            <li>Initialize the microphone.</li>
            <li>Calibrate the microphone.</li>
            <li>Start listening for voice commands.</li>
            <li>Detect hand gestures.</li>
            <li>Display the detected gesture.</li>
            <li>Display voice commands.</li>
            <li>Execute the requested PC action.</li>
        </ol>
    </section>

    <!-- VOICE COMMANDS -->
    <section>
        <h2>Voice Commands</h2>

        <div class="command">
            <strong>Open YouTube</strong>
            <pre>Open YouTube</pre>
        </div>

        <div class="command">
            <strong>Open Google</strong>
            <pre>Open Google</pre>
        </div>

        <div class="command">
            <strong>Open Chrome</strong>
            <pre>Open Chrome</pre>
        </div>

        <div class="command">
            <strong>Open Notepad</strong>
            <pre>Open Notepad</pre>
        </div>

        <div class="command">
            <strong>Open Calculator</strong>
            <pre>Open Calculator</pre>
        </div>

        <div class="command">
            <strong>Increase Volume</strong>
            <pre>Volume up</pre>
        </div>

        <div class="command">
            <strong>Decrease Volume</strong>
            <pre>Volume down</pre>
        </div>

        <div class="command">
            <strong>Set Volume</strong>
            <pre>Volume 50</pre>
        </div>

        <div class="command">
            <strong>Mute</strong>
            <pre>Mute</pre>
        </div>

        <div class="command">
            <strong>Unmute</strong>
            <pre>Unmute</pre>
        </div>

        <div class="command">
            <strong>Screenshot</strong>
            <pre>Take screenshot</pre>
        </div>

        <div class="command">
            <strong>Play / Pause</strong>
            <pre>Play</pre>
            <pre>Pause</pre>
        </div>

        <div class="command">
            <strong>Next Track</strong>
            <pre>Next track</pre>
        </div>

        <div class="command">
            <strong>Previous Track</strong>
            <pre>Previous track</pre>
        </div>

        <div class="command">
            <strong>Exit</strong>
            <pre>Close assistant</pre>
        </div>
    </section>

    <!-- VOLUME -->
    <section>
        <h2>Volume Control</h2>

        <h3>Increase Volume</h3>

<pre>
Volume up
</pre>

        <p>
            The system volume increases by 5%.
        </p>

        <h3>Decrease Volume</h3>

<pre>
Volume down
</pre>

        <p>
            The system volume decreases by 5%.
        </p>

        <h3>Set Volume</h3>

<pre>
Volume 50
Volume 75
Volume 100
</pre>

        <p>
            Valid range: <strong>0% - 100%</strong>
        </p>
    </section>

    <!-- SCREENSHOT -->
    <section>
        <h2>Screenshot</h2>

        <p>Say:</p>

<pre>
Take screenshot
</pre>

        <p>
            Screenshots are stored in:
        </p>

<pre>
screenshots/
</pre>

        <p>Example:</p>

<pre>
screenshots/
├── screenshot_20260809_091530.png
├── screenshot_20260809_092010.png
└── screenshot_20260809_092530.png
</pre>
    </section>

    <!-- CAMERA -->
    <section>
        <h2>Camera Configuration</h2>

        <p>
            The default camera index is:
        </p>

<pre>
CAMERA_INDEX = 0
</pre>

        <p>
            If the camera does not work, try:
        </p>

<pre>
CAMERA_INDEX = 1
</pre>

        <p>or:</p>

<pre>
CAMERA_INDEX = 2
</pre>
    </section>

    <!-- CAMERA TEST -->
    <section>
        <h2>Camera Troubleshooting</h2>

        <ol>
            <li>Check that the webcam is connected.</li>
            <li>Close applications currently using the webcam.</li>
            <li>Check Windows camera permissions.</li>
            <li>Try another camera index.</li>
            <li>Restart the application.</li>
        </ol>

        <h3>Camera Test Script</h3>

<pre>
import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) &amp; 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
</pre>
    </section>

    <!-- MICROPHONE -->
    <section>
        <h2>Microphone Troubleshooting</h2>

        <ul>
            <li>Check that the microphone is connected.</li>
            <li>Check Windows microphone permissions.</li>
            <li>Make sure the correct microphone is selected.</li>
            <li>Close applications that may be using the microphone.</li>
            <li>Restart the application.</li>
        </ul>

        <h3>Microphone Calibration</h3>

        <p>
            The application performs ambient-noise calibration when it starts.
        </p>

        <p>
            During calibration:
        </p>

        <ul>
            <li>Do not speak.</li>
            <li>Keep the environment reasonably quiet.</li>
            <li>Avoid loud background noise.</li>
        </ul>
    </section>

    <!-- INTERNET -->
    <section>
        <h2>Internet Requirement</h2>

        <p>
            The current version uses Google's speech recognition service
            through the <code>SpeechRecognition</code> library.
        </p>

        <div class="warning">
            An internet connection is required for voice recognition.
        </div>

<pre>
Microphone
    |
    v
Speech Recognition
    |
    v
Internet
    |
    v
Recognized Command
</pre>

        <p>
            Gesture recognition works locally and does not require an internet connection.
        </p>
    </section>

    <!-- OFFLINE -->
    <section>
        <h2>Offline Voice Recognition</h2>

        <p>
            For a completely offline implementation, the speech recognition
            component can be replaced with a local speech-to-text engine.
        </p>

        <ul>
            <li>Vosk</li>
            <li>Whisper</li>
            <li>Faster-Whisper</li>
            <li>Other local speech recognition models</li>
        </ul>

<pre>
Microphone
    |
    v
Local Speech Model
    |
    v
Text Command
    |
    v
Command Engine
    |
    v
PC Action
</pre>
    </section>

    <!-- PERFORMANCE -->
    <section>
        <h2>Performance</h2>

        <p>
            Voice recognition and gesture recognition operate simultaneously.
        </p>

<pre>
Main Thread
    |
    +--> Webcam
    |
    +--> OpenCV
    |
    +--> MediaPipe
    |
    +--> Gesture Detection
</pre>

<pre>
Voice Thread
    |
    +--> Microphone
    |
    +--> Speech Recognition
    |
    +--> Command Processing
</pre>

        <p>
            Voice recognition runs in a separate thread so that the webcam
            interface remains responsive.
        </p>
    </section>

    <!-- PRIVACY -->
    <section>
        <h2>Security and Privacy</h2>

        <p>
            The current voice recognition implementation uses Google's
            speech recognition service.
        </p>

        <p>
            Voice data may be transmitted to the speech recognition service
            for processing.
        </p>

        <p>
            For privacy-sensitive applications, use a local speech recognition
            engine such as Vosk or Whisper.
        </p>

        <p>
            Gesture processing is performed locally using MediaPipe.
        </p>
    </section>

    <!-- FUTURE -->
    <section>
        <h2>Future Improvements</h2>

        <h3>Voice</h3>

        <ul>
            <li>Wake word detection</li>
            <li>Offline speech recognition</li>
            <li>Natural language commands</li>
            <li>Custom voice commands</li>
            <li>AI-powered command interpretation</li>
            <li>Conversational assistant</li>
            <li>Context-aware commands</li>
        </ul>

        <h3>Gesture</h3>

        <ul>
            <li>Swipe gestures</li>
            <li>Dwell-based interaction</li>
            <li>Contactless virtual buttons</li>
            <li>Gesture-based mouse control</li>
            <li>Gesture-based keyboard</li>
            <li>Two-hand gestures</li>
            <li>Custom gesture training</li>
        </ul>

        <h3>Computer Control</h3>

        <ul>
            <li>Mouse movement</li>
            <li>Left click</li>
            <li>Right click</li>
            <li>Double click</li>
            <li>Keyboard shortcuts</li>
            <li>Window switching</li>
            <li>Application management</li>
            <li>Screen brightness control</li>
            <li>Wi-Fi control</li>
            <li>Bluetooth control</li>
        </ul>

        <h3>Media</h3>

        <ul>
            <li>Play/Pause</li>
            <li>Volume control</li>
            <li>Next track</li>
            <li>Previous track</li>
            <li>Media selection</li>
            <li>Application-specific media control</li>
        </ul>
    </section>

    <!-- CONTACTLESS UI -->
    <section>
        <h2>Contactless Virtual Interface</h2>

        <p>
            The assistant can be extended with virtual buttons that can be
            controlled by moving the index finger over them.
        </p>

<pre>
+------------------------------------------------+
|          CONTACTLESS PC CONTROL                |
|                                                |
|       +--------+  +--------+  +--------+       |
|       |   -    |  |   M    |  |   +    |       |
|       +--------+  +--------+  +--------+       |
|                                                |
|             Move your finger                  |
|             over a button                     |
+------------------------------------------------+
</pre>

<pre>
Webcam
   |
   v
Hand Detection
   |
   v
Index Finger
   |
   v
X,Y Coordinates
   |
   v
Virtual Button Detection
   |
   v
PC Action
</pre>
    </section>

    <!-- AI -->
    <section>
        <h2>AI Integration</h2>

        <p>
            The project can be extended with an AI command engine to
            understand natural language.
        </p>

        <p>For example, instead of:</p>

<pre>
Volume 50
</pre>

        <p>The user could say:</p>

<pre>
Set the volume around half.
</pre>

        <p>Or:</p>

<pre>
It's too loud, reduce it a little.
</pre>

<pre>
User
 |
 v
Voice
 |
 v
Speech-to-Text
 |
 v
AI / NLP
 |
 v
Intent Detection
 |
 +-----------------------+
 |                       |
 v                       v
Volume Control       Application Control
</pre>
    </section>

    <!-- IOT -->
    <section>
        <h2>IoT Integration</h2>

        <p>
            The assistant can be connected to ESP32 or Raspberry Pi devices
            using MQTT.
        </p>

<pre>
Voice / Gesture
      |
      v
Python Assistant
      |
      v
MQTT
      |
      v
ESP32
      |
      +----------> LED
      |
      +----------> Relay
      |
      +----------> Motor
      |
      +----------> Sensor
</pre>

        <h3>Example</h3>

<pre>
Turn on the light
</pre>

<pre>
Voice
  |
  v
Speech Recognition
  |
  v
Command Parser
  |
  v
MQTT
  |
  v
ESP32
  |
  v
Relay ON
  |
  v
Light ON
</pre>
    </section>

    <!-- JETSON -->
    <section>
        <h2>Raspberry Pi / Jetson Integration</h2>

        <p>
            The project can potentially be deployed on:
        </p>

        <ul>
            <li>Raspberry Pi</li>
            <li>NVIDIA Jetson</li>
            <li>Other Linux-based edge devices</li>
        </ul>

        <p>
            The Windows-specific PyCaw component would need to be replaced
            with an operating-system-specific audio control library.
        </p>

<pre>
Windows
   |
   +--> PyCaw

Linux
   |
   +--> PulseAudio / PipeWire

Embedded Device
   |
   +--> Device-specific audio control
</pre>
    </section>

    <!-- ADVANCED -->
    <section>
        <h2>Advanced Multimodal Architecture</h2>

        <p>
            The long-term architecture can combine voice, gesture,
            eye tracking, AI, computer vision and IoT.
        </p>

<pre>
                             USER
                              |
        +---------------------+---------------------+
        |                     |                     |
        v                     v                     v
      VOICE                GESTURE                 EYE
        |                     |                     |
        v                     v                     v
 Speech-to-Text            MediaPipe           Eye Tracking
        |                     |                     |
        +---------------------+---------------------+
                              |
                              v
                       AI COMMAND ENGINE
                              |
            +-----------------+-----------------+
            |                 |                 |
            v                 v                 v
         Windows           Browser            Media
         Control           Control            Control
            |                 |                 |
            +-----------------+-----------------+
                              |
                              v
                        PC / IoT ACTION
                              |
                              v
                            ESP32
</pre>
    </section>

    <!-- FUTURE COMMANDS -->
    <section>
        <h2>Possible Future Commands</h2>

<pre>
Open YouTube and search for Python tutorials.

Set the volume to 40 percent.

Take a screenshot.

Open Chrome.

Play my music.

Increase the brightness.

Open my project folder.

Start the camera.

Turn on the IoT device.

Turn off the light.

Show me the system status.

Open my Git project.

Start the vision application.
</pre>
    </section>

    <!-- ROADMAP -->
    <section>
        <h2>Development Roadmap</h2>

        <h3>Phase 1 - Basic Assistant</h3>

        <ul>
            <li>Voice commands</li>
            <li>Gesture detection</li>
            <li>Volume control</li>
            <li>Application launching</li>
            <li>Screenshot capture</li>
        </ul>

        <h3>Phase 2 - Advanced Gestures</h3>

        <ul>
            <li>Swipe gestures</li>
            <li>Dwell interaction</li>
            <li>Virtual buttons</li>
            <li>Mouse control</li>
            <li>Keyboard control</li>
        </ul>

        <h3>Phase 3 - Offline AI</h3>

        <ul>
            <li>Offline speech recognition</li>
            <li>Local AI model</li>
            <li>Natural language commands</li>
            <li>Context-aware commands</li>
        </ul>

        <h3>Phase 4 - IoT</h3>

        <ul>
            <li>MQTT</li>
            <li>ESP32</li>
            <li>Raspberry Pi</li>
            <li>Sensors</li>
            <li>Relays</li>
            <li>Motors</li>
        </ul>

        <h3>Phase 5 - Full Multimodal Assistant</h3>

<pre>
Voice
Gesture
Eye Tracking
AI
Computer Vision
IoT
       |
       v
Multimodal PC Assistant
</pre>
    </section>

    <!-- TROUBLESHOOTING -->
    <section>
        <h2>Troubleshooting Checklist</h2>

<pre>
[ ] Python 3.12 installed
[ ] Correct virtual environment activated
[ ] NumPy 1.26.4 installed
[ ] OpenCV installed
[ ] MediaPipe 0.10.21 installed
[ ] PyCaw installed
[ ] Comtypes installed
[ ] SpeechRecognition installed
[ ] PyAudio installed
[ ] PyAutoGUI installed
[ ] Pyttsx3 installed
[ ] Webcam connected
[ ] Microphone connected
[ ] Speakers/headphones connected
[ ] Windows microphone permission enabled
[ ] Windows camera permission enabled
[ ] Internet connection available for voice recognition
</pre>
    </section>

    <!-- QUICK START -->
    <section>
        <h2>Quick Start</h2>

<pre>
conda create -n voice_gesture python=3.12 -y
conda activate voice_gesture

python -m pip install -r requirements.txt

python -m pip install --force-reinstall --no-deps numpy==1.26.4

python assistant.py
</pre>
    </section>

    <!-- LICENSE -->
    <section>
        <h2>License</h2>

        <p>
            This project is intended for educational, research and development purposes.
        </p>

        <p>
            You can replace this section with your preferred license.
        </p>

<pre>
MIT License
</pre>
    </section>

    <!-- AUTHOR -->
    <section>
        <h2>Author</h2>

        <p>
            Developed as a Python-based multimodal Human-Computer Interaction
            project combining:
        </p>

        <ul>
            <li>Computer Vision</li>
            <li>Hand Gesture Recognition</li>
            <li>Speech Recognition</li>
            <li>Text-to-Speech</li>
            <li>Windows Automation</li>
            <li>System Audio Control</li>
            <li>Media Control</li>
            <li>Browser Control</li>
            <li>Human-Computer Interaction</li>
            <li>IoT Integration</li>
        </ul>
    </section>

    <!-- SUMMARY -->
    <section>
        <h2>Project Summary</h2>

        <p>
            The <strong>Voice + Gesture PC Assistant</strong> demonstrates
            how computer vision and speech recognition can be combined to
            create a contactless human-computer interface.
        </p>

        <p>
            The current system allows users to interact with a Windows PC using:
        </p>

<pre>
Voice
  +
Hand Gestures
  =
Contactless PC Control
</pre>

        <p>
            The project provides a foundation for building an advanced
            AI-powered multimodal assistant capable of controlling:
        </p>

        <ul>
            <li>Windows applications</li>
            <li>Browser applications</li>
            <li>Media</li>
            <li>System volume</li>
            <li>Screenshots</li>
            <li>External IoT devices</li>
            <li>ESP32 devices</li>
            <li>Raspberry Pi devices</li>
            <li>Smart home systems</li>
        </ul>

        <div class="success">
            <strong>Goal:</strong>
            Build a complete multimodal AI assistant that can understand
            voice, gestures, visual input and natural language while
            interacting with computers and connected devices.
        </div>
    </section>

</div>

<footer>
    <p>Voice + Gesture PC Assistant</p>
    <p>Python • OpenCV • MediaPipe • Speech Recognition • PyCaw</p>
</footer>

</body>
</html>