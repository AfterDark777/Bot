from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hola! Soy un bot funcionando en Railway.')

def main():
    # Usa tu token aquí
    updater = Updater("8002085886:AAGvphg93iBGqSc9KiQcueounUUUd3L1kkg", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()