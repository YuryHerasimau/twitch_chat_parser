import config.config as config
import socket
import logging
from emoji import demojize


def log():
    # use logging library to log messages to a file
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s — %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

    # instantiate a socket to establish a connection to Twitch IRC
    sock = socket.socket()
    # connect this socket to Twitch
    sock.connect((config.SERVER, config.PORT))
    # send your token and nickname for authentication and the channel to connect to over the socket
    # don't forget to encode the string into bytes which allows it to be sent over the socket
    sock.send(f"PASS {config.TOKEN}\n".encode('utf-8'))
    sock.send(f"NICK {config.NICKNAME}\n".encode('utf-8'))
    sock.send(f"JOIN {config.CHANNEL}\n".encode('utf-8'))

    try:
        while True:
            # check for new messages from the socket
            resp = sock.recv(2048).decode('utf-8')
            # send "PONG" in response to confirm the use of a socket connection
            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            # log messages with emojis mapped to their meaning in words
            elif len(resp) > 0:
                logging.info(demojize(resp))

    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == "__main__":
    log()
