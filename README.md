# Create reddit post

PRAW (Python Reddit API Wrapper) is a Python package that simplifies interacting with the Reddit API.
Here, I will cover how to make API calls to submit videos, images, and text posts using PRAW.

<p align="center">
    <img alt="Reddit logo" width="300px" src="./.github/assets/reddit-logo.jpeg" />
</p>

## Requirements

1. Python 3.x
2. PRAW: Install using `pip install praw`
3. A Reddit account and a registered app on Reddit: https://www.reddit.com/prefs/apps
    - Select "script" for the type of app
    - Choose the name of the app
    - Set the redirect URL to https://placeholder.com/
    - Note down the client ID and secret

## Setup

1. Clone this repository and navigate to the project directory.
2. Import PRAW and authenticate with Reddit by supplying your credentials:

```python
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="app_name",
    username="your_username",
    password="your_password",
)   
```

Replace the placeholders with your actual credentials.

Specify `subreddit_name = ""`; I recommend creating some test or mock subreddits for experimenting before attempting to post on public ones.

### After submitting a video post

<p align="center">
    <img alt="Reddit video post" width="300px" src="./.github/assets/video_example.png" />
</p>

### After submitting a image post

<p align="center">
    <img alt="Reddit image post" width="300px" src="./.github/assets/image_example.png" />
</p>

### After submitting a text post (with comment)

<p align="center">
    <img alt="Reddit text post" width="300px" src="./.github/assets/text_example.png" />
</p>

<p align="center">
    <img alt="Reddit comment" width="300px" src="./.github/assets/comment_example.png" />
</p>

## Documentation

For more information on using PRAW and the Reddit API, please refer to the official PRAW
documentation: https://praw.readthedocs.io/en/stable/

