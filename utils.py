import requests
import json

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAP1jiIKT64BAHbMmQ2g7zDBnOISQK4VcTZBfluCFVhpkPsFhKaT6pOk2ZCYlul5Q2gs7YIc11nI5HJ8McLhF9WEBot2XSqja6RJaoor8SBiZCVw2NAgQUi409VM89TYH5UZCysumJdRQmKinE9QDi3fGYWZBlDZApZB5Dq4YEXIwZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


def send_img_message(fb_id, image_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)

    response = {
        "attachment": {
            "type": "image",
            "payload": {
                "url": image_url,
                "is_reusable": True
            },
        }
    }
    response_msg = json.dumps({"recipient": {"id": fb_id}, "message": response})
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=response_msg)

    if response.status_code != 200:
        print("Unable to send img message")
    return response


def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)

    payload = {
        "recipient":{"id":id},
        "message":{
            "attachment":{
                "type": "template",
                "payload":{
                    "template_type": "button",
                    "text": text,
                    "buttons": buttons
                }
            }
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
HERE
"""
