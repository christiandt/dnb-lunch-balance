import os
from microsmycentral import MicrosMycentral
import getpass
import keyring
import pync
import sys

username = ""
balance = 0

username_file_path = os.path.join(
    os.path.expanduser("~/.config"),
    "dnb-lunch-username"
)


def main():
    global balance
    global username

    try:
        with open(username_file_path, 'rb') as username_file:
            username = username_file.read().strip()
    except IOError as e:
        if "No such file" in str(e):
            set_credentials()

    password = keyring.get_password("pylunch", username)

    mmc = MicrosMycentral()
    if mmc.post_credentials(username, password):
        balance = mmc.get_current_balance()
        message = "Current balance: {0:.2f} kr".format(balance)
        pync.notify(message, title='Lunch', appIcon='appicon.icns')
    else:
        print("failed to post credentials")


def set_credentials():
    global username
    username = raw_input('Add dnb email: ')
    with open(username_file_path, 'wb') as username_file:
        username_file.write(username)
    keyring.set_password("pylunch", username, getpass.getpass(prompt='Add password: '))


if __name__ == '__main__':
    if "reset" in sys.argv:
        set_credentials()
    main()
