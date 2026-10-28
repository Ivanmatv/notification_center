from notification_center import NotificationCenter


class TelegramNotification(NotificationCenter):
    def __init__(self, telegram_id: str):
        super().__init__()
        self.__telegram_id = telegram_id
        self.is_valid_login = False
        self.__check_telegram_id()

    def __check_telegram_id(self) -> None:
        telegram_id_length = len(self.__telegram_id)
        TELEGRAM_ID_LENGTH = 5

        if (self.__telegram_id.isdigit()
                and telegram_id_length == TELEGRAM_ID_LENGTH):
            print('Telegram id is valid')
            self.is_valid_login = True
        else:
            print(f"Telegram id - {self.__telegram_id} - is not valid")
            self.is_valid_login = False

    def get_telegram_id(self) -> str:
        return self.__telegram_id

    def change_telegram_id(self, new_telegram_id: str) -> None:
        self.__telegram_id = new_telegram_id
        print("Telegram id changed")
