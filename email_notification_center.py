from notification_center import NotificationCenter


class EmailNotification(NotificationCenter):
    def __init__(self, email: str):
        super().__init__()
        self.__email = email
        self.is_valid_login = False
        self.__check_email()

    def __check_email(self) -> None:
        EMAIL_SYMBOL = '@'

        if EMAIL_SYMBOL in self.__email:
            print(f"Email - {self.__email} - is valid")
            self.is_valid_login = True
        else:
            print(f"Email - {self.__email} - is not valid")
            self.is_valid_login = False

    def get_email(self) -> str:
        return self.__email

    def change_email(self, new_email: str) -> None:
        self.__email = new_email
        print("Email changed")
