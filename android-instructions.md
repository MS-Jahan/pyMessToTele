# Using on Android
To use this python tool on Android, you have to install a linux terminal emulator named Termux which is available on Google Play Store. After Installing Termux, open the app, write down the commands stated below one by one and press enter.
<ol>
<li>Update and upgrade packages: <code>apt update && apt upgrade</code> (Press y and enter when prompted to upgrade packages.)</li>
<li>Install python and git: <code>apt install python git</code></li>
<li>Get storage permission; Press <b>Allow</b>: <code>termux-setup-storage</code>
<li>Change directory to internal storage: <code>cd /storage/emulated/0</code>
<li>Clone this repository: <code>git clone https://github.com/MS-Jahan/pyMessToTele</code></li>
<li>Install necessary python modules: <code>python2 -m pip install telepot fbchat getpass pickle --user</code></li>
<li>Change directory to this project folder: <code>cd pyMessToTele</code></li>
<li>Make changes in your script according to <b>Before Running The Script</b> in the <a href='https://github.com/MS-Jahan/pyMessToTele/blob/master/README.md'>README.md</a>.</li>
<li>Now run the script: <code>python2 messtotele.py</code></li>
<li>Type your email and password when asked. Password will not be visible when typing.</li>
<li>Now you will be able to receive and respond to messages from Facebook Messenger from Telegram :-)</li>
</ol>
