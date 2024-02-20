import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def get_email_client():
    if "sendgrid_api_key.txt" not in os.listdir():
        raise Exception("Make sure sendgrid API key is in \"sendgrid_api_key.txt\"!")
    with open("./sendgrid_api_key.txt") as f:
        api_key = f.read()
    sg_email_client = SendGridAPIClient(api_key)
    return sg_email_client

def send_email(email_client, from_email, to_email, subject, html_content, debug=False):
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_content)

    response = email_client.send(message)

    if debug: 
        print(response.status_code, response.body, response.headers)


if __name__ == "__main__":
    email_client = get_email_client()

    send_email(
        email_client=email_client,
        from_email="warnnotifier@gmail.com",
        to_email="yash.saxena@utexas.edu",
        subject="Example subject",
        html_content="<strong>Example bolded content</strong>"
    )