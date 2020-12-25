import utils

# pace increases rappidly each non 'chaos' / 'order' message
pace = 0.05

# goes from 1s to 4s : time to process all messages
timer = 2.5


def update_pace():
    global pace
    pace += 0.01

    if pace > 1:
        pace = 1


def void():
    # Moves character one up
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print(f"DEBUG: FUNC: void")

    update_pace()


def upward():
    # Moves character one up
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: upward")

    update_pace()


def left():
    # Moves character one left
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: left")

    update_pace()


def downward():
    # Moves character one down
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: downward")

    update_pace()


def right():
    # Moves character one right
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: right")

    update_pace()


def inventory():
    # Opens character's inventory
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: inventory")

    update_pace()


def enter():
    # Validates current action
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: enter")

    update_pace()


def back():
    # Cancels current action
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: back")

    update_pace()


def chaos():
    # Drives chat crazy
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: chaos")

    # 1 <= timer <= 4
    global timer
    global pace

    timer -= pace
    pace = 0.05

    timer = timer if timer >= 1 else 1


def order():
    # Drives chat mentally ok.
    if utils.DEBUG_ALL or utils.DEBUG_FCT:
        print("DEBUG: FUNC: order")

    # 1 <= timer <= 4
    global timer
    global pace

    timer += pace
    pace = 0.05

    timer = timer if timer <= 4 else 4

# def forward():
#     pass


# def forward():
#     pass
