import time
import winsound
import pyttsx3
from plyer import notification

def water_reminder(interval_seconds=10):
    """
    Sends notification, plays beep, and speaks reminder every given seconds.
    """

    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    try:
        while True:
            # 🔔 Beep sound
            winsound.Beep(1000, 800)

            # 💻 Desktop notification
            notification.notify(
                title="💧 Water Reminder!",
                message="Hey Nitesh Negi, please drink water 💧",
                timeout=5
            )

            # 🗣 Speak reminder
            engine.say("Hey Nitesh Negi, please drink water.")
            engine.runAndWait()

            print("Reminder sent! Waiting for next alert...")
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nWater reminder stopped by user.")

# Run every 10 seconds
water_reminder(10)
