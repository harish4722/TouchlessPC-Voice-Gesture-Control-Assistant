import cv2
import mediapipe as mp
import speech_recognition as sr
import pyttsx3
import pyautogui

import threading
import time
import os
import webbrowser
import subprocess
import ctypes
import math

from datetime import datetime
from pycaw.pycaw import AudioUtilities


# ============================================================
# CONFIGURATION
# ============================================================

CAMERA_INDEX = 0

GESTURE_COOLDOWN = 1.0

SCREENSHOT_FOLDER = "screenshots"


# ============================================================
# CREATE SCREENSHOT FOLDER
# ============================================================

if not os.path.exists(SCREENSHOT_FOLDER):
    os.makedirs(SCREENSHOT_FOLDER)


# ============================================================
# WINDOWS AUDIO
# ============================================================

devices = AudioUtilities.GetSpeakers()

volume = devices.EndpointVolume


def get_volume():

    value = volume.GetMasterVolumeLevelScalar()

    return int(value * 100)


def set_volume(value):

    value = max(0, min(100, value))

    volume.SetMasterVolumeLevelScalar(
        value / 100.0,
        None
    )


def volume_up():

    current = get_volume()

    new_volume = min(
        current + 5,
        100
    )

    set_volume(new_volume)

    return new_volume


def volume_down():

    current = get_volume()

    new_volume = max(
        current - 5,
        0
    )

    set_volume(new_volume)

    return new_volume


def mute():

    volume.SetMute(
        1,
        None
    )


def unmute():

    volume.SetMute(
        0,
        None
    )


def toggle_mute():

    muted = volume.GetMute()

    if muted:

        unmute()

        return False

    else:

        mute()

        return True


# ============================================================
# MEDIA CONTROL
# ============================================================

# Windows media virtual-key codes

VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1


def press_media_key(key):

    ctypes.windll.user32.keybd_event(
        key,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        key,
        0,
        2,
        0
    )


def play_pause():

    press_media_key(
        VK_MEDIA_PLAY_PAUSE
    )


def next_track():

    press_media_key(
        VK_MEDIA_NEXT_TRACK
    )


def previous_track():

    press_media_key(
        VK_MEDIA_PREV_TRACK
    )


# ============================================================
# TEXT TO SPEECH
# ============================================================

engine = pyttsx3.init()

engine.setProperty(
    "rate",
    170
)

engine.setProperty(
    "volume",
    1.0
)


def speak(text):

    print(
        "Assistant:",
        text
    )

    try:

        engine.say(text)

        engine.runAndWait()

    except Exception as e:

        print(
            "TTS Error:",
            e
        )


# ============================================================
# GLOBAL VARIABLES
# ============================================================

running = True

last_command = "Waiting for command..."

last_gesture = "No gesture"

last_gesture_time = 0


# ============================================================
# SCREENSHOT
# ============================================================

def take_screenshot():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = os.path.join(
        SCREENSHOT_FOLDER,
        f"screenshot_{timestamp}.png"
    )

    image = pyautogui.screenshot()

    image.save(filename)

    return filename


# ============================================================
# VOICE COMMAND HANDLER
# ============================================================

