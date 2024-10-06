import instagrapi

# Replace with your Instagram account credentials
username = "dhyancanplay@gmail.com"
password = "papanmom2008@@"

# Replace with the path to your reel video file
reel_path = "/upload_video/reel.mp4"

# Create an Instagram API client
client = instagrapi.Client()

# Login to your Instagram account
client.login(username, password)

# Upload the reel
reel_result = client.upload_reel(reel_path)

# Print the reel's ID for reference
print("Reel ID:", reel_result.id)
