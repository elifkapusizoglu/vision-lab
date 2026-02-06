import cv2

cam_capture=cv2.VideoCapture(0)

while (True):
    ret, goruntu=cam_capture.read()
    cv2.imshow("Goruntu", goruntu)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break




cam_capture.release()
cv2.destroyAllWindows()