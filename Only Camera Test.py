import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,0)

    cv2.imshow("Only Camera Test", frame)

    key = cv2.waitKey(27)

    if key == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break

cv2.destroyAllWindows()
cap.release() 


