import time
from game.game import Game
from utils import *
from dictionaries.dictionarys import colors
from dictionaries.colors_dic import colors_in_pt

from lists.fusion_list import list_fusion

async def fusion_handler(game: Game, command: str):
    print(f"Fusion received: {command}")

    if command in list_fusion:
        if command == "ROLL_DICE": #DONE
            game.roll_dice()
        elif command == "END_TURN": #DONE
            game.end_turn()
        elif command == "BUY_HOUSE": #DONE
            game.buy()
        elif command == "GIVE_UP_GAME": #DONE
            game.give_up_game()
        elif command == "HELP_GAME_INFO" or command == "GAME_INFO": # DONE
            game.help()
        elif command == "HELP_LIST_OF_COLORS" or command == "LIST_OF_COLORS": # DONE
            game.help_colors()
        elif command == "ROLL_DICE_BUY_HOUSE": #DONE
            roll_dice_and_buy_house(game)
        elif command == "SELECT": # DONE
            hand_front_select_handler(game)
        elif command == "ROLL_DICE_COMPLETED": #DONE
            completed_handler(game)
    elif "CHOOSE_COLOR" in command: #DONE
        choose_color_handler(game, command)
    elif "SELECT_COLOR" in command: #DONE
        select_color_handler(game, command)
    else:
        game.tts("Não percebi o comando")
        print(f"Command not found: {command}")

def roll_dice_and_buy_house(game: Game): 
    game.roll_dice()
    time.sleep(5)
    try:
        game.buy()
    except:
        game.tts("Não tens propriedades para comprar")
    
    time.sleep(3)
    game.tts("Continua a jogar")

def hand_front_select_handler(game):
    if game.button.join_game.text.lower() == "join game":
        game.join_game()
    else:
        name_house = game.name_house
        game.list_house_information(name_house)

def choose_color_handler(game, command):
    command = command.split("_")
    color = command[-1].lower()
    if color in colors:
        color = colors[color]
        game.choose_color(color)
        color = colors_in_pt[color]
        game.tts(f"Selecionaste a cor {color}")
    else:
        game.tts(random_not_valid_color())

def select_color_handler(game, command):
    command = command.split("_")
    color = command[-1].lower()
    if color in colors:
        color = colors[color]
        game.choose_color(color)
        color = colors_in_pt[color]
        game.tts(f"Selecionaste a cor {color}")
        time.sleep(2)
        game.tts("Espera que o entre na sala")
        game.join_game()
    else:
        game.tts(random_not_valid_color())

def completed_handler(game):
    game.roll_dice()
    time.sleep(5)
    try:
        if game.button.buy:
            game.buy()
    except:
        game.tts("Não calhas-te em nenhuma propriedade, que eu possa comprar")
    
    time.sleep(3)
    while True:
        roll_dice_and_buy_house(game)
        if game.button.end_turn:
            game.end_turn()
            break
    game.tts("Não posso fazer mais nada")
    time.sleep(3)
    game.tts("Continua a jogar")
    
    
