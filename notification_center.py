class NotificationCenter:
    def __init__(self):
        self.is_valid_login = None

    def send_message(self, message: str) -> None:
        print(message)

    def is_valid_user_login(self) -> bool:
        if self.is_valid_login:
            return True
        else:
            return False