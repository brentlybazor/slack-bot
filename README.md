# Slack Bot

## This python bot keeps you appearing 'online' on Slack

This bot simulates typing on slack to keep the appearance of being online. It is suggested to use your own person DM section so it does not show that you are typing to someone else.

---

Steps to get this bot working:

1. Make sure to have Python 3 installed
1. Install these packages using *pip*
    - *pip install -U python-dotenv*
    - *pip install -U selenium*
1. Download the [Chrome webdriver](https://chromedriver.chromium.org/)
1. Extract the webdriver and move it to a different directory. (default for this program is *C:\Program Files (x86)\chromedriver.exe*, but can be changed in the *.env* file or overriden in the *.env.local*)
1. Set up the environment variables in the .env and .env.local
1. It is recommended to put sensitive data (email, password, etc.) in the .env.local to prevent accidentally pushing to repo
1. Navigate to the directory in a terminal and type *`python index.py`* to start the bot.
---

Other things to note:
- The local environment variables should go in *.env.local*
- Some of the local variables are availiabe in the *.env* to copy/paste to *.env.local*