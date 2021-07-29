from ibiza import Yad2
import time
import winsound
from notification import Push_bullet_app

frequency = 500  # Set Frequency To 2500 Hertz
duration = 1100  # Set Duration To 1000 ms == 1 second

def make_beep(beep):
    if(beep):
        for i in range(2):
            winsound.Beep(frequency, duration)
            time.sleep(0.5 * (i + 1))
        
        winsound.Beep(frequency, duration * 2)

class Bot(Yad2):
    def __init__(self):
        Yad2.__init__(self, None)
        self.pb = Push_bullet_app()

    def combine_and_remove_duplicates(self, arr1, arr2):
        for x in arr1:
            for y in arr2:
                if(x['url'] == y['url']):
                    arr2.remove(y)

        arr3 = sorted(arr1 + arr2, key=lambda x: x['date_added'])
        return arr1 + arr2

    def get_new_items(self, arr1, arr2):
        arr3 = []

        for x in arr1:
            is_exist = False
            for y in arr2:
                if(x['url'] == y['url']):
                    is_exist = True
                
            if (not is_exist):
                arr3.append(x)

        arr3 = sorted(arr3, key=lambda x: x['date_added'])
        return arr3

    def join_perfect(self, arr):
        text = '-%d New Items-' %len(arr)
        for item in arr:
            text += '\n' + item['url'] + '\n' + 'Added at: ' + item['date_added']
        text += '\n-%d New Items-' %len(arr)
        return text

    def check_new_items(self, current_list):
        new_items = self.get_new_items(current_list, self.all_items)
        self.all_items = self.combine_and_remove_duplicates(self.all_items, current_list)
        if(len(new_items) > 0):
            # print(new_items)
            # print(len(self.all_items))
            text = self.join_perfect(new_items)
            self.pb.pushNotification(text)
            print('-%d New Items-' %len(new_items))
        else:
            print('-Nothing New-')

    def run(self, keep_run_func):
        interval_time = 60 * 5 #seconds

        while(keep_run_func()):
            current_list = self.get_items()
            self.check_new_items(current_list)
            print('##################################################')
            time.sleep(interval_time)