def execute_command(command):

    global running
    global last_command

    command = command.lower().strip()

    last_command = command

    print(
        "Command:",
        command
    )


    # --------------------------------------------------------
    # CLOSE ASSISTANT
    # --------------------------------------------------------

    if (
        "close assistant" in command
        or
        "exit assistant" in command
        or
        "stop assistant" in command
    ):

        speak("Closing assistant")

        running = False

        return


    # --------------------------------------------------------
    # YOUTUBE
    # --------------------------------------------------------

    if "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open(
            "https://www.youtube.com"
        )

        return


    # --------------------------------------------------------
    # GOOGLE
    # --------------------------------------------------------

    if "open google" in command:

        speak("Opening Google")

        webbrowser.open(
            "https://www.google.com"
        )

        return


    # --------------------------------------------------------
    # CHROME
    # --------------------------------------------------------

    if "open chrome" in command:

        speak("Opening Chrome")

        try:

            subprocess.Popen(
                "start chrome",
                shell=True
            )

        except Exception as e:

            print(e)

        return


    # --------------------------------------------------------
    # NOTEPAD
    # --------------------------------------------------------

    if "open notepad" in command:

        speak("Opening Notepad")

        subprocess.Popen(
            "notepad.exe"
        )

        return


    # --------------------------------------------------------
    # CALCULATOR
    # --------------------------------------------------------

    if "open calculator" in command:

        speak("Opening Calculator")

        subprocess.Popen(
            "calc.exe"
        )

        return


    # --------------------------------------------------------
    # SCREENSHOT
    # --------------------------------------------------------

    if (
        "take screenshot" in command
        or
        "capture screen" in command
    ):

        filename = take_screenshot()

        speak("Screenshot captured")

        print(
            "Saved:",
            filename
        )

        return


    # --------------------------------------------------------
    # MUTE
    # --------------------------------------------------------

    if command == "mute" or "mute volume" in command:

        mute()

        speak("Muted")

        return


    # --------------------------------------------------------
    # UNMUTE
    # --------------------------------------------------------

    if (
        command == "unmute"
        or
        "unmute volume" in command
    ):

        unmute()

        speak("Unmuted")

        return


    # --------------------------------------------------------
    # VOLUME UP
    # --------------------------------------------------------

    if (
        "volume up" in command
        or
        "increase volume" in command
        or
        "increase the volume" in command
    ):

        value = volume_up()

        speak(
            f"Volume {value} percent"
        )

        return


    # --------------------------------------------------------
    # VOLUME DOWN
    # --------------------------------------------------------

    if (
        "volume down" in command
        or
        "decrease volume" in command
        or
        "decrease the volume" in command
    ):

        value = volume_down()

        speak(
            f"Volume {value} percent"
        )

        return


    # --------------------------------------------------------
    # SET VOLUME
    # --------------------------------------------------------

    words = command.split()

    if "volume" in words:

        try:

            index = words.index(
                "volume"
            )

            if index + 1 < len(words):

                value = int(
                    words[index + 1]
                )

                if 0 <= value <= 100:

                    set_volume(
                        value
                    )

                    speak(
                        f"Volume set to {value} percent"
                    )

                    return

        except ValueError:

            pass


    # --------------------------------------------------------
    # PLAY / PAUSE
    # --------------------------------------------------------

    if (
        command == "play"
        or
        command == "pause"
        or
        "play music" in command
    ):

        play_pause()

        speak("Play pause")

        return


    # --------------------------------------------------------
    # NEXT
    # --------------------------------------------------------

    if (
        "next track" in command
        or
        "next song" in command
    ):

        next_track()

        speak("Next track")

        return


    # --------------------------------------------------------
    # PREVIOUS
    # --------------------------------------------------------

    if (
        "previous track" in command
        or
        "previous song" in command
    ):

        previous_track()

        speak("Previous track")

        return


    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    speak(
        "Sorry, I don't understand that command"
    )


# ============================================================
# VOICE RECOGNITION
# ============================================================

def voice_listener():

    global running

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300

    recognizer.dynamic_energy_threshold = True

    microphone = sr.Microphone()


    print()
    print(
        "Voice assistant started."
    )

    print(
        "Say a command..."
    )


    # --------------------------------------------------------
    # CALIBRATE MICROPHONE
    # --------------------------------------------------------

    try:

        with microphone as source:

            print(
                "Calibrating microphone..."
            )

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

    except Exception as e:

        print(
            "Microphone error:",
            e
        )

        return


    # --------------------------------------------------------
    # LISTEN LOOP
    # --------------------------------------------------------

    while running:

        try:

            with microphone as source:

                audio = recognizer.listen(
                    source,
                    timeout=1,
                    phrase_time_limit=4
                )


            print(
                "Processing voice..."
            )


            try:

                command = recognizer.recognize_google(
                    audio
                )

                print(
                    "You:",
                    command
                )

                execute_command(
                    command
                )

            except sr.UnknownValueError:

                pass

            except sr.RequestError as e:

                print(
                    "Speech recognition service error:",
                    e
                )


        except sr.WaitTimeoutError:

            pass

        except Exception as e:

            print(
                "Voice error:",
                e
            )

            time.sleep(1)


# ============================================================
# HAND GESTURE FUNCTIONS
# ============================================================

def distance(point1, point2):

    return math.sqrt(
        (point1.x - point2.x) ** 2
        +
        (point1.y - point2.y) ** 2
    )


