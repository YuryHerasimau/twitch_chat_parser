# Twitch Chat Parser

A simple Twitch chat message parser.

## Getting Started

### Dependencies

* Python 3, PIP
* emoji
* pandas

### Installing

```
git clone https://github.com/YuryHerasimau/twitch_chat_parser.git
cd ./twitch_chat_parser
python3 -m pip install -r ./requirements.txt
```

Сreate the `settings.ini` file in the config directory of the project with the following keys:

- [Twitch]
- `nickname` = <your_nickname>
- `token` = `<oath token from https://twitchapps.com/tmi/>`
- `server` = irc.chat.twitch.tv
- `port` = 6667
- `channel` = #<name_of_any_channel>

### Executing program

1. Log messages to a file `chat.log`
```
python3 twitch_logger.py
```
2. Stop the script
```
Ctrl + C
```
3. Parse the `chat.log` into a pandas DataFrame to prepare for analysis
```
python3 twitch_parser.py
```