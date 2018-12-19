import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EEAAP1jiIKT64BAClk5A0ztCzjlNbCUXDqq2qXZCcGjufZA6WesWZBZBZCDYwZCTNZCYUtPZAhZBzGdeAhLKXZApc0Aa5qnc6ZAfZCgqH9vvJNsNPAv8AlOKJVA4dBsTgzHS81WZAcGf5kublbTGC2hl3UvRrQ23E8lpd8IKWuH2kZCPre4")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
