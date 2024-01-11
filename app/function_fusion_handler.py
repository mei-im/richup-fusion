import logging
import time
from game.game import Game

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
            # TODO: IMPLEMENTAR
            game.tss("Ainda não implementado")
        elif command == "INITIALIZATION_GAME": 
            # TODO: IMPLEMENTAR
            game.tss("Ainda não implementado")
    else:
        game.tts("Não percebi o comando") # TODO: CREATE A RANDOM FUNCTION
        # log.info(f"Command not found: {gesture}")
        print(f"Command not found: {command}")


# TODO: FUNCTION TO IMPLEMENT
def roll_dice_and_buy_house(game: Game): 
    game.roll_dice()
    time.sleep(5)
    print("AQUI")
    if "buy" in game.button.buy.text().lower():
        print("AQUI2")
        game.buy()
    # elif "get free" in game.button.prison_pay.text().lower():
    #     game.tts("Estas na prisão, não podes comprar casas")
    elif "roll" in  game.button.roll_dice.text().lower():
        print("AQUI3")
        game.tts("Ainda podes voltar a lançar os dados")
    elif "end" in game.button.end_turn.text().lower():
        print("AQUI4")
        game.tts("Estas numa casa que não podes comprar")
    else:
        print("AQUI5")
        game.tts("Não podes comprar casas neste momento")