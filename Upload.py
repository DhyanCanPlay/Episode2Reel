import os
import time
from instagrapi import Client

# Login to Instagram
username = "your_username"
password = "your_password"

client = Client()
client.login(username, password)

# Folder containing reels
folder_path = "path_to_your_folder"

# Caption and hashtags for the posts
caption = "Your caption here #hashtag1 #hashtag2"

# Get list of video files in the folder
reels = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.mov'))]

# Upload each reel with a 50-minute gap
for reel in reels:
    reel_path = os.path.join(folder_path, reel)
    client.clip_upload(reel_path, caption)
    print(f"Uploaded: {reel}")

    # Wait for 50 minutes before uploading the next reel
    time.sleep(50 * 60)