def detect_gesture(hand):

    # --------------------------------------------------------
    # LANDMARKS
    # --------------------------------------------------------

    thumb_tip = hand.landmark[
        mp_hands.HandLandmark.THUMB_TIP
    ]

    thumb_ip = hand.landmark[
        mp_hands.HandLandmark.THUMB_IP
    ]


    index_tip = hand.landmark[
        mp_hands.HandLandmark.INDEX_FINGER_TIP
    ]

    index_pip = hand.landmark[
        mp_hands.HandLandmark.INDEX_FINGER_PIP
    ]


    middle_tip = hand.landmark[
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP
    ]

    middle_pip = hand.landmark[
        mp_hands.HandLandmark.MIDDLE_FINGER_PIP
    ]


    ring_tip = hand.landmark[
        mp_hands.HandLandmark.RING_FINGER_TIP
    ]

    ring_pip = hand.landmark[
        mp_hands.HandLandmark.RING_FINGER_PIP
    ]


    pinky_tip = hand.landmark[
        mp_hands.HandLandmark.PINKY_TIP
    ]

    pinky_pip = hand.landmark[
        mp_hands.HandLandmark.PINKY_PIP
    ]


    # --------------------------------------------------------
    # FINGER STATES
    # --------------------------------------------------------

    index_open = (
        index_tip.y
        <
        index_pip.y
    )


    middle_open = (
        middle_tip.y
        <
        middle_pip.y
    )


    ring_open = (
        ring_tip.y
        <
        ring_pip.y
    )


    pinky_open = (
        pinky_tip.y
        <
        pinky_pip.y
    )


    # --------------------------------------------------------
    # THUMB UP
    # --------------------------------------------------------

    thumb_up = (
        thumb_tip.y
        <
        thumb_ip.y
        and
        not index_open
        and
        not middle_open
        and
        not ring_open
        and
        not pinky_open
    )


    # --------------------------------------------------------
    # THUMB DOWN
    # --------------------------------------------------------

    thumb_down = (
        thumb_tip.y
        >
        thumb_ip.y
        and
        not index_open
        and
        not middle_open
        and
        not ring_open
        and
        not pinky_open
    )


    # --------------------------------------------------------
    # FIST
    # --------------------------------------------------------

    fist = (
        not index_open
        and
        not middle_open
        and
        not ring_open
        and
        not pinky_open
        and
        not thumb_up
        and
        not thumb_down
    )


    # --------------------------------------------------------
    # VICTORY / TWO FINGERS
    # --------------------------------------------------------

    victory = (
        index_open
        and
        middle_open
        and
        not ring_open
        and
        not pinky_open
    )


    if thumb_up:

        return "THUMB UP"


    if thumb_down:

        return "THUMB DOWN"


    if victory:

        return "VICTORY"


    if fist:

        return "FIST"


    if (
        index_open
        and
        middle_open
        and
        ring_open
        and
        pinky_open
    ):

        return "OPEN PALM"


    return "UNKNOWN"


# ============================================================
# GESTURE ACTION
# ============================================================

def execute_gesture(gesture):

    global last_gesture_time
    global last_gesture

    current_time = time.time()


    # Prevent repeated activation

    if (
        current_time
        -
        last_gesture_time
        <
        GESTURE_COOLDOWN
    ):

        return


    # --------------------------------------------------------
    # THUMB UP
    # --------------------------------------------------------

    if gesture == "THUMB UP":

        value = volume_up()

        last_gesture = (
            f"Volume + : {value}%"
        )

        last_gesture_time = current_time

        print(
            "Gesture:",
            last_gesture
        )


    # --------------------------------------------------------
    # THUMB DOWN
    # --------------------------------------------------------

    elif gesture == "THUMB DOWN":

        value = volume_down()

        last_gesture = (
            f"Volume - : {value}%"
        )

        last_gesture_time = current_time

        print(
            "Gesture:",
            last_gesture
        )


    # --------------------------------------------------------
    # FIST
    # --------------------------------------------------------

    elif gesture == "FIST":

        mute()

        last_gesture = "Muted"

        last_gesture_time = current_time

        print(
            "Gesture: Mute"
        )


    # --------------------------------------------------------
    # VICTORY
    # --------------------------------------------------------

    elif gesture == "VICTORY":

        play_pause()

        last_gesture = "Play / Pause"

        last_gesture_time = current_time

        print(
            "Gesture: Play / Pause"
        )


# ============================================================
# MEDIAPIPE SETUP
# ============================================================

