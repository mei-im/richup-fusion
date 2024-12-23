from utils import *
import logging
import time

from game.game import Game
from dictionaries.dictionarys import houses,colors
from lists.intent_list import list_intent

intent_before = ""
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# log = logging.getLogger(__name__)
MIN_CONFIDENCE = 0.7

async def voice_handler(game: Game, message:dict):
    global intent_before
    intent = message["intent"]["name"]
    confidence = message["intent"]["confidence"]

    if intent in list_intent:
        # log.info(f"Message received/ intent: {intent} / confidence: {confidence}")
        print(f"Message received/ intent: {intent} / confidence: {confidence}")
       
        if confidence < MIN_CONFIDENCE:
            game.tts(random_not_understand())
        elif intent == "insert_name":   # DONE
            insert_name_handler(game, message, intent)
        elif intent == "create_room": # DONE
            game.create_game()
        elif intent == "choose_color": # NOT USED
            choose_color_handler(game, message, intent)
        elif intent == "information_house": # DONE
            information_house_handler(game, message, intent)
        elif intent == "start_game": # DONE
            game.start_game()
        elif intent == "roll_dice": # NOT USED
            game.roll_dice()
        elif intent == "end_turn": # NOT USED
            game.end_turn()
        elif intent == "buy_house": # NOT USED
            game.buy()
        elif intent == "leave_prison": # DONE
            game.leave_prison()
        elif intent == "give_up_game": # NOT USED
            game.give_up_game()
        elif  intent == "confirm": # DONE
            game.confirm()
        elif  intent == "deny": # DONE
            game.cancel()
        elif intent == "goodbye": # DONE
            game.tts("Adeus, até à próxima.")
            game.close()
            global not_quit
            not_quit = False
        elif intent == "list_of_colors": # NOT USED
            game.help_colors()
        elif intent == "game_info": # NOT USED
            game.help()
        elif intent == "mute": # DONE
            game.mute_func()
        elif intent == "unmute": # DONE
            game.unmute()
        elif intent == "help": # DONE
            game.help()
        elif intent == "change_to_initial_page": #DONE
            game.page_initial()
        elif intent == "greet": # DONE
            game.tts(random_greet())
        elif intent == "close_information" or intent == "close_game": # DONE
            game.close_information()
        else:
            game.tts(random_not_understand())
            # log.info(f"Command not found: {message}")
            print(f"Command not found: {message}")
    else:
        game.tts(random_not_understand())
        # log.info(f"Command not found: {message}")
        print(f"Command not found: {message}")

def information_house_handler(game, message, intent):
    global intent_before
    intent_before = intent
    if message["entities"]:
        if len(message["entities"]) > 0:
            house_name = message["entities"][0]["value"].lower()
            if house_name in houses:
                house_name = houses[house_name]
                game.list_house_information(house_name)
            else:
                game.tts("O jogo não tem essa propriedade")
        else:
            game.tts("Por favor, repita o nome da propriedade")
    else:
        game.tts("Por favor, diz o nome da propriedade")

def choose_color_handler(game, message, intent):
    global intent_before
    intent_before = intent
    if message["entities"]:
        if len(message["entities"]) > 0:
            color_name = message["entities"][0]["value"].lower()
            if color_name in colors:
                color_name = colors[color_name]
                game.choose_color(color_name)
                game.tts(f"Ficaste com a cor {color_name}")
                time.sleep(3)
                game.join_game()
            else:
                game.tts(random_not_valid_color())
        else:
            game.tts(random_not_understand_color())
    else:
        game.tts(random_not_understand_color())

def insert_name_handler(game, message, intent):
    global intent_before
    if message["entities"]:
        if len(message["entities"]) > 0:
            name = message["entities"][0]["value"].lower()
            game.insert_name(name)
        else:
            game.tts(random_not_understand_name())
    else:
        game.tts(random_not_understand_name())
    intent_before = intent