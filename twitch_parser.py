from datetime import datetime
import re
import pandas as pd


def get_chat_dataframe(file):
    data = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n\n\n')
        
        for line in lines:
            # example_msg = '2023-03-13_14:06:28 — :empttydx!empttydx@empttydx.tmi.twitch.tv PRIVMSG #iltw1 :я так и знала'
            try:
                # extract the date and create a datetime object from a string
                time_logged = line.split('—')[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')
                # split the rest of the message, skip the date, and rejoin with an em dash '—' to ensure the message is the same
                username_message = line.split('—')[1:]
                username_message = '—'.join(username_message).strip()
                # each parentheses '(.*)' will capture each of the 3 pieces of info we want to extract from a well-formatted string
                username, channel, message = re.search(
                    ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
                ).groups()

                d = {
                    'dt': time_logged,
                    'channel': channel,
                    'username': username,
                    'message': message
                }

                data.append(d)
            
            except Exception:
                pass
            
    return pd.DataFrame().from_records(data)
        
    
if __name__ == "__main__":
    df = get_chat_dataframe('chat.log')
    df.message.to_csv('messages.csv', index=False)
