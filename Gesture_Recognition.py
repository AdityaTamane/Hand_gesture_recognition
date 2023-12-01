import os
import time

import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

# Keyboard Lib Setup
keyboard = Controller()

# Variables
width, height = 1280, 720

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Gesture Left
        if fingers == [1, 1, 1, 1, 0]:
            print("Left")
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            time.sleep(1)

        # Gesture Right
        if fingers == [0, 1, 1, 1, 1]:
            print("Right")
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            time.sleep(1)

        # Gesture Up
        if fingers == [0, 1, 1, 0, 0]:
            print("Up")
            keyboard.press(Key.up)
            keyboard.release(Key.up)

        # Gesture Down
        if fingers == [0, 0, 1, 1, 1]:
            print("Down")
            keyboard.press(Key.down)
            keyboard.release(Key.down)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break