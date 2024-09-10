Here’s a well-structured `README.md` file for the provided codes.

---

# Hand Tracking and Gesture-Based Mouse Controller

This project implements real-time hand tracking using the `mediapipe` library and maps specific hand gestures to mouse movements and clicks using the `pyautogui` library. The system utilizes a webcam to detect hand landmarks and interprets these gestures to control the mouse cursor.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Files](#files)
- [Potential Improvements](#potential-improvements)
- [Contributing](#contributing)

## Overview

This project demonstrates a basic implementation of gesture recognition for controlling the mouse using hand movements. It captures the hand using the webcam and tracks the hand's position and gestures (like finger movement). The system is divided into two parts:
1. **Hand Tracking Module**: Detects and tracks hand gestures.
2. **Mouse Controller**: Uses hand gestures to move the mouse cursor and perform clicks.

## Project Structure

The project consists of two Python scripts:
1. **HandTrackingModule.py**: Detects and tracks hand landmarks using the Mediapipe library.
2. **MouseClicker.py**: Maps the detected hand gestures to mouse movements and click actions using PyAutoGUI.

## Setup and Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- `mediapipe` library
- `opencv-python`
- `pyautogui`
- `numpy`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parth-agrawall/Hand-Tracking-and-Gesture-AI-Mouse-Controlling-System.git
   ```

2. Navigate into the project directory:
   ```bash
   cd HandGestureMouseControl
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If you do not have a `requirements.txt`, manually install the libraries:
   ```bash
   pip install mediapipe opencv-python pyautogui numpy
   ```

## How It Works

### Hand Tracking

The **HandTrackingModule.py** script uses the Mediapipe library to detect hands and identify 21 unique hand landmarks. These landmarks are used to track the positions of each finger and identify gestures, such as whether fingers are up or down.

### Mouse Controller

The **MouseClicker.py** script uses the hand positions and gestures detected by the Hand Tracking module to move the mouse cursor and perform clicks. It uses the following gestures:
- **Index Finger Up**: Moves the mouse cursor.
- **Index and Middle Finger Up and Close**: Performs a mouse click.

The cursor movement is smoothed for better control, and the gestures are detected in real-time.

## Usage

### Running the Project

1. **Start the Hand Tracking Module**:
   - To test hand detection, run `HandTrackingModule.py`:
     ```bash
     python HandTrackingModule.py
     ```

   This will open a window where you can see your hand landmarks being detected in real-time.

2. **Run the Mouse Controller**:
   - To control your mouse with hand gestures, run `MouseClicker.py`:
     ```bash
     python MouseClicker.py
     ```

   This script will track your hand and allow you to move the mouse cursor and click based on the defined gestures.

### Control Explanation:
- **Move the Mouse**: Hold your index finger up and move your hand within the frame.
- **Click**: Make a "pinching" gesture by bringing your index and middle fingers close together.

Press **'q'** to quit the application.

## Files

- **HandTrackingModule.py**:
  - Contains the hand tracking logic using `mediapipe`.
  - Defines the `handDetector` class that tracks hand landmarks and identifies gestures.
  
- **MouseClicker.py**:
  - Integrates the `handDetector` class and uses `pyautogui` to map gestures to mouse movements and clicks.

## Potential Improvements

- **Add more gestures**: You could implement gestures for right-click, scroll, or multi-finger swipes.
- **Refine accuracy**: You could fine-tune the detection thresholds for different hand gestures.
- **Optimize performance**: Test on different hardware setups to improve FPS and detection speed.

## Contributing

If you would like to contribute to this project, feel free to open an issue or submit a pull request.


---
