import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)
def start_bot(update: Updater, context: CallbackContext):
    print(update)
    mytext = """Привет dfkthf {}
    я могу использовать только команду  /start =)""".format(update.message.chat.first_name)
    update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
    text= update.message.text
    logging.info(text)

    update.message.reply_text(text)


def main():
    updtr = Updater('1449256444:AAEXKP965duuF7ufMEukRAH_8nBjSjt_k9E')

    updtr.dispatcher.add_handler(CommandHandler("start",start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text,chat))

    updtr.start_polling()
    updtr.idle()
if __name__ == "__main__":
    logging.info('Bot started!')
    main()