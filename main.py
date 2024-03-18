import cv2
import math

def extract_frames(video_path, output_folder, num_frames=430):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")
        return
    
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = math.ceil(total_frames / num_frames)
    
    # Calculate new dimensions for the aspect ratio
    original_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    original_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    aspect_ratio = 8 / 5
    new_width = original_width
    new_height = round(new_width / aspect_ratio)
    if new_height > original_height:
        new_height = original_height
        new_width = round(new_height * aspect_ratio)
    
    # Ensure dimensions are integers
    new_width = int(new_width)
    new_height = int(new_height)
    
    for i in range(0, total_frames, interval):
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = video.read()
        if not success:
            break
        # Resize frame to maintain aspect ratio
        resized_frame = cv2.resize(frame, (new_width, new_height))
        # Save frame
        cv2.imwrite(f"{output_folder}/{i // interval + 1}.jpg", resized_frame)
        print(f"Frame {i // interval + 1} saved.")
    
    video.release()
    print("Done.")

# Example usage
video_path = 'video.mp4'  # Update this to your video's path
output_folder = 'output_images'  # Make sure this directory exists
extract_frames(video_path, output_folder)
