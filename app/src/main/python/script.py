import instaloader


def download(profile,custom_save_location=""):
    profile = profile.replace(" ", "")
    user = instaloader.Instaloader()
    user.save_metadata = False
    user.post_metadata_txt_pattern = ""
    if custom_save_location=="":
        user.dirname_pattern = f"/sdcard/InstaLoaderApp/{profile}"
    else:
        user.dirname_pattern = custom_save_location
    user.download_profile(profile)


def post_count(username):
    username = username.replace(" ", "")
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    posts = profile.get_posts()

    return posts.count

# for reference: https://github.com/instaloader/instaloader/issues/1851
def download_post_from_link(shortcode):
    L = instaloader.Instaloader()
    L.dirname_pattern = f"/sdcard/InstaLoaderApp/posts"
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, target = "")