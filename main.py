import instaloader
import re


def get_shortcode(url):
    pattern = r"instagram\.com/(?:reel|p|tv)/([^/?#]+)"
    resultado = re.search(pattern, url)

    if resultado:
        return resultado.group(1)
    else:
        return None


url = input("Paste the Instagram Reel URL: ")

shortcode = get_shortcode(url)

if shortcode is None:
    print("Invalid URL")
else:
    loader = instaloader.Instaloader(
        download_pictures=True,
        download_videos=False,
        download_video_thumbnails=True,
        download_comments=False,
        save_metadata=False,
        post_metadata_txt_pattern=""
    )

    post = instaloader.Post.from_shortcode(loader.context, shortcode)

    loader.download_post(post, target="instagram_thumbnails")

    print("Thumbnail downloaded successfully.")
