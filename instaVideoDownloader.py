import instaloader, os
profile_name = input("Instagram Hesap adını girin: ")
try:
    print("Downloading media")
    instaloader.Instaloader(
        download_videos=True,
        download_comments=False,
        download_geotags=False,
        download_pictures=False,
        download_video_thumbnails=False,
        save_metadata=False,
        compress_json=False,
        ).download_profile(profile_name, profile_pic=False)

    # for file in os.listdir(profile_name):
    #     if file.endswith('.txt'):
    #         file_path = os.path.join(profile_name, file)
    #         os.remove(file_path)
    print("Download Completed")
except ValueError:
    print(f"Bir hata ile karşılaşıldı, tekrar deneyin yada {profile_name} hesabı yok")

