import cv2
import time


def main(camera_index: int = 0) -> None:
    """
    Beginner friendly camera viewer with a basic FPS overlay.

    Controls:
    - Press "q" to quit

    Tips:
    - If your camera doesn't open, try camera index=1 or 2.
    """
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"ERROR: Camera could not be opened (index={camera_index}).")
        print("Try changing the index: 0 --> 1 or 2")
        return

    window_name = "Vision Lab | FPS Overlay (Starter)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Store time of previous frame
    previous_time = time.time()

    try:
        while True:
            ret, frame = cap.read()

            if not ret or frame is None:
                print("[Error] Frame could not be read from camera")
                break

            # Get current time
            current_time = time.time()

            # Calculate time difference between frames
            delta_time = current_time - previous_time
            previous_time = current_time

            # Calculate FPS
            fps = (1 / delta_time) if delta_time > 0 else 0.0
            fps_text = f"FPS: {fps:.1f}"

            # Compute text position (top-right)
            h, w = frame.shape[:2]
            margin = 20
            (text_w, text_h), baseline = cv2.getTextSize(
                fps_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2
            )
            x = w - text_w - margin
            y = margin + text_h  # keep it inside the frame

            # Draw FPS text on the frame (top-right)
            cv2.putText(
                frame,
                fps_text,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow(window_name, frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
