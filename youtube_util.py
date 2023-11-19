import re

youtube_url_regex = "^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/.+$"

def is_youtube_url(url):
    return re.match(youtube_url_regex, url) != None
