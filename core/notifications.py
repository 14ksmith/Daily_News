from twilio.rest import Client
import os
import smtplib


def send_text(rss_feed, text_body):
    """Send text with news headlines/links/publishing dates."""
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    message = client.messages.create(
        body=f"{rss_feed}\n\n{text_body}",
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("USER_PHONE_NUMBER"),
    )
    print(message.status)


def send_email(rss_feed, email_body, server):
    """Send email with news headlines/links/publishing dates."""

    email_body = email_body.encode("ascii", "ignore")
    email_body = email_body.decode()

    with smtplib.SMTP(server, port=587) as connection:
        connection.starttls()
        connection.login(os.getenv("FROM_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("FROM_EMAIL"),
            to_addrs=os.getenv("TO_EMAIL"),
            msg=f"Subject:{rss_feed}\n\n{email_body}.",
        )

    print("Email has been sent")
