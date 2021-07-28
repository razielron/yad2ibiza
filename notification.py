import json
import requests
from pushbullet import Pushbullet

class Push_bullet_app:
    def __init__(self):
        self.access_token = ''
        self.pb = Pushbullet(self.access_token)

    def pushNotification(self, text):
        push = self.pb.push_note('New Links: ', text)