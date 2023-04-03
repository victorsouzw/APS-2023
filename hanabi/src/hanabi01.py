from tkinter import *
from tkinter import messagebox, ttk
from tkinter import simpledialog, font
from PIL import ImageTk, Image
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from entities.mesa import Mesa
from Enumerations.StatusPartida import StatusPartida
from Enumerations.TipoDeDica import TipoDeDica
from entities.carta import Carta
from munch import DefaultMunch


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_window = Tk()  # instanciar Tk
        self.board = Mesa()
        self.dog_server_interface = DogActor()
        self.fill_main_window()  # organização e preenchimento da janela
        game_state = self.board.get_estado()
        self.update_gui(game_state)
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
        self.opcao_escolhida = None
        self.main_window.mainloop()  # abrir a janela0

    def fill_main_window(self):
        self.main_window.title("Hanabi")
        self.main_window.geometry("1280x720")
        
        self.discard_pile = Frame(self.main_window, width=200, height=300)
        self.played_cards = Frame(self.main_window, width=500, height=200)
        self.baralho_de_compras = Frame(self.main_window, width=200, height=200)
        self.dicas_e_infracoes = Frame(self.main_window, width=200, height=200)

        self.discard_pile.grid(row=1, column=1)
        self.played_cards.grid(row=1, column=0)
        self.baralho_de_compras.grid(row=0, column=1)
        self.dicas_e_infracoes.grid(row=2, column=1)

        self.menubar = Menu(self.main_window)
        self.menubar.option_add("*tearOff", FALSE)
        self.main_window["menu"] = self.menubar

        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label="File")

        self.menu_file.add_command(label="Iniciar jogo", command=self.start_match)
        self.menu_file.add_command(label="Restaurar estado inicial", command=self.start_game)

    def start_match(self):
        match_status = self.board.get_estado().get_status()
        if match_status == 1:
            answer = messagebox.askyesno("START", "Deseja iniciar uma nova partida?")
            if answer:
                print("im here")
                start_status = self.dog_server_interface.start_match(2)
                code = start_status.get_code()
                message = start_status.get_message()
                if code == "0" or code == "1":
                    messagebox.showinfo(message=message)
                else:  # (code=='2')
                    players = start_status.get_players()
                    local_player_id = start_status.get_local_id()
                    self.board.start_match(players, local_player_id)
                    game_state = self.board.get_estado()
                    self.update_gui(game_state)
                    
                   

    def receive_start(self, start_status):
        self.start_game() 
        players = start_status.get_players()
        local_player_id = start_status.get_local_id()
        self.board.start_match(players, local_player_id)
        game_state = self.board.get_estado()
        self.update_gui(game_state)
        if self.board.jogador_local_inicia():
            self.dog_server_interface.send_move(game_state.get_move_to_send())

    def start_game(self):
        match_status = self.board.get_estado().get_status()
        if match_status == 2 or match_status == 6:
            self.board.reset()
            game_state = self.board.get_estado()
            self.update_gui(game_state)

    
        

    def update_gui(self, game_state):
        
        jogadores = game_state.get_jogadores()

        self.mostrar_cartas_descartadas()
        self.mostrar_cartas_jogadas()
        self.mostra_baralho_compra(game_state)
        self.mostra_dicas_e_infracoes()
        self.mostra_baralho_jogadores(jogadores)
        
    def mostra_baralho_jogadores(self, jogadores):
        self.local_player_hand = Frame(self.main_window, width=550, height=300)
        self.remote_player_hand = Frame(self.main_window, width=550, height=300)
        
        self.remote_player_hand.grid(row=0, column=0)       
        self.local_player_hand.grid(row=2, column=0)
        cartas = ["src/images/red4.png",
                    "src/images/red4.png",
                    "src/images/blue4.png",
                    "src/images/white3.png",
                    "src/images/green1.png"]
        mao_de_cartas = [0 for i in range(5)]
        
        #jogador 1
        for i in range(len(mao_de_cartas)):
            
            
            img = ImageTk.PhotoImage(Image.open("src/images/card.png").resize((125, 200)))
            cartaM = ttk.Button(
                self.local_player_hand,
                image=img,
                padding=5,
                compound='bottom',
                command = lambda : self.selecionar_carta("src/images/card.png")
            )
            cartaM.image = img
            cartaM.pack(side='left', fill='both')  

        #jogador 2
        for i in range(len(mao_de_cartas)):
            
            img = ImageTk.PhotoImage(Image.open(cartas[i]).resize((125, 200)))
            cartaM = ttk.Button(
                self.remote_player_hand,
                image=img,
                padding=5,
                compound='bottom',
                command = lambda : self.selecionar_carta("another path")
            )
            cartaM.image = img
            cartaM.pack(side='left', fill='both')

    #feito
    def mostrar_cartas_descartadas(self):
        titulo_cartas_descartadas = Label(self.discard_pile,
                                          text='Cartas descartadas',
                                          font=font.Font(size=12, weight='bold'))
        titulo_cartas_descartadas.grid(row=0, column=0)

       
        
        

    #feito
    def mostrar_cartas_jogadas(self):
        self.played_cards = Frame(self.main_window, width=100, height=200)
        self.played_cards.grid(row=1, column=0)
               
        cartas_mais_altas = [0 for i in range(5)]

        for carta in cartas_mais_altas:
            img = ImageTk.PhotoImage(Image.open("src/images/cardjogada.png").resize((125, 200)))
            cartaM = ttk.Button(
                self.played_cards,
                image=img,
                padding=5,
                compound='bottom'
            )
            cartaM.image = img
            cartaM.pack(side='left', fill='both')

    #feito
    def mostra_baralho_compra(self, game_state):
        self.baralho_de_compras = Frame(self.main_window, width=200, height=200)
        self.baralho_de_compras.grid(row=0, column=1)
        
        img = ImageTk.PhotoImage(Image.open("src/images/card.png").resize((125, 200)))
        cartaB = ttk.Button(
            self.baralho_de_compras,
            image=img,
            padding=25,
            compound='bottom',
            style='RedCard.TLabel',
            text=str(len(game_state.get_area_compra())),
        )
        cartaB.image = img
        cartaB.pack(side='left', fill='both')

    #feito
    def mostra_dicas_e_infracoes(self):
        numero_total_de_dicas = 8
        self.dicas_e_infracoes = Frame(self.main_window, width=200, height=200)
        self.dicas_e_infracoes.grid(row=2, column=1)
        
        dicas = Frame(self.dicas_e_infracoes)
        dicas.grid(row=0, column=0)

        infracoes = Frame(self.dicas_e_infracoes,)
        infracoes.grid(row=1, column=0)
        
        dicas_restantes = Label(dicas,
                                text='Dicas disponíveis',
                                fg='black',
                                font=font.Font(size=12,),
                                )
        dicas_usadas = Label(dicas,
                                text='Dicas usadas',
                                fg='black',
                                font=font.Font(size=12,)
                                )
        numero_dicas_restantes = Label(dicas,
                                text=str("numero dicas restantes"),
                                fg='black',
                                font=font.Font(size=12,)
                                )
        numero_dicas_usadas = Label(dicas,
                                text=str("numero dicas usadas"),
                                fg='black',
                                font=font.Font(size=12,)
                                )

        infracoes_cometidas = Label(infracoes,
                                    text='Infrações cometidas',
                                    font=font.Font(size=12)
                                    )
        numero_infracoes_cometidas = Label(infracoes,
                                    text=str("numero infracoes"),
                                    fg='red',
                                    font=font.Font(size=12, weight='bold')
                                    )
    
        dicas_restantes.grid(row=0, column=0, padx=5)
        dicas_usadas.grid(row=0, column=1, padx=5)
        numero_dicas_restantes.grid(row=1, column=0, padx=5)
        numero_dicas_usadas.grid(row=1, column=1, padx=5)

        infracoes_cometidas.grid(row=0, column=0, columnspan=2)
        numero_infracoes_cometidas.grid(row=1, column=0, columnspan=2)

   

    #feito
    def popup_dar_dica(self):       
        popup = Toplevel()
        popup.geometry("250x250+350+200")
        popup.resizable(False,False)
        popup.title("Escolha uma dica")
        label = Label(popup, text="Escolha uma dica", font=font.Font(size=12, weight='bold'))
        label.pack(side="top", pady=10)
        button1 = Button(popup, text="Voltar", command=popup.destroy)
        button1.pack(side='bottom', pady=10)
        button2 = Button(popup, text="Cor", command = lambda : print("dica de cor"))
        button2.pack(side='bottom', pady=10)
        button3 = Button(popup, text="Número", command= lambda : print("dica de numero"))
        button3.pack(side='bottom', pady=10)

    #feito
    def clicar_no_botao_de_dica(self, popup):
        popup.destroy()
        
            
            
    #feito
    def popup_jogar_descartar_carta(self):       
        popup = Toplevel()
        popup.geometry("250x250+350+200")
        popup.resizable(False,False)
        popup.title("O que você quer fazer com a carta?")
        label = Label(popup, text="Escolha uma opção:", font=font.Font(size=12, weight='bold'))
        label.pack(side="top", pady=10)
        button1 = Button(popup, text="Voltar", command=popup.destroy)
        button1.pack(side='bottom', pady=10)
        button2 = Button(popup, text="Jogar carta", command = lambda : print("jogou carta"))
        button2.pack(side='bottom', pady=10)
        button3 = Button(popup, text="Descartar carta", command= lambda : print("descartou carta"))
        button3.pack(side='bottom', pady=10)
        
    #feito
    def jogar_carta(self, popup, carta):
        popup.destroy()
        print("estou dentro do jogar carta")
        
        ##feito
    def descartar_carta(self, popup, carta):
        popup.destroy()
        print("estou dentro do descartar carta")
        

    #feito, resolver o board.selecionar_carta que conversa com dog
    def selecionar_carta(self, carta):
        
        if carta != "src/images/card.png":
            print("ESTOU DENTRO DO IF ")
            self.popup_dar_dica()
        else:
            self.popup_jogar_descartar_carta()
            print("ESTOU DENTRO DO ELSE ")
        
            
   