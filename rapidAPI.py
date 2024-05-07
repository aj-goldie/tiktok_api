import requests
import sys
import os
from moviepy.editor import *


def main():

    os.chdir(os.path.dirname(__file__))

    # Check if the URL is passed as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a TikTok URL as an argument.")
        sys.exit(1)  # Exit the script if no argument is provided

    # Get the TikTok URL from the first command-line argument
    tiktok_url = sys.argv[1]

    # Define the API URL
    url = "https://tiktok-download-video-no-watermark.p.rapidapi.com/tiktok/info"

    # Set up the query parameters with the user's input
    querystring = {"url": tiktok_url}

    # Define the headers including your RapidAPI key and host
    headers = {
        "X-RapidAPI-Key": "1bdc285ac0msh76fea54464643bap145095jsnf5b7fac3e6c3",
        "X-RapidAPI-Host": "tiktok-download-video-no-watermark.p.rapidapi.com",
    }

    # Make the GET request to the API
    response = requests.get(url, headers=headers, params=querystring)

    # Parse the JSON response
    data = response.json()

    # Extract the video URL from the 'video_link_nwm_hd' key
    video_url = data["data"]["video_link_nwm"]

    # Download the video using the extracted URL
    video_response = requests.get(video_url)
    if video_response.status_code == 200:
        with open("downloaded_video/downloaded_video.mp4", "wb") as file:
            file.write(video_response.content)
        print("Video downloaded successfully!")
    else:
        print("Failed to download video.")


# Load the MP4 video file
video = VideoFileClip("downloaded_video/downloaded_video.mp4")

# Extract the audio from the video
audio = video.audio

# Write the audio to an MP3 file
audio.write_audiofile("extracted_audio/extracted_audio.mp3")


# Check if the script is run directly (not imported)
if __name__ == "__main__":
    main()
