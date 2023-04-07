import praw
from pytube import YouTube
import requests
import os

from post import Post

reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="app_name",
    username="your_username",
    password="your_password",
)

# I recommend creating some test or mock subreddits for experimenting before attempting to post on public ones
subreddit_name = ""
subreddit = reddit.subreddit(subreddit_name)


# create new comment under the newly created post
def add_comment(new_post, post_details):
    message = new_post.reply(post_details.short_description + "\n\n" + post_details.description)
    print("Added new comment on post, done." + str(message))


def submit_text(post):
    post_title = post.name + ": " + post.pitch

    try:
        created_post = subreddit.submit(post_title, selftext=post.description)
        add_comment(created_post, post)
    except Exception as e:
        print("Can't create text post: ", str(e))


class ImageDownloadError(Exception):
    pass


def download_image(post):
    image_name = "post_image.png"

    try:
        response = requests.get(post.image_url)

        with open(image_name, "wb") as f:
            f.write(response.content)
    except Exception as e:
        raise ImageDownloadError("Error while downloading image") from e

    return image_name


def submit_image(post):
    post_title = post.name + ": " + post.pitch

    image = download_image(post)
    image_path = os.path.realpath(image)

    try:
        subreddit.submit_image(post_title, image_path=image_path)
    except Exception as e:
        print("Can't find image on local path:", str(e))


class VideoDownloadError(Exception):
    pass


def download_video(video_url):
    try:
        # you can optionally specify download(local_path); by default, it will be saved in the same directory as the script
        return YouTube(video_url).streams.filter(file_extension='mp4').first().download()
    except Exception as e:
        raise VideoDownloadError("Error with video download; it might be private") from e


def submit_video(post):
    post_title = post.name + ": " + post.pitch

    try:
        video_path = download_video(post.video_url)
    except VideoDownloadError as e:
        print(str(e))
        return False

    image = download_image(post)
    thumbnail_path = os.path.realpath(image)

    try:
        subreddit.submit_video(post_title, video_path=video_path, thumbnail_path=thumbnail_path)
    except Exception as e:
        print("Error with video upload:", str(e))


def createPost():
    post = Post("", "", "", "", "", "")

    post.name = "MarketRoadie"
    post.pitch = "Get those sweet sweet backlinks"
    post.short_description = "We have created MarketRoadie to help you gain backlinks, improve SEO and market your startup on over 50 startup " \
                             "aggregators out there."
    post.description = "MarketRoadie disseminates information about startups, supplied by the founders themselves, to a variety of startup " \
                       "aggregators. Presently, the platform supports 50 aggregators, primarily websites, with plans to expand to additional venues " \
                       "in the future. The goal is to assist startup founders in promoting their new ventures and increasing awareness. "

    # video and image URLs; you could use local files instead (specifying path to the local file)
    post.video_url = "https://youtu.be/7EVYEQkQikU"
    post.image_url = "https://marketing-images-upload.s3.us-west-2.amazonaws.com/MarketRoadie+About+Us.png"

    return post


if __name__ == '__main__':
    post = createPost()

    # submit video post; you need post title and URL to the video
    # video will start playing automatically when user scrolls to the post
    submit_video(post)

    # submit image post; it will consist of post title and image
    submit_image(post)

    # submit text post; it will consist of post title and the provided text
    submit_text(post)
