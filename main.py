import schedule
import time

import config
import notification_task
    
def schedule_daily_task(hour, minute):
    # Schedule the task to run every day at the specified time
    schedule.every().day.at(f"{hour:02}:{minute:02}").do(notification_task.execute)

    # Infinite loop to continuously check if the scheduled task should run
    while True:
        schedule.run_pending()
        time.sleep(60)  # Sleep for 60 seconds before checking again

def main():
    # Set the desired time (24-hour format)
    SCHEDULED_HOUR = config.get_configuration('scheduled_hour')
    SCHEDULED_MINUTE = config.get_configuration('scheduled_minute')

    # Start scheduling the daily task
    schedule_daily_task(SCHEDULED_HOUR, SCHEDULED_MINUTE)

if __name__ == "__main__":
    main()
