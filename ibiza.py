import json
import requests

class Yad2:
    def __init__(self, params):
        self.params = params
        self.req_base_url = 'https://gw.yad2.co.il/feed-search-legacy/vehicles/private-cars'
        self.all_items = []
        self.item_base_url = 'https://www.yad2.co.il/item/'

    
    def get_items(self):
        # use self.req_base_url and self.params with the GET request
        items = []
        r = requests.get('https://gw.yad2.co.il/feed-search-legacy/vehicles/private-cars?manufacturer=29&model=1625&year=2017-2018&hand=0-1&ownerID=1&forceLdLoad=true')
        jsonData = r.json()
        total_pages = jsonData['data']['feed']['total_pages']
        end_call = '&page=%s&forceLdLoad=true' if total_pages != 1 else '&forceLdLoad=true'

        for i in range(1, total_pages + 1):
            call = 'https://gw.yad2.co.il/feed-search-legacy/vehicles/private-cars?manufacturer=29&model=1625&year=2017-2018&hand=0-1&ownerID=1'
            call += end_call
            print(call)
            r = requests.get(call)
            jsonData = r.json()
            feed_items = jsonData['data']['feed']['feed_items']

            for item in feed_items:
                if('link_token' in item):
                    new_item = {
                        'url': self.item_base_url + item['link_token'],
                        'date_added': item['date_added']
                    }
                    items.append(new_item)

        return items