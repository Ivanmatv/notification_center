class NotificationCenter:
    def __init__(self, name):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def send_message(self, message) -> None:
        name = self.get_name()

        print(message)
        print(f"Сообщение отправлено через '{name}'")
