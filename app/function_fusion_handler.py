import logging
import time
from game.game import Game

from lists.fusion_list import list_fusion

async def fusion_handler(game: Game, command: str):
    # log.info(f"Fusion received: {command}")
    print(f"Fusion received: {command}")

    if command in list_fusion:
        if command == "ROLL_DICE":
            game.roll_dice()
        elif command == "END_TURN":
            game.end_turn()
        elif command == "BUY_HOUSE":
            game.buy()
        elif command == "GIVE_UP_GAME":
            game.give_up_game()
        elif command == "HELP_GAME_INFO" or command == "GAME_INFO":
            game.help()
        elif command == "HELP_LIST_OF_COLORS" or command == "LIST_OF_COLORS":
            game.help_colors()
        elif command == "ROLL_DICE_BUY_HOUSE":
            roll_dice_and_buy_house(game)
        elif command == "COMPLETED_TURN":
            # TODO: IMPLEMENTAR
            game.tss("Ainda não implementado")
    else:
        game.tts("Não percebi o comando") # TODO: CREATE A RANDOM FUNCTION
        # log.info(f"Command not found: {gesture}")
        print(f"Command not found: {command}")

def roll_dice_and_buy_house(game: Game):
    game.roll_dice()
    time.sleep(3)
    if "Buy" in game.button.buy.text():
        game.buy()
    elif "get free" in game.button.leave_prison.text().lower():
        game.tss("Estas na prisão, não podes comprar casas")
    elif "roll" in  game.button.roll_dice.text().lower():
        game.tss("Ainda podes voltar a lançar os dados")
    elif "end" in game.button.end_turn.text().lower():
        game.tss("Estas numa casa que não podes comprar")
    else:
        game.tss("Não podes comprar casas neste momento")