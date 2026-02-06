import cv2
import time
from collections import deque


def main(camera_index: int = 0) -> None:
    """
    Basic FPS overlay with color feedback based on FPS value (moving average).

    Controls:
    - Press "q" to quit
    """
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"ERROR: Camera could not be opened (index={camera_index}).")
        print("Try changing the index: 0 --> 1 or 2")
        return

    window_name = "Vision Lab | FPS Overlay (Color + Avg)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Store time of previous frame
    previous_time = time.time()

    # Keep last N FPS values for a simple moving average
    fps_window = deque(maxlen=10)

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

            # Calculate FPS (instant)
            fps = (1 / delta_time) if delta_time > 0 else 0.0

            # Moving average FPS
            fps_window.append(fps)
            avg_fps = sum(fps_window) / len(fps_window)

            fps_text = f"FPS: {avg_fps:.1f}"

            # Choose text color based on average FPS thresholds
            if avg_fps < 15:
                color = (0, 0, 255)        # Red (BGR)
            elif avg_fps < 25:
                color = (0, 255, 255)      # Yellow (BGR)
            else:
                color = (0, 255, 0)        # Green (BGR)

            # Compute text position (top-right)
            h, w = frame.shape[:2]
            margin = 20
            (text_w, text_h), baseline = cv2.getTextSize(
                fps_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2
            )
            x = w - text_w - margin
            y = margin + text_h

            # Draw FPS text
            cv2.putText(
                frame,
                fps_text,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2,
                cv2.LINE_AA,
            )

            # Draw a tiny legend
            cv2.putText(
                frame,
                "Red<15 | Yellow 15-25 | Green>25",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow(window_name, frame)

            # 16 ms delay ~ 60 FPS cap (beginner-friendly)
            key = cv2.waitKey(16) & 0xFF
            if key == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
