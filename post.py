from dataclasses import dataclass


@dataclass
class Post:
    name: str
    pitch: str
    short_description: str
    description: str
    image_url: str
    video_url: str
