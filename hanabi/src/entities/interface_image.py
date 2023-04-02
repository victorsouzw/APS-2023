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
                
    def descartar_carta(self, carta : Carta, eh_infracao : bool):
        if not eh_infracao:
            self.set_dicas_disponiveis(self.get_dicas_disponiveis() + 1)
        self.adiciona_area_descarte(carta)
        jogador = self.get_jogador_local()
        jogador.jogar_descartar_carta(carta)               
        if len(self.__area_compra) > 0:
            self.comprar_carta()
        self.encerrar_turno_jogador()
        self.avaliar_fim_de_jogo()

    def adiciona_area_descarte(self, carta):
        self.__area_descarte.append(carta)
                    
    def encerrar_turno_jogador(self):
        self.set_status(StatusPartida.NOT_SEU_TURNO_EM_ANDAMENTO.value)
        jogador = self.get_jogador_local()
        if self.__ultima_rodada:
            jogador.set_jogou_ultimo_turno(True)
        self.carrega_imagem_cartas()
                
    def jogar_carta(self, carta : Carta):
        jogador = self.get_jogador_local()
        jogador.jogar_descartar_carta(carta)
        self.__area_cartas_jogadas.append(carta)
        if len(self.__area_compra) > 0:
            self.comprar_carta()
        self.encerrar_turno_jogador()
        
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
        
    def avaliar_fim_de_jogo(self):
        if len(self.__area_cartas_jogadas) == 25:
            self.define_mensagem_fim_de_jogo()
            self.__partida_encerrada = True     
            self.__match_status = "finished"        
        elif self.__infracoes_cometidas == 3:
            self.__match_status = "finished"  
            self.__mensagem = "Vocês perderam! O festival foi um fracasso."
            self.__partida_encerrada = True   
            print("JOGO FINALIZADO - DERROTA")        
        elif len(self.__area_compra) == 0:
            if self.__ultima_rodada:
                jogaram_ultima_rodada = 0
                for jogador in self.__jogadores:
                    if jogador.get_jogou_ultimo_turno():
                        jogaram_ultima_rodada += 1
                if jogaram_ultima_rodada == len(self._jogadores):
                    self.define_mensagem_fim_de_jogo()
                    self.__partida_encerrada = True   
                    self.__match_status = "finished"                            
            else:
                self.__ultima_rodada = True
        return
    
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
    
    def start_match(self, jogadores, id):
        self.__status = StatusPartida.AGUARDANDO_DISTRIBUICAO_CARTAS.value
        self.__jogadores = []         
        for i in range(len(jogadores)):
            jogador = Jogador(jogadores[i][0], jogadores[i][1], jogadores[i][2])
            if jogador.get_id() == id:
                jogador.set_eh_local(True)
                if jogador.get_posicao() == '1':
                    self.set_status(3)    
                else:
                    self.set_status(5)
            self.adicionar_jogador(jogador)
        if self.get_jogador_local().get_posicao() == '1':
            self.constroi_baralho_inicial()
            self.carrega_imagem_cartas()
            
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
                    
    def avaliar_carta_selecionada(self, carta):
        mensagem = "DAR_DICA"
        for jogador in self.__jogadores:
            if jogador.get_eh_local() and jogador.is_carta_no_baralho(carta):
                mensagem = "SELECIONAR_ESPAÇO"
        return mensagem
    
    def receber_jogada(self, jogada):
        self.set_area_cartas_jogadas(jogada.get_area_cartas_jogadas())
        self.set_area_compra(jogada.get_area_compra())
        self.set_area_descarte(jogada.get_area_descarte())
        self.set_dicas_disponiveis(jogada.get_dicas_disponiveis())
        self.set_infracoes_cometidas(jogada.get_infracoes_cometidas())
        self.set_jogadores(jogada.get_jogadores())      
        
        if jogada.get_match_status() == "next" and not self.get_status() == StatusPartida.AGUARDANDO_DISTRIBUICAO_CARTAS.value:
            self.set_status(StatusPartida.SEU_TURNO_EM_ANDAMENTO.value)
        elif self.get_status() == StatusPartida.AGUARDANDO_DISTRIBUICAO_CARTAS.value: 
            self.set_status(StatusPartida.NOT_SEU_TURNO_EM_ANDAMENTO.value)
        else: 
            self.set_status(StatusPartida.FINALIZADO.value)
        self.carrega_imagem_cartas()           
        
                
    def reset(self):
        self.set_area_cartas_jogadas([])
        self.set_area_compra([])
        self.set_area_descarte([])
        self.set_status(StatusPartida.AGUARDANDO_INICIO.value)
        self.set_jogadores([])
        self.set_dicas_disponiveis(8)
        self.set_infracoes_cometidas(0)
        self.set_mensagem("")
        
    def get_move_to_send(self):
        move_to_send = self.__dict__
        move_to_send["match_status"] = self.get_match_status()
        return move_to_send
    
    def convert_from_dict(self, interface_dict):
        interface = InterfaceImage()
        interface.set_mensagem = interface_dict._InterfaceImage__mensagem
        interface.set_area_cartas_jogadas([])
        for carta_jogada in interface_dict._InterfaceImage__area_cartas_jogadas:
            carta = Carta.convert_from_dict(carta_jogada)
            interface.__area_cartas_jogadas.append(carta)
        interface.set_area_compra([])       
        for carta_jogada in interface_dict._InterfaceImage__area_compra:
            carta = Carta.convert_from_dict(carta_jogada)
            interface.__area_compra.append(carta)
        interface.set_area_descarte([]) 
        for carta_jogada in interface_dict._InterfaceImage__area_descarte:
            carta = Carta.convert_from_dict(carta_jogada)
            interface.__area_descarte.append(carta)
        interface.__match_status = interface_dict._InterfaceImage__match_status
        interface.set_infracoes_cometidas(interface_dict._InterfaceImage__infracoes_cometidas)
        interface.set_dicas_disponiveis(interface_dict._InterfaceImage__dicas_disponiveis)
        interface.__ultima_rodada = interface_dict._InterfaceImage__ultima_rodada
        interface.__partida_encerrada = interface_dict._InterfaceImage__partida_encerrada
        interface.set_jogadores([])
        for jogador_dict in interface_dict._InterfaceImage__jogadores:
            jogador = self.get_jogador_by_id(jogador_dict._Jogador__jogador_id)
            jogador.set_mao_de_cartas([])
            for carta_dict in jogador_dict._Jogador__mao_de_cartas:
                carta = Carta.convert_from_dict(carta_dict)
                jogador.get_mao_de_cartas().append(carta)
            interface.get_jogadores().append(jogador)
        return interface   
            
    def get_jogador_by_id(self, id):
        for jogador in self.get_jogadores():
            if jogador.get_id() == str(id):
                return jogador
            
    def dar_dica(self, carta, tipo_de_dica):
        jogador_dono_da_carta = self.get_jogador_dono_da_carta(carta)
        if tipo_de_dica == TipoDeDica.COR:
            for carta_jogador in jogador_dono_da_carta.get_mao_de_cartas():
                if carta_jogador.get_cor() == carta.get_cor():
                    carta_jogador.receber_dica(TipoDeDica.COR)
        else:
            for carta_jogador in jogador_dono_da_carta.get_mao_de_cartas():
                if carta_jogador.get_numero() == carta.get_numero():
                    carta_jogador.receber_dica(TipoDeDica.NUMERO)
        
    def get_jogador_dono_da_carta(self, carta):        
        for jogador in self.__jogadores:
            for carta_jogador in jogador.get_mao_de_cartas():
                if carta_jogador == carta:
                    jogador_dono_da_carta = jogador
                    return jogador_dono_da_carta      
                
                    
        
            
            
            
            
                    
            
        
        
    
        