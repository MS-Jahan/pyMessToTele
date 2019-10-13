import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from fbchat import Client
from fbchat.models import *
import pickle
from getpass import getpass
import string
from pygtail import Pygtail


TOKEN = '' #Add Bot Token (Search 'Botfather', follow instruction, create bot and get token).
CHAT_ID = '' #Add your Chat ID (goto 'https://api.telegram.org/bot<token>/getupdates' for Chat ID). 

# Use '/setinline' and '/setinlinefeedback' one after another and follow their instructions to enable InlineQuery for 
# your telegram bot.

#bot = telepot.Bot(TOKEN)
t = ''
user = ''
step = 1
q_data = ''


def normalSend(msg, receiver_id):
    #content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Reply to ' + user, callback_data= receiver_id)],
               ])

    bot.sendMessage(CHAT_ID, msg, reply_markup=keyboard)



def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    messageText = msg['text'].decode("utf-8")
    messageInput(messageText)
    '''keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Reply to ' + user, callback_data= t)],
               ])
    client.send(Message(text = msg), thread_id= t, thread_type=ThreadType.USER)
    #bot.sendMessage(chat_id = CHAT_ID, msg['text'], reply_markup=keyboard)
    '''


class CustomClient(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
            global t 
            t = author_id
            thread = self.fetchThreadInfo(thread_id)[thread_id]
            global user
            user = thread.name
            if author_id != self.uid:
                if thread_type != ThreadType.GROUP:
                    print(str(thread_id) + " " + str(thread_type))
                    #user = client.fetchUserInfo(user_id)[user_id]
                    text = thread.name + ": " + message_object.text
                    #on_chat_message(text)
                    #bot.sendMessage(CHAT_ID, text)
                    normalSend(text, t)

def messageInput(Text):#######
    global step, no1, q_data
    if step == 1:
        bot.sendMessage(CHAT_ID, Text)
        step = 2
    elif step == 2:
        no1 = Text
        client.send(Message(text= no1), thread_id = q_data, thread_type=ThreadType.USER)
        step = 1


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    #print('Callback Query:', query_id, from_id, query_data)
    #print('Reply to ' + t)
    #bot.answerCallbackQuery(query_id, text='Got it')
    #bot.sendMessage(from_id, 'Reply to ' + t + ':')
    global q_data
    q_data = query_data
    thread = client.fetchThreadInfo(query_data)[query_data]
    messageText = 'Reply to ' + thread.name + ':'
    messageInput(messageText)
    
    
    




                    
'''
def handle(msg):
    #content_type, chat_type, chat_id = telepot.glance(msg)
    text_cmd = msg['text']
    #print text_cmd
    #if content_type == 'text': '100040523581208'
    bot.sendMessage(CHAT_ID, client.send(Message(text=text_cmd), thread_id= t, thread_type=ThreadType.USER))
    #bot.sendMessage(onMessage(message_id = client.send(Message(text=text_cmd), thread_id='100040523581208', thread_type=ThreadType.USER)))
    
 '''



    
        

        

      
        
try:
	print('Checking for cookies...')
	session_cookies = pickle.load(open('cookies.p','rb'))
	client = CustomClient("cookie", "cookie", session_cookies = session_cookies) # replace your username and password here
	print('Cookies found!')
except:
    print('Cookies not found. Please enter credentials.')
    client = CustomClient(raw_input('Email: '), getpass('Password: ')) # replace your username and password here
    session = client.getSession()
    pickle.dump(session, open('cookies.p','wb'))
    print('Cookies saved to cookies.p file.')


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
#MessageLoop(bot, handle).run_as_thread()
print 'Telegram bot has started Listening ...'
print('Starting program...')
client.listen()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
