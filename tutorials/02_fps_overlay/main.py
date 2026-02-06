import cv2
import time

#open default camera

camera=cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR, Camera could not be opened..!")
    exit()


#store time of previous frame
 previous_time= time.time()

while True:
    #Read from the camera
    ret, frame=camera.read()
    if not ret:
        break

    # Get current time
    current_time = time.time()

    # Calculate time difference between frames
    delta_time = current_time - previous_time
    previous_time = current_time

    # Calculate FPS
    if delta_time > 0:
        fps = 1 / delta_time
    else:
        fps = 0

    # Draw FPS text on the frame
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show frame
    cv2.imshow("Vision Lab | Basic FPS", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()