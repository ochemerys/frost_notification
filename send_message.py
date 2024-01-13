"""Send a message to phone number.
    Usage:
    python3 send_message.py <PHONE_NUMBER> <"MESSAGE">
"""
import sys
import subprocess


def send_message(phone_number, message):
    """Send a message to phone number.
        
        Args:
            phone_number: phone number as integer of 10 0r 11 digits
            message: The message to be sent as UTF-8 string.
    """
    apple_script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', apple_script])


def main(phone_number, message):
    """Validate parameters and Send a message to a phone number.

        Args:
            phone_number: phone number as integer of 10 0r 11 digits
            message: The message to be sent as UTF-8 string.
    """
    try:
        phone_number = int(phone_number)
        if len(str(phone_number)) < 10 or len(str(phone_number)) >= 12:
            raise ValueError() 
        if len(message) < 1:
            raise ValueError() 
        try:
            send_message(phone_number, message)
        except:
            print("An exception occurred during sending message") 
    except ValueError:
        print('Invalid Phone Number or Message is empty')


if __name__ == '__main__':
    ph_num = sys.argv[1]
    msg = sys.argv[2]
    main(ph_num, msg)