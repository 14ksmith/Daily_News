from datetime import datetime, timedelta
import time
from core.rss import rss_scraping
from core.initialize import (
    initialize_rss_links,
    initialize_settings,
    initialize_env_variables,
)


def start_news_cycle(rss_settings, rss_links):
    current_datetime = datetime.now()

    # set target time for text to send
    target_time = datetime.strptime(rss_settings.get("send_time"), "%H:%M")
    # have to change target_time date to current date
    target_time = target_time.replace(
        day=current_datetime.day,
        year=current_datetime.year,
        month=current_datetime.month,
    )

    # variable tracking if text has sent each day
    has_sent_news_today = False

    while True:
        current_time = datetime.now()

        if has_sent_news_today == False:

            # if current time is before target time
            if current_time < target_time:
                # sleep for amount of time diff between current time and target time
                sleeptime = (target_time - current_time).total_seconds()
                print(
                    f"It's not quite time yet. Only {round(sleeptime/60)} minutes until today's news is sent!"
                )
                time.sleep(sleeptime)

                print("Sending news!")
                # send text/email with top five articles from urls in rss.txt
                rss_scraping(settings=rss_settings, rss_links=rss_links)
                has_sent_news_today = True

            # if curent time is at or after target time
            else:
                print("Sending news!")
                # send text/email with top five articles from urls in rss.txt
                rss_scraping(settings=rss_settings, rss_links=rss_links)
                has_sent_news_today = True

        # If the news has already been sent today
        else:
            # create a new target time that is target time today, plus one day
            new_target_time = target_time + timedelta(days=1)
            # sleeptime is tomorrows target time minus current time (need to convert to seconds for sleep method)
            sleeptime = (new_target_time - current_time).total_seconds()
            print(f"Already sent today, waiting until {target_time.time()} tomorrow")
            time.sleep(sleeptime)
            # reset has_sent_news_today for next day to false
            has_sent_news_today = False


if __name__ == "__main__":

    # initialize env variables from .env
    initialize_env_variables()

    # settings from settings file
    rss_settings = initialize_settings()

    # links output from txt file
    rss_links = initialize_rss_links()

    # start sending news at the specified time on a loop
    start_news_cycle(rss_settings, rss_links)
