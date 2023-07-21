import instaloader

def download_profile_image(username):

    loader = instaloader.Instaloader()
        
    profile = instaloader.Profile.from_username(loader.context, username)
        
    loader.download_profile(profile, profile_pic_only=True)


if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    download_profile_image(username)