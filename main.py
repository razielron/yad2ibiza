from bot import Bot
import threading
import time
from threads import Threads
import requests

thread_manager = {'active': True, 'bot': None, 'thread': None}

def build_bots():
    thread_manager['bot'] = Bot()

def print_menu():
    print("press 0 to STOP All Bots and exit")

def build_bot_thread():
    bot = thread_manager['bot']
    thread_manager['thread'] = threading.Thread(target=bot.run, args=(lambda : thread_manager['active'], ))

def stop_all():
    thread_manager['active'] = False

def start():
    build_bots()
    build_bot_thread()
    thread_manager['thread'].start()

    while(thread_manager['active']):
        print_menu()
        user_choise = int(input("Enter your value: \n"))
        if(user_choise == 0): stop_all()

start()