import configparser

config = configparser.ConfigParser()
config.read('config/settings.ini')

"""
Get token here: https://twitchapps.com/tmi/
"""

NICKNAME = config["Twitch"]["nickname"]
TOKEN = config["Twitch"]["token"]
SERVER = config["Twitch"]["server"]
PORT = int(config["Twitch"]["port"])
CHANNEL = config["Twitch"]["channel"]