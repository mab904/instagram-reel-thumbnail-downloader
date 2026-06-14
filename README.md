# Instagram Reel Thumbnail Downloader

A simple Python tool to download the thumbnail image from an Instagram Reel without downloading the full video.

This project is useful if you want to save only the cover image of a Reel for organization, content analysis, inspiration boards, or personal reference.

## Features

* Download Instagram Reel thumbnails
* Does not download the video
* Does not download captions or metadata files
* Simple command-line usage
* Saves thumbnails automatically into a folder

## Requirements

* Python 3
* Instaloader

## Installation

First, install the required library:

```bash
pip install instaloader
```

## Usage

Run the Python file:

```bash
python main.py
```

Then paste the Instagram Reel URL when asked:

```bash
Paste the Instagram Reel URL:
```

Example:

```bash
https://www.instagram.com/reel/XXXXXXXXXXX/
```

The thumbnail will be downloaded into a folder called:

```bash
instagram_thumbnails
```

## Code

```python
import instaloader
import re


def get_shortcode(url):
    pattern = r"instagram\.com/(?:reel|p|tv)/([^/?#]+)"
    result = re.search(pattern, url)

    if result:
        return result.group(1)
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
```

## Notes

This tool works best with public Instagram content. Private accounts may require login access through Instaloader.

Please use this tool responsibly and only download content you have permission to access.
