# simple bot
# by t.me/akhsan20
# using telepot

import telepot, time
from telepot.loop import MessageLoop

def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']
   print ('Got command: %s' % command)

   if command == '/start':
      bot.sendMessage(chat_id, "OK let's go.....")
   else:
      print ('Your comand: %s' % command)
      bot.sendMessage(chat_id, 'Your comand: \n' + command)
      pass
      
def on_callback_query(msg):
   query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
   print('press_menu:', query_id, from_id, query_data)

   bot.answerCallbackQuery(query_id, text='Got it')

# Create a bot object with API key
bot = telepot.Bot('YOUR_TOKEN')

# Attach a function to notifyOnMessage call back
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print 'I am listening ...'

# Listen to the messages
while 1:
    time.sleep(10)
