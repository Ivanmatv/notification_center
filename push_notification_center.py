from notification_center import NotificationCenter


class PushNotification(NotificationCenter):
    def __init__(self, application_name: str):
        super().__init__()
        self.__application_name = application_name
        self.__applications = ["MAX"]
        self.is_valid_login = False
        self.__check_application_name()

    def __check_application_name(self) -> None:
        if self.__application_name in self.__applications:
            print(f"application - {self.__application_name} - is exist")
            self.is_valid_login = True
        else:
            print(f"Application - {self.__application_name} - is not exist")
            self.is_valid_login = False

    def get_application_name(self) -> str:
        return self.__application_name

    def change_application_name(self, new_application_name: str):
        self.__application_name = new_application_name
        print("Application name changed")
