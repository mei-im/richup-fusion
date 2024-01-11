import logging
import time
from game.game import Game
from utils import *

from lists.fusion_list import list_fusion

async def fusion_handler(game: Game, command: str):
    # log.info(f"Fusion received: {command}")
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
        elif command == "COMPLETED_TURN":
            game.tss("Ainda não implementado")
        elif command == "INITIALIZATION_GAME": 
            game.tss("Ainda não implementado")
    else:
        game.tts("Não percebi o comando") # TODO: CREATE A RANDOM FUNCTION
        # log.info(f"Command not found: {gesture}")
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