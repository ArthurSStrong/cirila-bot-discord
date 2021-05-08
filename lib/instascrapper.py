import json
import requests
import random

class Instascrapper:
    """Some comment
    In a galaxy far, far away~"""
    def __init__(self, inst_url):
        self.inst_url = inst_url
        self.request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}

    def __scrap(self):

        _list = list()

        page = requests.get(self.inst_url, headers=self.request_headers)

        data = page.text

        start = data.index('_sharedData')

        end = data.index(';</script>')

        json_data = data[start+14:end]

        _list.append(json_data)

        print(f'--------\nPagina Descargada: {self.inst_url  }')

        return _list

    def __get_photos(self, raw_data: str):

        _images = []

        json_data = json.loads(raw_data)

        _content = {}

        for item in json_data['entry_data'].keys():

            if item == 'TagPage':

                _content = json_data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']
            
            elif item == 'ProfilePage':

                _content = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

        for item in _content:
                
            _photo = item['node']['display_url']

            #_shortcode = item['node']['shortcode']
            _images.append(_photo)
        
        return _images


    def get_photo(self):
    
        _j_list = self.__scrap()
        _images = []

        for item in _j_list:
            _list = self.__get_photos(item)
            _images = _images + _list

        if _images:
            return random.choice(_images)
        else:
            return 0
