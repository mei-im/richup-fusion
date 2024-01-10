import logging
from game.game import Game

from lists.fusion_list import list_fusion

async def voice_handler(game: Game, command: str):
    # log.info(f"Fusion received: {command}")
    print(f"Fusion received: {command}")

    if command in list_fusion:
        game.fusion(command)
        if command == "ROLL_DICE":
            game.roll_dice()
        elif command == "END_TURN":
            game.end_turn()
        elif command == "BUY_HOUSE":
            game.buy()
        elif command == "GIVE_UP_GAME": # todo melhorar isto
            game.give_up_game()
        elif command == "HELP_GAME_INFO":
            game.help()
        elif command == "ROLL_DICE_BUY_HOUSE":
            game.roll_dice()
            if game.button.buy_house.text.lower() == "buy house":
                game.buy()
            else:
                game.tss("A propriedade já tem dono") 
                
        elif command == "HELP_LIST_OF_COLORS" or command == "LIST_OF_COLORS":
            string_colors = ", ".join(game.available_colors_pt)
            game.tts(f"As cores disponíveis são: {string_colors}")
    else:
        game.tts("Não percebi o comando") # TODO: CREATE A RANDOM FUNCTION
        # log.info(f"Command not found: {gesture}")
        print(f"Command not found: {command}")