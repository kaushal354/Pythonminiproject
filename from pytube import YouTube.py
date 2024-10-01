import yt_dlp

def download_video(link):
    ydl_opts = {}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

link = input("Enter the YouTube video URL: ")
download_video(link)

