#!/usr/bin/env python3
"""
Live RealSense demo — runs SAM 3D Body on each frame from the camera
and displays the mesh overlay in real time.

Usage:
    python demo_realsense_live.py
    python demo_realsense_live.py --detector_model ./checkpoints/yolo/yolo11m-pose.pt

Press Q to quit.
"""
import argparse
import os

import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml", ".sl"],
    pythonpath=True,
    dotenv=True,
)

import cv2
from notebook.utils import setup_sam_3d_body
from mocap.utils.video_source import RealSenseSource
from tools.vis_utils import visualize_sample_together


def main(args):
    print("Loading model...")
    estimator = setup_sam_3d_body(
        local_checkpoint_path=args.local_checkpoint,
        detector_name="yolo_pose",
        detector_path=args.detector_model,
        detector_model=args.detector_model,
        fov_name="moge2",
        device="cuda",
    )

    print("Starting RealSense camera...")
    source = RealSenseSource(width=848, height=480, fps=30)

    cv2.namedWindow("SAM 3D Body — Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("SAM 3D Body — Live", 1920, 270)  # 4-panel wide, scaled to fit screen

    print("Running — press Q to quit.")
    while True:
        frame, _ = source.get_frame()
        if frame is None:
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        outputs = estimator.process_one_image(
            frame_rgb,
            bbox_thr=0.5,
            hand_box_source="yolo_pose",
        )

        if outputs:
            vis = visualize_sample_together(frame, outputs, estimator.faces)
            cv2.imshow("SAM 3D Body — Live", vis.astype("uint8"))
        else:
            cv2.imshow("SAM 3D Body — Live", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    source.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local_checkpoint",
        default="./checkpoints/sam-3d-body-dinov3",
        help="Local checkpoint directory",
    )
    parser.add_argument(
        "--detector_model",
        default="./checkpoints/yolo/yolo11m-pose.pt",
        help="YOLO pose model path",
    )
    args = parser.parse_args()
    main(args)
