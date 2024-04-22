import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard

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
            keyboard.press("left")
            keyboard.release("left")

        # Gesture Right
        elif fingers == [0, 1, 1, 1, 1]:
            print("Right")
            keyboard.press("right")
            keyboard.release("right")

        # Gesture Up
        elif fingers == [0, 1, 1, 0, 0]:
            print("Up")
            keyboard.press("up")
            keyboard.release("up")

        # Gesture Down
        elif fingers == [0, 0, 1, 1, 1]:
            print("Down")
            keyboard.press("down")
            keyboard.release("down")

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
