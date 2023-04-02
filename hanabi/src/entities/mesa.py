from entities.carta import Carta
from entities.interface_image import InterfaceImage
from Enumerations.TipoDeDica import TipoDeDica
from Enumerations.StatusPartida import StatusPartida


class Mesa:

    def __init__(self):
        self.__estado = InterfaceImage()

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado: InterfaceImage):
        self.__estado = estado

    def dar_dica(self, carta: Carta, tipo_de_dica: TipoDeDica):
        if self.__estado.get_dicas_disponiveis() > 0:
            self.__estado.dar_dica(carta, tipo_de_dica)
            self.__estado.set_dicas_disponiveis(self.__estado.get_dicas_disponiveis() - 1)
            self.__estado.encerrar_turno_jogador()
            return ""
        else:
            return "Não há dicas disponíveis. Ação indisponível!"

    def jogar_carta(self, cartaJogada: Carta):
        podeSerJogada = self.validar_carta_jogada(cartaJogada)
        if podeSerJogada:
            self.__estado.jogar_carta(cartaJogada)
            if cartaJogada.get_numero() == 5:
                self.__estado.set_dicas_disponiveis(self.__estado.get_dicas_disponiveis() + 1)
        else:
            self.__estado.set_infracoes_cometidas(self.__estado.get_infracoes_cometidas() + 1)
            self.__estado.descartar_carta(cartaJogada, True)
        self.__estado.avaliar_fim_de_jogo()

    def validar_carta_jogada(self, cartaJogada: Carta):
        cor = cartaJogada.get_cor()
        ultimoNumeroJogado = self.get_numero_carta_mais_alta_da_cor(cor)
        if cartaJogada.get_numero() == ultimoNumeroJogado + 1:
            return True
        return False

    def get_numero_carta_mais_alta_da_cor(self, cor: str):
        num_carta_mais_alta = 0
        for carta in self.__estado.get_area_cartas_jogadas():
            if carta.get_cor() == cor:
                num_carta_mais_alta += 1

        return num_carta_mais_alta

    def comprar_carta(self):
        self.__estado.comprar_carta()

    def descartar_carta(self, carta: Carta):
        if self.__estado.get_dicas_disponiveis() < 8:
            self.__estado.descartar_carta(carta, False)
            return ""
        else:
            return "Não há dicas a serem recuperadas, portanto você não pode descartar nenhuma carta. Escolha outra ação."

    def receber_notificacao_de_desistencia(self):
        self.reset()
        self.get_estado().set_jogadores([])
        self.get_estado().set_status(StatusPartida.AGUARDANDO_INICIO.value)

    def start_match(self, jogadores, id: int):
        self.__estado.start_match(jogadores, id)

    def avaliarFimDeJogo(self):
        self.__estado.avaliarFimDeJogo()
        if self.__estado.get_mensagem() != "":
            pontuacao_final = len(self.__estado.get_area_cartas_jogadas())
            self.__estado.set_pontuacao_final(pontuacao_final)

    def selecionar_carta(self, carta):
        return self.__estado.avaliar_carta_selecionada(carta)

    def receber_jogada(self, jogada_dict):
        jogada = self.__estado.convert_from_dict(jogada_dict)
        self.__estado.receber_jogada(jogada)

    def reset(self):
        self.__estado.reset()
        
    def receber_notificacao_desistencia(self):
        self.__estado.set_status(StatusPartida.DESISTENCIA.value)
        self.__estado.reset()
    
    def jogador_local_inicia(self):
        if self.__estado.get_jogador_local().get_posicao() == '1':
            return True
        return False
