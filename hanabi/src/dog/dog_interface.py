from entities.interface_image import InterfaceImage

class DogPlayerInterface:
    def __init__(self):
        super().__init__()

    def receive_start(self, start_status : InterfaceImage):
        print("O método receive_start() precisa ser sobrescrito")

    def receive_move(self, a_move : InterfaceImage):
        print("O método receive_move() precisa ser sobrescrito")

    def receive_withdrawal_notification(self):
        print("O método receive_withdrawal_notification() precisa ser sobrescrito")
