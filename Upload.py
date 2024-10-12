import os
import re
import time
from instagrapi import Client

# Instagram login
cl = Client()
cl.login('username', 'password')

# Path to the folder containing reels
folder_path = './output_video'
caption = "Follow for more naruto episodes Daily.   This Reel was uploaded with Code.  #anime #naruto #hinata #animeart #animegirl #animeedits #animememes #narutoshippuden #animeedit #animes #animelover #animedrawing #animeboy #animegirls #animelove #animefan #animeworld #animefanart #narutouzumaki #animefans #animeartist #animeaccount #animescene #animejapan #animewallpaper #animeromance #anime_sketches25 #animerecommendations #weeaboo"
thumbnail = './output_folder/thumbnail.jpg'
# Function to extract numbers from filenames
def extract_number(filename):
    match = re.search(r'\d+', filename)  # Find digits in the filename
    return int(match.group()) if match else float('inf')  # Return a large number if no digits

# Get a list of all video files in the folder
video_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.mov'))]

# Sort the files by the number in their filenames
video_files.sort(key=extract_number)

# Upload each video one by one
for video_file in video_files:
    video_path = os.path.join(folder_path, video_file)
    try:
        cl.clip_upload(video_path, caption=caption, thumbnail=thumbnail)
        print(f"Uploaded: {video_file}")
    except Exception as e:
        print(f"Failed to upload {video_file}: {e}")

    # Wait for 5 minutes (300 seconds) between uploads
    time.sleep(300)

print("All uploads complete!")
