import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    extra_var, image = webcam.read()
    image = cv2.flip(image, 1)
    frame_h, frame_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, lm in enumerate(landmarks):
                x = int(lm.x * frame_w)
                y = int(lm.y * frame_h)
                if id == 8:
                    cv2.circle(image, (x, y), 10, (0, 255, 255), 3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(image, (x, y), 10, (0, 0, 255), 3)
                    x2 = x
                    y2 = y
        dist=((x2-x1)**2+(y2-y1)**2)**(0.5)//4
        print(dist)
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        if dist > 50 :
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")
    cv2.imshow("Hand Volume Control using Python", image)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
