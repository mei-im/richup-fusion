import json
from os import system
import xml.etree.ElementTree as ET
import ssl
import websockets
from function_gesture_handler import gesture_handler
from function_voice_handler import voice_handler

from game.game import Game
from tts import TTS

HOST = "127.0.0.1"
not_quit = True


async def message_handler(game: Game, message:str):
    message, status = process_message(message)
    if message == "OK" and status == None:
        return "OK"
    elif status == "voice":
        await voice_handler(game=game, message=message)
    elif status == "gesture":
        await gesture_handler(game=game, gesture=message)
    else:
        return "OK"


def process_message(message):
    if message == "OK":
        return "OK", None
    else:
        json_command = ET.fromstring(message).find(".//command").text
        print(f"Json command: {json_command}")
        if "recognized" in json_command:
            gesture = json.loads(json_command)
            return gesture, "gesture"
        elif "nlu" in json_command:
            command = json.loads(json_command)["nlu"]
            command = json.loads(command)
            return command, "voice"
        else:
            return "OK", None
    
async def main():
    tts = TTS(FusionAdd=f"https://{HOST}:8000/IM/USER1/APPSPEECH").sendToVoice
    game = Game(TTS=tts)
    mmi_cli_out_add = f"wss://{HOST}:8005/IM/USER1/APP"

    #SSL config 
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Connect to websocket
    
    async with websockets.connect(mmi_cli_out_add, ssl=ssl_context) as websocket:
        print("Connected to MMI CLI OUT")
                
        while not_quit:
            try:
                msg = await websocket.recv()
                await message_handler(game=game, message=msg)
            except Exception as e:
                tts("Ocorreu um erro, a fechar o jogo")
                print(f"Error: {e}")
        
        print("Closing connection")
        await websocket.close()
        print("Connection closed")
        exit(0)
    


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())