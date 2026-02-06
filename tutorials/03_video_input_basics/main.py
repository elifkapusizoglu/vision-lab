import cv2
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Video input basics: camera or video file.")
    parser.add_argument(
        "--source",
        type=str,
        default="0",
        help='Video source: camera index (e.g., "0") or file path (e.g., "sample.mp4").',
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Convert numeric strings to int for camera index
    source = int(args.source) if args.source.isdigit() else args.source

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"ERROR: Could not open source: {args.source}")
        print('Tips: try --source 0 or --source 1, or provide a valid video file path.')
        return

    window_name = "Vision Lab | Video Input Basics (press q to quit)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame = cap.read()

            # For video files, ret becomes False at the end of the file
            if not ret or frame is None:
                print("End of stream or frame read error.")
                break

            cv2.putText(
                frame,
                f"Source: {args.source} (press q to quit)",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
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
