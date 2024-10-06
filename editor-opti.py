import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip

# Parameters
ep = "12"  # Episode number
input_video = "ep12.mp4"  # Ensure correct path
output_folder = "output_videos"
os.makedirs(output_folder, exist_ok=True)
duration_per_part = 60  # in seconds
fps = 30

def process_video_with_text(input_video, ep):
    try:
        clip = VideoFileClip(input_video)
    except Exception as e:
        print(f"Error loading video: {e}")
        return

    num_parts = int(clip.duration // duration_per_part) + 1
    print(f"Processing video into {num_parts} parts...")

    for i in range(num_parts):
        start_time = i * duration_per_part
        end_time = min((i + 1) * duration_per_part, clip.duration)
        
        part_path = os.path.join(output_folder, f"ep{ep}_part_{i + 1}.mp4")
        print(f"Writing video part {i + 1} to {part_path}...")
        
        # Open video capture from the input video
        cap = cv2.VideoCapture(input_video)
        
        # Set the starting frame position
        cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)

        # Prepare VideoWriter
        width, height = 1080, 1920  # Target 9:16 frame size
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(part_path, fourcc, fps, (width, height))
        
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or cap.get(cv2.CAP_PROP_POS_MSEC) >= end_time * 1000:
                print(f"Finished processing part {i + 1} after {frame_count} frames.")
                break

            # Resize the frame (16:9 -> 1080x608)
            frame = cv2.resize(frame, (1080, 608))
            background = np.zeros((1920, 1080, 3), dtype=np.uint8)
            y_offset = (1920 - 608) // 2
            background[y_offset:y_offset + 608, 0:1080] = frame
            
            # Add text (Ep: x Part: x)
            text = f"Ep: {ep} Part: {i + 1}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_position = (100, 500)  # Position 100px from the top
            font_scale = 2
            color = (255, 255, 255)  # White text
            thickness = 4
            cv2.putText(background, text, text_position, font, font_scale, color, thickness, cv2.LINE_AA)
            
            # Write the frame to the output video
            out.write(background)
            frame_count += 1

        cap.release()
        out.release()
    
    print("Processing complete.")

# Run the process
process_video_with_text(input_video, ep)
