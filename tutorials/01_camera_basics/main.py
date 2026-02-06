# Camera basics tutorial entrypoint

import cv2


def main(camera_index: int=0) -> None:
    """
        Beginner friendly camera viewer.

        Controls: 
        -Press "q" to quit

        Tips:
        - If your camera doesn't open, try camera index=1 or 2.
    """
    cap= cv2.VideoCapture(camera_index)

    #Some wabcams wait a moment; optionals but helps stability.
    # cap.set(cv2.CAP_PROF_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROF_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print(f"ERROR  Camera could not be opened (index={camera_index})." )
        print("Try changing the index: 0 --> 1 or 2")
        return
    window_name="Camera Basics(press q to quit)"
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame=cap.read()
            
            if not ret or frame is None:
                print("[Error] Frame could not be read from camera")
                break


            # Simple overlay for beginners to confirm loop is alive
            cv2.putText(
                frame,
                "press q to quit",
                (20,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2,
            )

            cv2.imshow(window_name,frame)
            key=cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
if __name__=="__main__":
    main()
