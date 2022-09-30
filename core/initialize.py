import json
from dotenv import load_dotenv

# return a list of links that you can get the news from
def initialize_rss_links():
    """Read in links from rss.txt, and return a list of rss urls."""
    rss_url_list = []
    with open("settings/rss.txt") as feeds:
        # read in the lines from rss.txt
        rss_url_lines = feeds.readlines()
        # for each line, strip any newline characters
        for line in rss_url_lines:
            # append the link to the list
            rss_url_list.append(line.strip())

    return rss_url_list


def initialize_settings():
    """Open settings.json and return the settings as a dictionary."""
    with open("settings/settings.json") as settings:
        return json.load(settings)


def initialize_env_variables():
    load_dotenv()
