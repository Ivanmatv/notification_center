from email import EmailNotification
from telegram import TelegramNotification
from push import PushNotification


push = PushNotification('Push')
telegram = TelegramNotification('Telegram')
email = EmailNotification('Email')

message = 'Внимание! Новая акция'
push.send_message(message)
