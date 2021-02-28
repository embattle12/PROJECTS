import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water",
            message="The National Academics of Science Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups(3.7 liters) of fluide for men. About 11.5 cups(2.7liters) of fluid for women.",
            timeout=10
    )
    time.sleep(60*60)
