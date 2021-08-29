from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from liqScript import getLiquidity
import requests
import re

def get_liquidity(arg):
    print(arg)
    content = getLiquidity(arg)
    return content

def bop(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id,text='fetching data...')
    if (len(context.args) < 1):
        context.bot.send_message(chat_id=chat_id,text='currency argument missing, please specify')
    else:
        try:
            liquidity_response = get_liquidity(context.args[0])
            if liquidity_response['liquidity']:
                context.bot.send_message(chat_id=chat_id,text='Available Liquidity: ' + liquidity_response['liquidity'])
            else:
                context.bot.send_message(chat_id=chat_id,text=liquidity_response)
        except:
            context.bot.send_message(chat_id=chat_id,text='An error occured while Processing, try again later')
        
def main():
    updater = Updater('1921554220:AAFFpfwcDoe7C7xXqDB9EqVnwepa-psrNV0', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('liquidity',bop,pass_args=True))
    updater.start_polling()
    
    updater.idle()

if __name__ == '__main__':
    main()