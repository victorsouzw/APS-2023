import array as arr
import random
from Enumerations.StatusPartida import StatusPartida
from entities.carta import Carta
from entities.jogador import Jogador
from Enumerations.TipoDeDica import TipoDeDica

class InterfaceImage:
    def __init__(self):
        self.__mensagem = ""
        self.__area_cartas_jogadas = []
        self.__area_descarte = []
        self.__area_compra = []
        self.__status = StatusPartida.AGUARDANDO_INICIO.value
        self.__jogadores = []
        self.__ultima_rodada = False
        self.__partida_encerrada = False
        self.__dicas_disponiveis = 8
        self.__infracoes_cometidas = 0
        self.__match_status = "next"
        
    def get_match_status(self):
        return self.__match_status
        
    def __repr__(self):
        return str(self.__dict__)
        
    def get_partida_encerrada(self):
        return self.__partida_encerrada
        
    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem
        
    def get_mensagem(self): 
        return self.__mensagem
    
    def set_area_cartas_jogadas(self, baralho):
        self.__area_cartas_jogadas = baralho
    
    def get_area_cartas_jogadas(self):
        return self.__area_cartas_jogadas
    
    def set_area_descarte(self, baralho):
        self.__area_descarte = baralho
        
    def get_area_descarte(self):
        return self.__area_descarte
    
    def set_area_compra(self, baralho):
        self.__area_compra = baralho
        
    def get_area_compra(self):
        return self.__area_compra
    
    def set_status(self, status):
        self.__status = status
        
    def get_status(self):
        return self.__status
    
    def set_jogadores(self, jogadores):
        self.__jogadores = jogadores
        
    def get_jogadores(self):
        return self.__jogadores

    def get_dicas_disponiveis(self):
        return self.__dicas_disponiveis

    def set_dicas_disponiveis(self, dicasDisponiveis: int):
        self.__dicas_disponiveis = dicasDisponiveis

    def set_infracoes_cometidas(self, infracoes_cometidas: int):
        self.__infracoes_cometidas = infracoes_cometidas
        
    def get_infracoes_cometidas(self):
        return self.__infracoes_cometidas
       
    def constroi_baralho_inicial(self):
        baralho_compra = self.get_area_compra()
        cores = {1: "red", 2: "green", 3: "blue", 4: "yellow", 5:"white"}
        for i in range (1,6): #numero
            for j in range (1,6): #cor
                baralho_compra.append(Carta(cores.get(j), i))
                if i == 1:
                    baralho_compra.append(Carta(cores.get(j), i))
                if i != 5:
                    baralho_compra.append(Carta(cores.get(j), i))
        self.set_area_compra(random.sample(baralho_compra, len(baralho_compra)))
        self.distribui_cartas_pros_jogadores()
        
    def distribui_cartas_pros_jogadores(self):
        for jogador in self.__jogadores:
            baralho_jogador = []
            for i in range (5):                
                baralho_jogador.append(self.__area_compra[i])
                self.__area_compra.pop(i)
            jogador.set_mao_de_cartas(baralho_jogador)
                




                

        
    def get_jogador_local(self):
        for jogador in self.__jogadores:
            if jogador.get_eh_local():
                return jogador
        return 0
        
    def comprar_carta(self):
        jogador = self.get_jogador_local()
        cartaComprada = self.__area_compra[random.randrange(len(self.__area_compra))]
        self.__area_compra.remove(cartaComprada)
        jogador.get_mao_de_cartas().append(cartaComprada)
        

    
    def define_mensagem_fim_de_jogo(self):
        pontuacao = len(self.__area_cartas_jogadas)
        if pontuacao <= 5:
            self.__mensagem = "Horrível, vaias da multidão."
        elif 6 <= pontuacao <= 10:
            self.__mensagem = "Medíocre, mal se ouvem aplausos."
        elif 11 <= pontuacao <= 15:
            self.__mensagem = "Honrosa, mas não ficará na memória..."
        elif 16 <= pontuacao <= 20:
            self.__mensagem = "Excelente, encanta a multidão."
        elif 21 <= pontuacao <= 24:
            self.__mensagem = "Extraordinária, ficará na memória."
        elif pontuacao == 25:
            self.__mensagem = "Lendária, adultos e crianças atônitos, estrelas em seus olhos!"
    

            
    def adicionar_jogador(self, jogador):
        self.get_jogadores().append(jogador)
        
    def carrega_imagem_cartas(self):
        for carta in self.__area_cartas_jogadas:
            carta.carrega_imagem_carta(True, False)
            
        for carta in self.__area_descarte:
            carta.carrega_imagem_carta(True, False)
            
        for jogador in self.__jogadores:
            if jogador.get_eh_local():
                for carta in jogador.get_mao_de_cartas():
                    carta.carrega_imagem_carta(False, True)
            else: 
                for carta in jogador.get_mao_de_cartas():
                    carta.carrega_imagem_carta(False, False)
                    


        
                

        

    




                
                    
        
            
            
            
            
                    
            
        
        
    
        