from email_notification_center import EmailNotification
from telegram_notification_center import TelegramNotification
from push_notification_center import PushNotification


NOTIFICATION_CENTRES = {
        "telegram": TelegramNotification,
        "push": PushNotification,
        "email": EmailNotification,
    }

notification_center = None

message = 'Внимание! Новая акция'

STOP_COMMAND = "выйти"
input_notification_method = ""

while input_notification_method != STOP_COMMAND:
    print("""
    Каналы отправки сообщений.
    Введите канал отправки сообщения:
    1) Канал Telegram -> telegram
    2) Канал Email -> email
    3) Канал Push -> push
    """)

    input_notification_method = ""
    while not input_notification_method or input_notification_method == STOP_COMMAND:
        input_notification_method = input("Введите канал отправки сообщения: ").strip().lower()

        if input_notification_method not in NOTIFICATION_CENTRES:
            input_notification_method = False
            print("Такого метода нет")

    input_user_login = input("Введите логин пользователя или названиe приложения: ").strip()

    print()

    if input_notification_method in NOTIFICATION_CENTRES:
        notification_center = NOTIFICATION_CENTRES[input_notification_method](input_user_login)

        if notification_center.is_valid_user_login():
            notification_center.send_message(message)
    else:
        print("Такой команды нет!")
