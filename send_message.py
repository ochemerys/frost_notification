import subprocess

def send_message(phone_number, message):
    apple_script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''

    subprocess.run(['osascript', '-e', apple_script])

