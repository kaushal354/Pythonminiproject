import streamlink

def download_stream(url, output_file="output.mp4"):
    try:
        # Fetch the available streams from the URL
        streams = streamlink.streams(url)
        
        # Check if streams are available
        if not streams:
            print("No streams available for the provided URL.")
            return
        
        # Get the best available stream (can also choose '720p', '480p', etc.)
        stream = streams.get('best')
        
        if stream:
            print(f"Downloading stream: {stream}")
            
            # Open the stream and start downloading
            with open(output_file, "wb") as file:
                stream_fd = stream.open()
                while True:
                    data = stream_fd.read(1024)  # Read the stream in chunks
                    if not data:
                        break
                    file.write(data)
            print(f"Download completed successfully. Saved as {output_file}")
        else:
            print("No suitable stream found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = input("Enter the streaming video URL: ")
download_stream(url, output_file="stream_video.mp4")

