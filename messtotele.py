# -*- coding: utf-8 -*-


#import sys
import os
#import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from fbchat import Client
from fbchat.models import *
import pickle
from getpass import getpass
#import string





TOKEN = '' #Add Bot Token (Search 'Botfather', follow instruction, create bot and get token).
CHAT_ID = '' #Add your Chat ID (goto 'https://api.telegram.org/bot<token>/getupdates' for Chat ID). 

# Use '/setinline' and '/setinlinefeedback' one after another and follow their instructions to enable InlineQuery for 
# your telegram bot.

names = []



#bot = telepot.Bot(TOKEN)
t = ''
user = ''
step = 0
q_data = ''
dirpath = 'images/images.jpg' #For Windows, use // instead of /.




def normalSend(msg, title, receiver_id):
    #content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text= title, callback_data = receiver_id)],
               ])

    bot.sendMessage(CHAT_ID, msg, reply_markup=keyboard)
    
def normalSend0(msg, title, receiver_id):
    #content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text= title, callback_data = receiver_id)],
                   [InlineKeyboardButton(text= 'Last Messages', callback_data = 'read_msg' + receiver_id)]
               ])

    bot.sendMessage(CHAT_ID, msg, reply_markup=keyboard)    



def on_chat_message(msg):
    try:
        os.remove(dirpath)
    except:
        None
    else:
        print('Error!')
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(msg)
    print(content_type)
    if msg['text'] == '/help':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Show Last 20 Threads', callback_data='show_lt')],
                   
               ])

        bot.sendMessage(chat_id, msg['text'], reply_markup=keyboard)
    
    elif '/searchUser' in msg['text']:
        msg['text'] = msg['text'].replace('/searchUser ', '')
        user = client.searchForUsers(msg['text'])[0]
        print(user)
        
    elif '/search' in msg['text']:
        msg['text'] = msg['text'].replace('/search ', '')
        thread = client.searchForThreads(msg['text'])
        print(thread)

    
    elif content_type == 'text':
        try:
            messageText = msg['text'].decode("utf-8")           
        except:
            messageText = msg['text']
        else:
            messageText = msg['text']
        messageInput(messageText, 'text')
    
        
    elif content_type == 'document' or content_type == 'photo':
        try:
            bot.download_file(msg['document']['file_id'], dirpath)
            messageText = dirpath
            messageInput(messageText, 'photo')
        except:
            ttt = str(msg)
            substr = ttt[209:268]
            substr = str(substr)
            print(substr)
            bot.download_file(substr, dirpath)
            messageText = dirpath
            messageInput(messageText, 'photo')
        '''else:
            bot.sendMessage(CHAT_ID, 'Cannot send this type of files.')'''
    
    
    
    
    
    
    
    
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
                if message_object.text:
                    print(str(thread_id) + " " + str(thread_type))
                    #user = client.fetchUserInfo(user_id)[user_id]
                    text = thread.name + ": " + message_object.text
                    #on_chat_message(text)
                    #bot.sendMessage(CHAT_ID, text)
                    normalSend(text, '✏ Reply', t)
                elif len(message_object.attachments) > 0:
                    for i in message_object.attachments:
                        if isinstance(i, ImageAttachment):
                            text = thread.name + ": " + i.large_preview_url
                            text = 'Reply to ' + thread.name
                            normalSend(text, '✏ Reply', t)
                else:
                    text = thread.name + " has sent you something! Check it on " + "https://www.facebook.com/messages/t/" + author_id
    

    
    

def messageInput(Text, type):
    global step, no1, q_data
    if step == 1:
        bot.sendMessage(CHAT_ID, Text)
        step = 2
    elif step == 2:
        if type == 'text':
            no1 = Text
            client.send(Message(text = no1), thread_id = q_data, thread_type=ThreadType.USER)
            step = 1
        elif type == 'photo' or type == 'document':
            client.sendLocalImage(Text, message=Message(text= None), thread_id=q_data, thread_type=ThreadType.USER)
            step = 1
            bot.sendMessage(CHAT_ID, 'File was sent!')
    else:
        bot.sendMessage(CHAT_ID, 'Please click on any button from any recipient first!')

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    #print('Callback Query:', query_id, from_id, query_data)
    #print('Reply to ' + t)
    #bot.answerCallbackQuery(query_id, text='Got it')
    #bot.sendMessage(from_id, 'Reply to ' + t + ':')
    global q_data, step
    step = 1
    q_data = query_data
    if query_data == 'show_lt':
        threads = client.fetchThreadList()
        #print(threads)
        #names = []
        #q_data = []
        for items in range(len(threads)):
            #print(threads[items])
            index1 = str(threads[items]).find(", name=") + 9
            #print(index1)
            index2 = str(threads[items]).find("', last_message_timestamp")
            #print(index2)
            name = str(threads[items])[index1:index2].decode('unicode-escape').encode('utf-8')
            #names.append(name)
            #names[items] = names[items].decode('unicode-escape').encode('utf-8')
            
            index1 = str(threads[items]).find("uid") + 5
            #print(index1)
            index2 = str(threads[items]).find("', type")
            #print(index2)
            q = str(threads[items])[index1:index2]
            #q_data.append(q)
            
            normalSend0(name, '✏ Reply', q)
    
    elif 'read_msg' in query_data:
        messages = client.fetchThreadMessages(thread_id=query_data.replace('read_msg', ''), limit=10)
        messages.reverse()
        #print(messages)
        for items in range(len(messages)):
            index1 = str(messages[items]).find("text='") + 16
            index2 = str(messages[items]).find("', mentions")
            mess = str(messages[items])[index1:index2].decode('unicode-escape').encode('utf-8')
            
            index1 = str(messages[items]).find("author='") + 8
            index2 = str(messages[items]).find("', timestamp")
            thread = str(messages[items])[index1:index2]
            thread = client.fetchThreadInfo(thread)[thread]
            thread = thread.name + ': '
            try:
                text = thread + mess
            except:
                text = thread.decode('unicode-escape').encode('utf-8') + mess
            bot.sendMessage(CHAT_ID, text)
        
        thread = client.fetchThreadInfo(query_data.replace('read_msg', ''))[query_data.replace('read_msg', '')]    
        normalSend('Reply to: ' + thread.name, '✏ Reply', query_data.replace('read_msg', ''))
            
        
        #print(threads)    
    else:    
        thread = client.fetchThreadInfo(query_data)[query_data]
        messageText = 'Reply to ' + thread.name + ':'
        messageInput(messageText, 'text')
    
    
    




                    
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

'''
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
'''
