import random as r
from imgurpython import ImgurClient
import redis

class Imgur:
    """Some comment
    In a galaxy far, far away~"""
    def __init__(self):

        try:
            redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, charset="utf-8", decode_responses=True)
            client_id = redis_db.get('imgur_client_id')
            client_secret = redis_db.get('imgur_client_secret')

            self.client = ImgurClient(client_id, client_secret)
        except:
            self.client = None

    def get_image(self, *text: str):

        if self.client is not None and text: 
            items = self.client.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='viral', window='all',page=0)
            rand = r.randint(0, len(items)-1)
            return items[rand].link
        else:
            return
