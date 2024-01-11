import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from utils import *
from game.mapping import Buttons, Inputs, Houses, Colors
from dictionaries.colors_dic import colors_in_pt, colors_map_values
from dictionaries.houses_dic import houses_number
from selenium.webdriver.common.by import By

GAME_INFO = """O RichUp é a adaptação do clássico jogo de tabuleiro que combina estratégia e negociação. 
            Cada jogador começa com dinheiro e escolhe uma cor para representá-lo no tabuleiro. 
            O objetivo é adquirir propriedades, construir casas e hotéis, e cobrar aluguer dos adversários.
            Durante o jogo, os jogadores negociam entre si, podem comprar, vender e trocar propriedades. 
            O vencedor é o último jogador que não vai à falência. Para ganhar, é essencial tomar decisões financeiras inteligentes, formar alianças e gerir recursos com sabedoria. 
            Boa sorte!"""

available_colors_pt =["verde lima", "amarela", "laranja", "vermelho", "azul", "ciano", "verde", "castanha", "magenta", "cor de rosa"]

class Game:
    def __init__(self, TTS) -> None:
        self.name_house = None
        self.browser = Firefox()
        self.browser.get('https://richup.io/')
        self.browser.maximize_window()
        self.mute = False
        self.tts_func = TTS
        self.tts = TTS
        self.tts("Bem vindo ao Monopoly online, um jogo de tabuleiro para toda a família e amigos")
        self.button = Buttons(self.browser)
        self.input = Inputs(self.browser)
        self.house = Houses(self.browser)
        self.colors = Colors(self.browser)
        time.sleep(4)
        self.button.accept_cookies.click()
        time.sleep(2)
        self.tts("Para começar, podes inserir o teu nome. E criar uma sala para ti e para os teus amigos")

    def get_url(self):
        return self.browser.current_url
      
    def insert_name(self, name): #DONE
        try:
            if self.input.name.get_attribute("value") != "":
                self.input.name.clear()
            self.input.name.send_keys(name)
            self.tts("O teu nome no jogo é " + self.input.name.get_attribute("value"))
            time.sleep(3)
            self.tts("Se ainda não tens uma sala, podes criar uma sala para ti e para os teus amigos")
        except:
            self.tts(random_not_auth_insert_name())

    def create_game(self): # DONE
        try: 
            if self.button.create_private_game:
                if self.input.name.get_attribute("value") == "":
                    self.tts("Como não inseriste nenhum nome, vou criar um nome aleatório para ti")
                    self.button.randomize_name.click()
                    self.tts("O teu nome no jogo é " + self.input.name.get_attribute("value"))
                self.tts("A criar uma sala!")
                time.sleep(1)
                self.button.create_private_game.click()
                self.tts("Escolha a cor com que quer jogar")
            else:
                self.tts(random_not_create_room())
        except:
            self.tts(random_not_create_room())

    def choose_color(self, color): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try: 
            if self.button.join_game_after_color.text.lower() == 'join game':
                name_color = colors_in_pt[color]
                color = self.colors.__getattribute__(color)
                color.click()
                self.tts(f"Ficaste com a cor {name_color}")
                time.sleep(3)
                self.join_game()
            else:
                self.tts("Não é permitido mudar de cor, neste momento")
                
        except:
            self.tts("Não é permitido mudares ou escolheres a cor, enquanto não estás numa sala ou num jogo a decorrer")

    def start_game(self): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try:
            if self.button.enable_bots:
                self.button.enable_bots.click()
            time.sleep(3)
            self.tts("Aguarde enquanto os jogadores entram na sala")
            time.sleep(3)
            if self.button.start_game.text.lower() == 'start game':
                self.button.start_game.click()
                self.tts(random_start_game())
        except:
            try:
                if self.button.join_game_after_color.text.lower() == 'join game':
                    self.tts("Precisa de entrar na sala para poder jogar")
                else:
                    self.tts(random_start_game_not_auth())
            except:
                self.tts(random_start_game_not_auth())

    def leave_prison(self): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        
        try:
            if 'get free' in self.button.prison_pay.text.lower():
                self.button.prison_pay.click()
                self.tts("Pagaste para sair da prisão")
            else:
                self.tts("Não estás na prisão")
        except:
            self.tts("Não é permitido, sair da prisão neste momento")

    def confirm(self): # DONE
        try:
            self.button.confirm_bankrupt.click()
            self.tts(random_give_up_confirm())
            time.sleep(3)
            self.tts("Podes fechar o jogo, ou continuar a ver o jogo a decorrer.")
        except:
            try:
                self.button.confirm_trade.click()
                self.tts("A negociação foi aceite")
            except:
                self.tts("Não tem nenhuma informação para confirmar")

    def cancel(self): # DONE
        try:
            self.button.cancel_bankrupt.click()
            self.tts(random_give_up_cancel())
        except:
            try:
                self.button.cancel_trade.click()
                self.tts("A negociação não foi aceite")
            except:
                self.tts("Não tem nenhuma informação para cancelar")

    def close(self):  # DONE
        self.browser.close()

    def mute_func(self): # DONE
        def do_nothing(message):
            pass
        if self.mute:
            self.tts("O som já está desativado")
            return
        self.tts("O jogo vai ser silenciado, para voltar a ouvir o jogo, peça para sair do modo silencioso")
        self.button.mute.click()
        self.mute = True
        time.sleep(3)
        self.tts = do_nothing

    def unmute(self): #DONE 
        if not self.mute:
            self.tts("O som não está desativado")
            return
        self.button.unmute.click()
        self.mute = False
        self.tts = self.tts_func
        time.sleep(3)
        self.tts("O jogo já não está silenciado")

    def list_house_information(self,house_name): #DONE

        if self.get_url() == "https://richup.io/":
            self.tts("Precisas de entrar numa sala para acessar ao tabuleiro do jogo")
            return
        
        if self.name_house != house_name:
            self.activate_house(house_name)
            time.sleep(3)
        
        house = self.house.__getattribute__(house_name)
        house.click()
        self.tts(f"Já consegues ver a informação da propriedade {house_name}")
        time.sleep(5)
        house.click()
        self.tts("A informação da propriedade foi minimizada")

    def change_color_number(self, number:int, increase:bool): #DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try:
            if self.button.join_game_after_color.text.lower() == 'join game':
                color_number_activate = self.get_color_activate()
                if color_number_activate != 0:
                    if increase:
                        color_number = color_number_activate + number
                    else:
                        color_number = color_number_activate - number

                    if color_number == 0:
                        color_number = 12
                    elif color_number == 13:
                        color_number = 1
                    self.tts(random_frase_color(colors_in_pt[colors_map_values[color_number]]))
                    self.colors.__getattribute__(colors_map_values[color_number]).click()
                else:   
                    self.tts("Não tem nenhuma cor disponível")
            else:
                self.tts("Não é permitido escolheres a cor, neste momento")
        except:
            self.tts("Não é permitido, mudar de cor neste momento")

    def get_color_activate(self)->int: #DONE
        color_number = -1
        for i in range(1,13):
            try:
                button = self.browser.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[{i}]")
            except:
                button = self.browser.find_element(By.XPATH, f"/html/body/div[3]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[{i}]")
            if not button.is_enabled():
                return i
        return color_number

    def get_activate_house(self): #DONE
        for i in range(len(houses_number)):
            div_element = self.house.__getattribute__(houses_number[i])
            if div_element.get_attribute("style") == "border: 4px solid red;":
                self.name_house = houses_number[i]
                return i
        return -1
    
    def activate_house(self, name_house:str): #DONE
        current_house = self.get_activate_house()
        if current_house != -1:
            div_element = self.house.__getattribute__(houses_number[current_house])
            self.browser.execute_script("arguments[0].style.border='0px'", div_element)

        div_element = self.house.__getattribute__(name_house)
        self.browser.execute_script("arguments[0].style.border='4px solid red'", div_element)
        self.name_house = name_house
            
    def house_handler(self, number:int, increase:bool): #DONE
        current_house = self.get_activate_house()
        if increase:
            current_house += number
        else:
            current_house -= number

        if current_house == -1:
            current_house = len(houses_number) - 1
        elif current_house == len(houses_number):
            current_house = 0

        name_house = houses_number[current_house]
        self.activate_house(name_house)
        
    def help(self):  # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try:
            self.button.help.click()
            self.tts("A informação do Jogo foi aberta")
            time.sleep(3)
            self.tts(GAME_INFO)
            time.sleep(30)
            try:
                self.button.close_help.click()
                self.tts("A informação do Jogo foi fechada")
            except:
                self.tts("Não é permitido, aceder à ajuda neste momento")
        except:
            self.tts("Não é permitido, aceder à ajuda neste momento")

    def give_up_game(self): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try: 
            self.button.bankrupt.click()
            time.sleep(1)
            self.tts("Tem a certeza que quer desistir do jogo?")
        except:
            self.tts(random_give_up_not_in_game())

    def join_game(self):  # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try:
            if self.button.join_game_after_color.text.lower() == 'join game':
                self.tts("Espera que entre na sala")
                time.sleep(3)
                self.button.join_game_after_color.click()
                time.sleep(3)
                self.tts("Bem vindo ao sua sala")
                time.sleep(2)
                if self.button.join_game.text.lower() != 'join game':
                    self.activate_house(houses_number[0])
            else:
                self.tts("Não é permitido entrar na sala, neste momento")
        except:
            self.tts("Não é permitido entrar na sala, enquanto não estás numa sala ou num jogo a decorrer")

    def end_turn(self): #DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        
        try: 
            if self.button.end_turn.text == 'End turn':
                self.button.end_turn.click()
                self.tts(random_end_turn())
            elif self.button.roll_dice.text.lower() == 'start game':
                self.tts("Precisa de começar o jogo para poder jogar")
            else:
                self.tts(random_end_turn_not_auth())
        except:
            try:
                if self.button.join_game_after_color.text.lower() == 'join game':
                    self.tts("Precisa de entrar na sala para poder jogar")
                else:
                    self.tts(random_end_turn_not_auth())
            except:
                self.tts(random_end_turn_other_player())

    def roll_dice(self): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try: 
            if self.button.roll_dice.text.lower() == 'roll the dice' or \
                self.button.roll_dice.text.lower() == 'roll again':
                self.button.roll_dice.click()
                self.tts(random_roll_dice())
            elif self.button.roll_dice.text.lower() == 'start game':
                self.tts("Precisa de começar o jogo para poder jogar")
            else:
                self.tts(random_roll_dice_in_turn())
        except: 
            try:
                if self.button.join_game_after_color.text.lower() == 'join game':
                    self.tts("Precisa de entrar na sala para poder jogar")
                else:
                    self.tts(random_roll_dice_not_auth())
            except:
                self.tts(random_roll_dice_not_auth())

    def buy(self): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return

        try:
            if "Buy" in self.button.buy.text:
                self.button.buy.click()
                self.tts(random_buy_house())
            else:
                self.tts(random_buy_house_not_auth())
        except:
            try:
                if self.button.roll_dice.text.lower() == 'roll the dice' or \
                    self.button.roll_dice.text.lower() == 'roll again' or \
                    self.button.roll_dice.text.lower() == 'end turn':
                    self.tts(random_buy_house_not_auth())
                else:
                    self.tts(random_buy_house_not_in_game())
            except:
                self.tts(random_buy_house_not_in_game())

    def help_colors(self): # DONE
        string_colors = ", ".join(available_colors_pt)
        self.tts(f"As cores disponíveis são: {string_colors}")

    def page_initial(self): #DONE
        if self.get_url() == "https://richup.io/":
            self.tts("Já te encontras na página inicial")
            return
        self.browser.get('https://richup.io/')
        time.sleep(2)
        self.tts("Já podes começar um novo jogo")

    def close_information(self): #DONE
        try:
            self.button.close_help.click()
            self.tts("A informação do Jogo foi fechada")
        except:
            try:
                self.button.close_bankrupt.click()
                self.tts("A janela de desistir do jogo foi fechada. Pode continuar a jogar")
            except:
                try:
                    self.button.close_trade.click()
                    self.tts("A janela de negociação foi fechada. Pode continuar a jogar")
                except:
                    self.tts("Não tens nenhuma janela aberta")


        
