from email_notification_center import EmailNotification
from telegram_notification_center import TelegramNotification
from push_notification_center import PushNotification


STOP_COMMAND = "выйти"
input_command = ""

while input_command != STOP_COMMAND:
    print("""
    Каналы отправки сообщений.
    Введите канал отправки сообщения:
    1) Канал Telegram -> telegram
    2) Канал Email -> email
    3) Канал Push -> push
    """)

    input_notification_method = input("Введите канал отправки сообщения: ").strip().lower()
    input_user_login = input("Введите логин пользователя или названиe приложения: ").strip()
    print()

    NOTIFICATION_CENTRES = {
        "telegram": TelegramNotification,
        "push": PushNotification,
        "email": EmailNotification,
    }
    notification_center = None

    message = 'Внимание! Новая акция'

    if input_notification_method in NOTIFICATION_CENTRES:
            notification_center = NOTIFICATION_CENTRES[input_notification_method](input_user_login)

            if notification_center.is_valid_user_login():
                notification_center.send_message(message)
    else:
        print("Такой команды нет!")
