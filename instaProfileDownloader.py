import instaloader as il

insta =il.Instaloader()
username=input('Enter Username: ')
insta.download_profile(username,profile_pic_only=True)
