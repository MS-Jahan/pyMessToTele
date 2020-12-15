# [THIS THING ISN'T WORKING RIGHT NOW CORRECTLY (fbchat module issue). USE IT IF YOU CAN DEBUG AND LET ME KNOW IF YOU CAN.]


# pyMessToTele
Reply to Messenger messages from Telegram.

Connect your Facebook Messenger to Telegram easily. Because Telegram is better, secure, simple and fun.

## Getting Started
Follow these instructions carefully to get this script up and running.

### Prerequisites
The things you need to get this script running:
1. Make sure Python 2 is installed in your machine.
2. Create bot in Telegram with @botfather and get the Bot Token.
3. Use '/setinline' and '/setinlinefeedback' command in @botfather conversation one after another and follow their instructions to enable InlineQuery for your telegram bot.
4. Get your Chat ID. See instructions [here](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id).
5. You also need a Facebook account, of course! 😉


### Usage

#### Before Running The Script
Please place your Chat ID and Bot Token in the script. No need to add facebook password in the script. You'll be prompted to enter password after running the script. Because of cookie usage, you'll not need to enter password next time unless you change your Facebook password or your IP address is changed.

#### Running Script
1. Clone this repository in your server/computer: `git clone https://github.com/MS-Jahan/pyMessToTele`
2. Change directory to project folder: `cd pyMessToTele`
3. Install essential modules: `python2 -m pip install telepot fbchat getpass pickle --user`
4. Make changes in your script according to **Before Running The Script**.
5. Run your script: `python2 messtotele.py`
6. Type your email and password when asked. Password will not be visible when typing.
7. Now you will be able to receive and respond to messages from Facebook Messenger from Telegram. :-)

Run this script on Android using [these instructions](https://github.com/MS-Jahan/pyMessToTele/blob/master/android-instructions.md).

## ToDo

- [x] Inline buttons.
- [x] Send photo from Telegram to Messenger.
- [ ] Receive media (photo, video, gif, voice, sticker) from Messenger to Telegram.
- [ ] Group chat support
- [x] Easily change current chat.
- [x] Show Contact List of Messenger in Telegram
- [x] Support for file attachments.

### Similar Project

[Messenger to Telegram](https://github.com/AlexR1712/messenger-to-telegram) written in NodeJs. I was inspired from my need at first and then this project!
