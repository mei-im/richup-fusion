import logging
from game.game import Game
from lists.gestures_list import list_gesture

from utils import random_not_understand, random_not_understand_the_gesture

MIN_CONFIDENCE = 0.7
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# log = logging.getLogger(__name__)

async def gesture_handler(game: Game, gesture:str):
    # log.info(f"Gesture received: {gesture}")
    print(f"Gesture received: {gesture}")
    name_of_gesture = gesture["recognized"][1]
    confidence = float(gesture["confidence"].replace(",", "."))

    if confidence < MIN_CONFIDENCE:
        game.tts(random_not_understand())
    elif name_of_gesture in list_gesture:
        if name_of_gesture == "HANDRIGHTUPHELP": # not used
            game.help()
        elif name_of_gesture == "HANDSUPGIVEUP": # not used
            game.give_up_game()
        elif name_of_gesture == "HANDSFRONTSELECT":
            hand_front_select_handler(game)
        elif name_of_gesture == "HANDLEFTSHOULDERLEVELDECREASE":
            hand_left_shoulder_decrease_handler(game)
        elif name_of_gesture == "HANDRIGHTSHOULDERLEVELINCREASE":
            hand_right_shoulder_increase_handler(game)
        elif name_of_gesture == "HANDSDIFFERENTDIRECTIONSCLOSE":    # not used
            game.end_turn()
        elif name_of_gesture == "HANDONEDIRECTIONROLLDICE": # not used
            game.roll_dice()
        elif name_of_gesture == "HANDSJOIN": # not used
            game.buy()
    else:
        game.tts(random_not_understand_the_gesture())
        # log.info(f"Command not found: {gesture}")
        print(f"Command not found: {gesture}")

def hand_right_shoulder_increase_handler(game):
    if game.button.join_game.text.lower() == "join game":
        game.change_color_number(number=1, increase=True)
    else:
        game.house_activate(number=1, increase=True)

def hand_left_shoulder_decrease_handler(game):
    if game.button.join_game.text.lower() == "join game":
        game.change_color_number(number=1, increase=False)
    else:
        game.house_activate(number=1, increase=False)

def hand_front_select_handler(game):
    if game.button.join_game.text.lower() == "join game":
        game.join_game()
        if game.button.join_game.text.lower() != "join game":
            game.house_activate(number=1, increase=True)
    else:
        name_house = game.name_house
        game.list_house_information(name_house)