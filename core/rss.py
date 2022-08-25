import requests
from bs4 import BeautifulSoup
from core.notifications import send_text, send_email


def rss_scraping(settings, rss_links):
    """Scrape rss feeds, parse, and send texts for each feed."""
    # Try to scrape the rss feed
    for rss in rss_links:
        # For top articles, get title, link, and publishing date
        top_articles = ""
        try:
            response = requests.get(rss)
            # Set 'soup' variable to scraping xml output
            soup = BeautifulSoup(response.content, features="xml")
            print("Request successful")
            # find all articles in scraping output
            articles = soup.find_all("item")
            feed_title = soup.find("title").get_text()

            # Get top designated number of articles (assigned in settings) for each rss feed, and assign 'title', 'link', and 'date' variables
            for article in articles[0 : settings.get("num_articles")]:
                title = article.find("title").get_text()
                link = article.find("link").get_text()
                # Not all articles include date, need to see if 'pudDate' is present before assigning variable
                if article.find("pubDate"):
                    date = article.find("pubDate").get_text()
                else:
                    date = ""
                top_articles += f"{title}\n{link}\n{date}\n\n"

            # Check if the notification type is text or email, and send articles accordingly
            if settings.get("send_method") == "text":
                send_text(rss_feed=feed_title, text_body=top_articles)
            elif settings.get("send_method") == "email":
                send_email(
                    rss_feed=feed_title,
                    email_body=top_articles,
                    server=settings.get("email_server"),
                )
            else:
                print("Invalid sending method, please choose either 'text' or 'email'.")

        # If scraping doesn't work, print the exception
        except Exception as exception:
            print(f"Request failed: {exception}")
