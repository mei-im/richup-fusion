import json
from os import system
import time
import xml.etree.ElementTree as ET
import ssl
import websockets
from utils import *


from game.game import Game
from dictionaries.dictionarys import houses,colors
from lists.intent_list import list_intent

intent_before = ""

async def voice_handler(game: Game, message:str):
    global intent_before
    print(f"Speak voice received: {message}")
    if message["intent"]["name"] in list_intent:
        print(f"Message received/ intent: {message['intent']['name']}")
        intent = message["intent"]["name"]
        if message["intent"]["confidence"] < 0.7:
            game.tts(random_not_understand())
        elif intent == "insert_name":#DONE  
            if message["entities"]:
                if len(message["entities"]) > 0:
                    name = message["entities"][0]["value"].lower()
                    game.insert_name(name)
                else:
                    game.tts(random_not_understand_name())
            else:
                game.tts(random_not_understand_name())
            intent_before = intent
        elif intent == "create_room": # DONE
            game.create_game()
            intent_before = intent
        elif intent == "choose_color": # DONE
            intent_before = intent
            if message["entities"]:
                if len(message["entities"]) > 0:
                    color_name = message["entities"][0]["value"].lower()
                    if color_name in colors:
                        color_name = colors[color_name]
                        print(f"Color name: {color_name}")
                        game.choose_color(color_name)
                    else:
                        game.tts(random_not_valid_color())
                else:
                    game.tts(random_not_understand_color())
            else:
                game.tts(random_not_understand_color())
        elif intent == "information_house":
            intent_before = intent
            if message["entities"]:
                if len(message["entities"]) > 0:
                    house_name = message["entities"][0]["value"].lower()
                    if house_name in houses:
                        house_name = houses[house_name]
                        print(f"House name: {house_name}")
                        game.list_house_information(house_name)
                    else:
                        game.tts("O jogo não tem essa propriedade")
                else:
                    game.tts("Por favor, repita o nome da propriedade")
            else:
                game.tts("Por favor, diz o nome da propriedade")
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
            colors_in_pt =["verde lima", "amarela", "laranja", "vermelho", "azul", "ciano", "verde", "castanha", "magenta", "cor de rosa"]
            string_colors = ", ".join(colors_in_pt)
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
            print(f"Command not found: {message}")
    else:
        game.tts(random_not_understand())
        print(f"Command not found: {message}")
