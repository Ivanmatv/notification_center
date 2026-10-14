from email import EmailNotification
from telegram import TelegramNotification
from push import PushNotification


push = PushNotification('Push')
telegram = TelegramNotification('Telegram')
email = EmailNotification('Email')

message = 'Внимание! Новая акция'

STOP_COMMAND = "выйти"
input_command = ""

while input_command != STOP_COMMAND:
    print("""
    Каналы отправки сообщений.
    Введите команду на выбор:
    1) Телеграм -> telegram
    2) Email -> email
    3) Push -> push
    """)
    input_command = input("Введите канал отправки сообщения: ").lower().strip()

    print()

    match input_command:
        case "telegram":
            telegram.send_message(message)
        case "email":
            email.send_message(message)
        case "push":
            push.send_message(message)
        case _:
            print("Такой команды нет!")

    print()
