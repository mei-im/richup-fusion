from utils import *
import logging

from game.game import Game
from dictionaries.dictionarys import houses,colors
from lists.intent_list import list_intent

intent_before = ""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
MIN_CONFIDENCE = 0.7
available_colors_pt =["verde lima", "amarela", "laranja", "vermelho", "azul", "ciano", "verde", "castanha", "magenta", "cor de rosa"]



async def voice_handler(game: Game, message:dict):
    global intent_before

    log.info(f"Speak voice received: {message}")
    intent = message["intent"]["name"]
    confidence = message["intent"]["confidence"]

    if intent in list_intent:
        log.info(f"Message received/ intent: {intent} / confidence: {confidence}")
       
        if confidence < MIN_CONFIDENCE:
            game.tts(random_not_understand())
        elif intent == "insert_name":#DONE  
            insert_name_handler(game, message, intent)
        elif intent == "create_room": # DONE
            game.create_game()
            intent_before = intent
        elif intent == "choose_color": # DONE
            choose_color_handler(game, message, intent)
        elif intent == "information_house":
            information_house_handler(game, message, intent)
        elif intent == "start_game": #DONE
            game.start_game()
            intent_before = intent
        elif intent == "roll_dice": #DONE
            game.roll_dice()
            intent_before = intent
        elif intent == "end_turn": #Done
            game.end_turn()
            intent_before = intent
        elif intent == "buy_house": #DONE
            game.buy()
            intent_before = intent
        elif intent == "leave_prison":
            game.leave_prison()
            intent_before = intent
        elif intent == "give_up_game": #DONE
            game.give_up_game()
            intent_before = intent
        elif  intent == "confirm" and "give_up_game" in intent_before: #DONE
            game.confirm_give_up_game()
            game.tts("Podes fechar o jogo, ou continuar a ver o jogo a decorrer.")
            intent_before = intent
        elif  intent == "deny" and "give_up_game" in intent_before: #DONE
            game.cancel_give_up_game()
            intent_before = intent
        elif intent == "close_game":#DONE
            game.tts("Obrigado por jogar Richup")
            game.close()
            global not_quit
            not_quit = False
        elif intent == "list_of_colors": #DONE
            string_colors = ", ".join(available_colors_pt)
            game.tts(f"As cores disponíveis são: {string_colors}")
            intent_before = intent
        elif intent == "game_info": # DONE
            game.help()
            intent_before = intent
        elif intent == "mute": # DONE
            game.mute_func()
            intent_before = intent
        elif intent == "unmute": # DONE
            game.unmute()
            intent_before = intent
        else:
            game.tts(random_not_understand())
            log.info(f"Command not found: {message}")
    else:
        game.tts(random_not_understand())
        log.info(f"Command not found: {message}")

def information_house_handler(game, message, intent):
    global intent_before
    intent_before = intent
    if message["entities"]:
        if len(message["entities"]) > 0:
            house_name = message["entities"][0]["value"].lower()
            if house_name in houses:
                house_name = houses[house_name]
                log.info(f"House name: {house_name}")
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
                log.info(f"Color name: {color_name}")
                game.choose_color(color_name)
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
