import instaloader, os
profile_name = input("Enter the Instagram Account name: ")
try:
    print("Downloading media")
    instaloader.Instaloader(
        download_videos=False,
        download_comments=False,
        download_geotags=False,
        download_pictures=True,
        download_video_thumbnails=False,
        save_metadata=False,
        compress_json=False,
        ).download_profile(profile_name, profile_pic=False)

    
    print("Download Completed")
except ValueError:
    print(f"An error was encountered, try again or there is no account {profile_name}")

