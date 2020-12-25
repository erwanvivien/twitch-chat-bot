import utils

# pace increases rappidly each non 'chaos' / 'order' message
pace = 0.05

# goes from 1s to 4s : time to process all messages
timer = 2.5
MIN = 1
MAX = 4

MAX_PACE = 1


def void():
    # Moves character one up
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print(f"DEBUG: FUNC: void")

    global pace
    pace += 0.01

    if pace > MAX_PACE:
        pace = MAX_PACE


def upward():
    # Moves character one up
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: upward")


def left():
    # Moves character one left
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: left")


def downward():
    # Moves character one down
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: downward")


def right():
    # Moves character one right
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: right")


def inventory():
    # Opens character's inventory
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: inventory")


def enter():
    # Validates current action
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: enter")


def back():
    # Cancels current action
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: back")


def chaos():
    # Drives chat crazy
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: chaos")

    # 1 <= timer <= 4
    global timer
    global pace

    timer -= pace
    pace = 0.05

    timer = timer if timer >= MIN else MIN


def order():
    # Drives chat mentally ok.
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: order")

    # 1 <= timer <= 4
    global timer
    global pace

    timer += pace
    pace = 0.05

    timer = timer if timer <= MAX else MAX
