import urllib.request
import json


def get_sub_count(channel_id, api_key):
    try:
        data = urllib.request.urlopen(
            f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
        ).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        return int(subs)
    except Exception as e:
        print(f"ERROR: {e}")
        return None
