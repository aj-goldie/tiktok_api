import asyncio
from TikTokApi import TikTokApi


async def download_video(video_url):
    async with TikTokApi() as api:
        # Create sessions
        await api.create_sessions(
            ms_tokens=[
                "n3VGqZJP2Ni_xxpQ7oHYhTsXwzSCBiVSexi5M-917x7bTpGHwc0VNKz4EYedI5zm1pWPEXk5hFETLW989D6kOXxJvY1RMcsi4pXMhvoH0j8ExxPBDgMV0Ql6ZKSC"
            ],
            num_sessions=1,
            sleep_after=3,
        )
        video = api.video(url=video_url)
        video_bytes = await video.bytes()

        # Saving The Video
        with open(f"{video.id}.mp4", "wb") as output:
            output.write(video_bytes)

        print(f"Video {video.id} downloaded successfully!")


if __name__ == "__main__":
    video_url = input("Enter the TikTok video URL: ")
    asyncio.run(download_video(video_url))
