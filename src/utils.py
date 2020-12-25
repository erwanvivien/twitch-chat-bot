import game
import copy

DEBUG_ALL = False
DEBUG_MSG = False
DEBUG_FCT = True
DEBUG_VALUES = False

# If file 'bruh' contains "Hellor"
# get_content("bruh") returns 'Hellor'


def get_content(file):
    file = open(file, "r")
    res = file.read()
    file.close()
    return res

# :xiaojiba!xiaojiba@xiaojiba.tmi.twitch.tv PRIVMSG #xiaojiba :test
# Extracts "test"
# :xiaojiba!xiaojiba@xiaojiba.tmi.twitch.tv PRIVMSG #xiaojiba :salur : test
# Extracts "salur : test"


def get_message_content(ircstring=None):
    if not ircstring:
        return ""

    # Splits the string on ':' token (see above example)
    fields = ircstring.split(":", 2)

    # Joins a field of string
    s = "".join(fields[2:])
    if DEBUG_ALL or DEBUG_MSG:
        print("DEBUG: MSGB: '" + str(bytes(s, "UTF-8")) + "'")

    # Removes last \r\n
    return s[:-2]


possibilities = {
    "VOID": [0, game.void],

    "Z": [0, game.upward],
    "Q": [0, game.left],
    "S": [0, game.downward],
    "D": [0, game.right],

    "INVENTORY": [0, game.inventory],

    "ENTER":   [0, game.enter],
    "BACK":   [0, game.back],

    "CHAOS": [0, game.chaos],
    "ORDER":   [0, game.order],
}


def reset_current():
    # Every possible word to use in the chat
    # [0] is the current key count - [1] is the associated function

    # resets the current to default
    return copy.deepcopy(possibilities)