mp_hands = mp.solutions.hands

mp_draw = mp.solutions.drawing_utils


hands = mp_hands.Hands(

    static_image_mode=False,

    max_num_hands=1,

    min_detection_confidence=0.7,

    min_tracking_confidence=0.7
)


# ============================================================
# START VOICE THREAD
# ============================================================

voice_thread = threading.Thread(
    target=voice_listener,
    daemon=True
)

voice_thread.start()


# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(
    CAMERA_INDEX
)


if not cap.isOpened():

    print(
        "ERROR: Camera could not be opened."
    )

    running = False

    exit()


cap.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    1280
)

cap.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    720
)


# ============================================================
# MAIN CAMERA LOOP
# ============================================================

while running:

    success, frame = cap.read()


    if not success:

        print(
            "Camera frame failed."
        )

        break


    # Mirror camera

    frame = cv2.flip(
        frame,
        1
    )


    # --------------------------------------------------------
    # RGB
    # --------------------------------------------------------

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------------------------------
    # HAND DETECTION
    # --------------------------------------------------------

    results = hands.process(
        rgb
    )


    gesture = "No hand"


    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]


        # Draw landmarks

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )


        # Detect gesture

        gesture = detect_gesture(
            hand
        )


        # Execute gesture

        execute_gesture(
            gesture
        )


    # ========================================================
    # USER INTERFACE
    # ========================================================

    current_volume = get_volume()


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    cv2.putText(
        frame,
        "VOICE + GESTURE PC ASSISTANT",
        (300, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )


    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    cv2.putText(
        frame,
        f"Volume: {current_volume}%",
        (30, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )


    # --------------------------------------------------------
    # GESTURE
    # --------------------------------------------------------

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (30, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )


    # --------------------------------------------------------
    # LAST ACTION
    # --------------------------------------------------------

    cv2.putText(
        frame,
        f"Action: {last_gesture}",
        (30, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # --------------------------------------------------------
    # LAST VOICE COMMAND
    # --------------------------------------------------------

    cv2.putText(
        frame,
        f"Voice: {last_command}",
        (30, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # ========================================================
    # VOLUME BAR
    # ========================================================

    bar_x = 30
    bar_y = 260

    bar_width = 400
    bar_height = 35


    cv2.rectangle(
        frame,
        (
            bar_x,
            bar_y
        ),
        (
            bar_x + bar_width,
            bar_y + bar_height
        ),
        (60, 60, 60),
        -1
    )


    volume_width = int(
        bar_width
        *
        current_volume
        /
        100
    )


    cv2.rectangle(
        frame,
        (
            bar_x,
            bar_y
        ),
        (
            bar_x + volume_width,
            bar_y + bar_height
        ),
        (0, 255, 0),
        -1
    )


    # ========================================================
    # VOICE COMMAND HELP
    # ========================================================

    cv2.putText(
        frame,
        "Voice Commands:",
        (30, 350),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    commands = [
        "Open YouTube",
        "Open Chrome",
        "Volume Up / Down",
        "Volume 50",
        "Mute / Unmute",
        "Take Screenshot",
        "Play / Pause",
    ]


    y = 390


    for command in commands:

        cv2.putText(
            frame,
            command,
            (50, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (200, 200, 200),
            1
        )

        y += 30


    # ========================================================
    # GESTURE HELP
    # ========================================================

    cv2.putText(
        frame,
        "Gestures:",
        (700, 350),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    gesture_help = [
        "Thumb Up  -> Volume +",
        "Thumb Down -> Volume -",
        "Fist -> Mute",
        "Two Fingers -> Play/Pause",
    ]


    y = 390


    for item in gesture_help:

        cv2.putText(
            frame,
            item,
            (720, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (200, 200, 200),
            1
        )

        y += 30


    # ========================================================
    # EXIT
    # ========================================================

    cv2.putText(
        frame,
        "Press Q to exit",
        (520, 680),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (180, 180, 180),
        2
    )


    # ========================================================
    # SHOW
    # ========================================================

    cv2.imshow(
        "Voice + Gesture PC Assistant",
        frame
    )


    # ========================================================
    # KEYBOARD
    # ========================================================

    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):

        running = False

        break


# ============================================================
# CLEANUP
# ============================================================

running = False

cap.release()

cv2.destroyAllWindows()

hands.close()

print(
    "Voice + Gesture Assistant stopped."
)