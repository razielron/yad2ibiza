# yad2ibiza

## Project Explanation:
With this project you can get an automated push notifications to your phone regarding ads at Yad 2.
Everytime there's a new ad you searched for at Yad 2 you will know about it right away.
For now, it searches for something specific - Seat Ibiza between the years 2016-2018 and more filters.
Later, I'll add a config file to make a dynamic search and be useful for more people.

## init:
1. clone the project
2. download python 3 (doesn't matter which specific version)
3. run this command: `pip install -r requirements.txt`

## config:
1. open on your browser https://www.pushbullet.com/
2. create an account
3. download the app pushbullet
4. connect your device and login, enable push notifications
5. on your pc - login to pushbullet
6. open settings
7. press 'Create Access Token'
8. Copy that token
9. go to the file 'notifications.py'
10. paste that token in the cunstructor's field 'self.access_token'
11. run 'main.py'
