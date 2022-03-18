from socket import timeout
import time
from plyer import notification

if __name__== "__main__":

    notification.notify(
        title="Good Morning!",
        message="It's time for you to enter your tasks and a Time Table made",
        timeout=5
    )
