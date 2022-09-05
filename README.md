# Daily News

                                             ___________
                                            |.---------.|
                                            ||  DAILY  ||
                                            ||  NEWS   ||
                                            ||         ||
                                            |'---------'|
                                             `)__ ____('
                                             [=== -- o ]--.
                                           __'---------'__ \
                                          [::::::::::: :::] )
                                           `""'"""""'""""`/T\
                                                          \_/

## Overview

Daily News is a Python application that reads RSS feeds at a specified time every day and sends the top stories from each outlet either via email or text. Daily News is customizable, allowing the user to specify the time of day they want the news to be sent, how many articles from each news outlet and whether to have notifications via email or text. With 5 minutes and few easy steps, you can set up daily deliveries of news from your favorite news outlets.

## How to use Daily News

### Setup/Installation

To set up Daily News, first install the necessary packages from `requirements.txt`. You can do this by running `pip3 install -r requirements.txt`.

Next you will need to update the `settings.json` file with the following information. `send_time` specifies the time of day you want daily news to be sent to you. Make sure to use the 24-hour clock when designating your desired send time. `send_method` lets the program know to send the stories to you either via text or through email. `email_server` specifies the SMTP server to use if you are using email notifications. Finally, `num_articles` specifies how many articles to be sent from each outlet, every day.

Below is an example of the settings.json file

```json
{
  "send_time": "fillInHere",
  "send_method": "fillInHere",
  "email_server": "fillInHere",
  "num_articles": "fillInHere"
}
```

Next, we will set up notifications. If using email, follow the instructions under the `Email Notifications` section. Similarly, if using text, follow the instructions under `Text Notifications`.

### Email Notifications

1. Add an email address that you want daily articles to be sent to. You can add this address as the value for `TO_EMAIL` in the `.env` file.

2. Add the email address that will send notifications with the daily articles. You can add this as the value for `FROM_EMAIL` in the `.env` file. (This can be the same address as the `TO_EMAIL`, if desired).

3. Add the password for the `FROM_EMAIL` by setting the value of `EMAIL_PASSWORD` in the `.env` file.

### Text Notifications

1. Sign up for a [twilio account](https://www.twilio.com/) and get a free virtual number.

2. Add the virtual phone number to the `.env` file as the value for `TWILIO_PHONE_NUMBER`.

3. Add the phone number that will be receiving the notifications to the `.env` file as the value for `USER_PHONE_NUMBER`.

4. Get your Twilio account SID and add it as the value for `TWILIO_ACCOUNT_SID` in `.env`.

5. Get your Twilio Auth token and add it as the value for `TWILIO_AUTH_TOKEN` in `.env`.

### Running Daily News

Now you are all set to run the program! To start Daily News, simply run the program with `python3 main.py`. Every day at your specified time, the application will gather news from the rss feeds you provided and send you the top articles as a text or email!
