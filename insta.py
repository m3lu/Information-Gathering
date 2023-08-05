import instaloader

insta = instaloader.Instaloader()

print("INSTA FINDER by melu")
username = input("Enter the username: ")

profile = instaloader.Profile.from_username(insta.context, username)
print("Username: ", profile.username)
print("Number of posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Bio: ", profile.biography)
print("Link: ", "https://www.instagram.com/" + username + "/")
