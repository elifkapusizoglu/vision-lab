import cv2
import os


def main() -> None:
    """
    Beginner-friendly video reader.
    This example reads frames from a video file (no camera, no CLI arguments).
    """

    # Video file path (put the video in the same folder)
    video_path = "sample.mp4"

    if not os.path.exists(video_path):
        print(f"ERROR: Video file not found: {video_path}")
        print("Tip: Put 'sample.mp4' in the same folder as this script.")
        return

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"ERROR: Could not open video: {video_path}")
        return

    window_name = "Vision Lab | Video Input Basics (Video File)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame = cap.read()

            # End of video
            if not ret or frame is None:
                print("End of video.")
                break

            cv2.putText(
                frame,
                "Video playback (press q to quit)",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow(window_name, frame)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
