from tkinter import *
from tkinter import messagebox, ttk
from tkinter import simpledialog, font
from PIL import ImageTk, Image


class PlayerInterface():
    def __init__(self):
        self.main_window = Tk()  # instanciar Tk
        
        self.fill_main_window()  # organização e preenchimento da janela

        self.preenche_tela()
        
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        print("nome do jogador: " + player_name)
        
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

        self.menu_file.add_command(label="Iniciar jogo")
        self.menu_file.add_command(label="Restaurar estado inicial")
        

    def preenche_tela(self):
        self.mostrar_cartas_descartadas()
        self.mostrar_cartas_jogadas()
        self.mostra_baralho_compra()
        self.mostra_dicas_e_infracoes()
        self.mostra_baralho_jogadores()
        
    def mostra_baralho_jogadores(self):
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
    def mostra_baralho_compra(self):
        self.baralho_de_compras = Frame(self.main_window, width=200, height=200)
        self.baralho_de_compras.grid(row=0, column=1)
        
        img = ImageTk.PhotoImage(Image.open("src/images/card.png").resize((125, 200)))
        cartaB = ttk.Button(
            self.baralho_de_compras,
            image=img,
            padding=25,
            compound='bottom',
            style='RedCard.TLabel',
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
    def selecionar_carta(self, carta):
        
        if carta != "src/images/card.png":
            self.popup_dar_dica()
        else:
            self.popup_jogar_descartar_carta()