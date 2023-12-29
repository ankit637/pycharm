import requests
import time

def check_download_speed(url):
    start_time = time.time()
    response = requests.get(url, stream=True)
    file_size = 0
    chunk_size = 1024  # 1 KB

    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=chunk_size):
            file_size += len(chunk)
    else:
        print("Failed to fetch the file.")

    end_time = time.time()
    download_time = end_time - start_time
    download_speed = (file_size / 1024) / download_time  # Speed in KB/s

    return download_speed

# Example URL for testing download speed
file_url = 'https://youtu.be/8H6VIpS_XiA?si=4NdOs43b7vuFXyS9'

speed = check_download_speed(file_url)
print(f"Download speed: {speed:.2f} KB/s")
