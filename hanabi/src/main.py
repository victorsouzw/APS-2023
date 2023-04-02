# -*- coding: utf-8 -*-

import tkinter as tk
from functools import partial
from tkinter import ttk
from entities.jogador import Jogador
from dog.dog_actor import DogActor
import player_interface


class App(tk.Tk):
    player_interface.PlayerInterface()
    
    # #TODO implementar PlayerInterface de acordo com diagrama de classes nessa classe aqui
    
    # def __init__(self):
    #     super().__init__()
    #     self.playerHandHeight = 135
    #     self.playerHandWidth = 400
    #     self.playersHub = tk.Frame(self, width=250, bg="#ababab")
    #     self.playersHubMenu = tk.Frame(self.playersHub, width=self.playerHandWidth, height=200, bg='black')
    #     self.playerOneCanvas = tk.Canvas(self.playersHub, width=self.playerHandWidth, height=200)
    #     self.__time = Time()
    #     # self.__time.adicionar_jogador(
    #     #     Jogador("Jogador 1", tk.LabelFrame(self.playerOneCanvas, text="Player one", width=self.playerHandWidth,
    #     #                                        height=self.playerHandHeight, bg="red")))
    #     # self.__time.adicionar_jogador(Jogador("Jogador 2", tk.LabelFrame(self.playersHub, text="Player 2",
    #     #                                                                  width=self.playerHandWidth,
    #     #                                                                  height=self.playerHandHeight,
    #     #                                                                  bg="green")))
    #     # self.__time.adicionar_jogador(
    #     #     Jogador("Jogador 3", tk.LabelFrame(self.playersHub, text="player three", width=self.playerHandWidth,
    #     #                                        height=self.playerHandHeight, bg="yellow")))
    #     # self.__time.adicionar_jogador(
    #     #     Jogador("Jogador 4", tk.LabelFrame(self.playersHub, text="Player 4", width=self.playerHandWidth,
    #     #                                        height=self.playerHandHeight, bg="white")))
    #     self.dogActor = DogActor()
    #     # for jogador in self.__time.get_jogadores():
    #     #     if jogador.get_nome() == "Jogador 1":
    #     #         self.dogActor.initialize("Jogador 1", jogador)

    #     self.title('Hanabi')

    #     # heading style
    #     self.style = ttk.Style(self)
    #     self.style.configure('Heading.TLabel', font=('Helvetica', 12))

    #     self.style.configure('backCard.TLabel',
    #                          font=('Helvetica', 12),
    #                          foreground='black',
    #                          background='#F2F2F2'
    #                          )

    #     self.style.configure('redCard.TLabel',
    #                          font=('Helvetica', 12),
    #                          foreground='red',
    #                          background='#3F0502'
    #                          )

    #     self.style.configure('blueCard.TLabel',
    #                          font=('Helvetica', 12),
    #                          foreground='blue',
    #                          background='#02053F'
    #                          )

    #     # UI options
    #     paddings = {'padx': 5, 'pady': 5}
    #     entry_font = {'font': ('Helvetica', 11)}

    #     self.playersHubTitle = tk.Label(self.playersHubMenu, text='Players Hub')
    #     self.playersHubTitle.pack()
    #     self.playersHubMenu.pack(side='top', fill='both', expand=True)
    #     self.playerOneCanvas.pack(side='top', fill='both', expand=True)

    #     self.dogActor.start_match(2)

    #     def click_carta(carta, jogador):
    #         try:
    #             self.cartaSelecionada.destroy()
    #         except:
    #             pass
    #         finally:
    #             self.cartaSelecionada = ttk.Label(
    #                 self.selectCard,
    #                 image=carta.get_url(),
    #                 padding=5,
    #                 compound='bottom',
    #                 text=str(carta.get_numero()) + carta.get_cor() + jogador.get_nome(),
    #                 style='RedCard.TLabel'
    #             )
    #             self.cartaSelecionada.image = carta
    #             self.cartaSelecionada.pack(side='left', fill='both')
    #             self.dogActor.send_move(str(carta.get_numero()) + carta.get_cor() + jogador.get_nome())

    #     # for jogador in self.__time.get_jogadores():
    #     #     jogador.get_posicao().pack(side='top', fill='both', expand=True)
    #     #     for carta in jogador.get_mao_de_cartas():
    #     #         if jogador.get_nome() == "Jogador 1":
    #     #             photo = tk.PhotoImage(file='./back.png'),
    #     #             cartaM = ttk.Button(
    #     #                 jogador.get_posicao(),
    #     #                 image=photo,
    #     #                 padding=5,
    #     #                 compound='bottom',
    #     #                 style='RedCard.TLabel',
    #     #                 command=partial(click_carta, carta, jogador)
    #     #             )
    #     #             cartaM.image = photo,
    #     #             cartaM.pack(side='left', fill='both')
    #     #         else:
    #     #             cartaM = ttk.Button(
    #     #                 jogador.get_posicao(),
    #     #                 image=carta.get_url(),
    #     #                 padding=5,
    #     #                 compound='bottom',
    #     #                 text=str(carta.get_numero()) + carta.get_cor(),
    #     #                 style='RedCard.TLabel',
    #     #                 command=partial(click_carta, carta, jogador)
    #     #             )
    #     #             cartaM.image = carta.get_url(),
    #     #             cartaM.pack(side='left', fill='both')
    #         self.selectCard = tk.LabelFrame(self, text='Selected Card', bg='#D0E0E0')
    #         self.selectCard.grid(row=2, column=1, rowspan=1, columnspan=2, sticky="nsew")

    #     self.playersHub.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nsew")

    #     self.tablePosition = tk.LabelFrame(self, text='Cards played', bg='#D0E0E0')
    #     self.tablePosition.grid(row=0, column=1, rowspan=1, columnspan=2, sticky="nsew")

    #     self.playAreaRed = tk.Frame(self.tablePosition, width=72, height=96, bg='#FF3030')
    #     self.playAreaRed.pack(side='left')
    #     self.playAreaBlue = tk.Frame(self.tablePosition, width=72, height=96, bg='#3030FF')
    #     self.playAreaBlue.pack(side='left')
    #     self.playAreaGreen = tk.Frame(self.tablePosition, width=72, height=96, bg='#30FF30')
    #     self.playAreaGreen.pack(side='left')
    #     self.playAreaYellow = tk.Frame(self.tablePosition, width=72, height=96, bg='#F9D71C')
    #     self.playAreaYellow.pack(side='left')
    #     self.playAreaWhite = tk.Frame(self.tablePosition, width=72, height=96, bg='#FFFFFF')
    #     self.playAreaWhite.pack(side='left')

    #     self.hintArea = tk.Frame(self, bg='#402010')
    #     self.hintAreaTitle = tk.Label(self.hintArea, text='Number of hints')
    #     self.hintAreaTitle.pack(side='top', expand=True)
    #     self.hintArea.grid(row=1, column=1, columnspan=1, sticky='nsew')

    #     discardText = '1 1 1 2 2 3 3 4 4 5'
    #     discardTextFormat = '{} {} {} {} {} {} {} {} {} {}'  # .format(range(10))

    #     self.discardArea = tk.Frame(self, width=200, bg='#4020F0')
    #     self.discardAreaTitle = tk.Label(self.discardArea, text='Discarded cards')
    #     self.discardAreaTitle.pack(side='top', expand=True)
    #     self.discardAreaContentRed = ttk.Label(self.discardArea, text=discardText, style='RedCard.TLabel')
    #     self.discardAreaContentBlue = ttk.Label(self.discardArea, text=discardText, style='BlueCard.TLabel')
    #     self.discardArea.grid(row=1, column=2, columnspan=1, sticky='nsew')
    #     self.discardAreaContentRed.pack(side='top', expand=True)
    #     self.discardAreaContentBlue.pack(side='top', expand=True)


    #     # Log of hints
    #     self.hintLog = tk.Frame(self, width=200, bg='#607040')


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
