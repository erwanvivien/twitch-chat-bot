import socket
import sys
import time
import datetime
import select

from utils import get_content, get_message_content, reset_current, \
    DEBUG_ALL, DEBUG_FCT, DEBUG_MSG, DEBUG_VALUES
import game

# this never changes => server, port
server = "irc.chat.twitch.tv"
port = 6667

# update this to change stream
channel = "#xiaojiba"

# Update this to change the name (kinda useless, will talk in your name)
botUsername = "EMU_DS_chat_bot"

# Get this from https://twitchapps.com/tmi/ - keep 'oauth:' in the file
password = get_content("irc_pass")


class IRC:
    # Taken from 'https://www.techbeamers.com/create-python-irc-bot/'
    irc = socket.socket()

    def __init__(self):
        # Creates a socket (the tunnel we'll use to talk to twitch)
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        # Transfer data
        if DEBUG_ALL or DEBUG_MSG:
            print(f"DEBUG: SENT: '{msg}'")

        # ':' after channel if mandatory to send more than one word
        self.irc.send(bytes(f"PRIVMSG {channel} :{msg}\n", "UTF-8"))

    def connect(self, server, port, channel, botnick, authpass):
        # Connect to the server
        print("IRC: Connecting to: " + server)
        self.irc.connect((server, port))

        # Perform user authentication
        self.irc.send(bytes("USER " + botnick + " " + botnick +
                            " " + botnick + " :python\n", "UTF-8"))
        self.irc.send(bytes("PASS " + authpass + "\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        print(f"IRC: Sent credentials for {botnick} bot")

        # Update sleep timing if too fast for your computer (5 is good)
        time.sleep(2)

        # Join the channel
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
        print(f"IRC: Joined {channel}")
        print("---------------------------------------------------------")
        print("")

    def get_response(self):
        # Select checks if buffer is empty or not
        # makes this function non-blocking
        ready = select.select([self.irc], [], [], 1)

        # If no buffer inside pipe, we just return empty string
        if not ready[0]:
            return ""

        # If message is a PING we send a PONG
        resp = self.irc.recv(2040).decode("UTF-8")
        if resp.find('PING') != -1:
            self.irc.send(
                bytes('PONG ' + resp.split(':')[1] + '\r\n', "UTF-8"))

        # We return the response anyway
        return resp


current = reset_current()

# Connection to chat
irc = IRC()
irc.connect(server, port, channel, botUsername, password)

last = datetime.datetime.now()

# Loop that reads every message in {channel}'s person default chat
while True:
    text = irc.get_response()
    if DEBUG_ALL or DEBUG_MSG:
        print(f"DEBUG: RCVD: '{text[:-2]}'")  # Debug only

    # Checks if it's a message from chat
    if "PRIVMSG" in text and channel in text:
        # Check `get_message_content` to see what it does
        content = get_message_content(text)
        if DEBUG_ALL or DEBUG_MSG:
            print(f"DEBUG: MSGC: '{content}'")
        content = content.upper()

        # Checks if it's known possibility
        if content in current:
            current[content][0] += 1
            if DEBUG_ALL or DEBUG_FCT:
                print(f"{content} is now {current[content][0]}")

    # Does stuff when at least `game.timer` seconds has passed
    if last + datetime.timedelta(seconds=game.timer) < datetime.datetime.now():
        if DEBUG_ALL or DEBUG_VALUES:
            print(f"current timer: {game.timer} - current pace: {game.pace}")

        # searches in the dictionnary see `current` the max used
        action = current["VOID"]
        for elt in current.values():
            if elt[0] > action[0]:
                action = elt

        # Executes top action
        action[1]()

        if DEBUG_ALL or DEBUG_VALUES:
            print(current)

        # Resets one time use variables
        current = reset_current()
        last = datetime.datetime.now()
