# Reduce eyestrain notification

# install plyer "pip install plyer" if it is not installed on your computer
from plyer import notification
import time

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Lola.ico", #create your own custom icon by converting a png file to .ico file at realfavicongenerator.net
        timeout = 20,
    )

if __name__ == '__main__':
    while True:
        notify("Time to pet Lola and look at the tree outside!", "It's important to rest your eyes.")
        time.sleep(1200)

