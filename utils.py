import requests
import os


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


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


"""
def send_image_url(id, img_url):
    pass
"""
def send_button_message(id, URL, buttons):
    
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    if buttons == 1:
        payload = {
            "recipient": {"id": id},
            "message": {
                "attachment":{
                    "type":"template",
                    "payload":{
                        "template_type":"button",
                        "text":"嗨~需要什麼幫忙呢?",
                        "buttons":[
                        {
                        "type":"postback",
                        "payload":"HI_PAYLOAD",
                        "title":"教室查詢"
                        },
                        {
                        "type":"postback",
                        "payload":"HI_PAYLOAD",
                        "title":"課程查詢"
                        }#,
                        # {
                        # "type":"postback",
                        # "payload":"HI_PAYLOAD",
                        # "title":"google map"
                        # }
                    ]
                }
            }
        }
        }

    elif buttons == 0:
        payload = {
            "recipient": {"id": id},
            "message": {
                "attachment":{
                    "type":"template",
                    "payload":{
                        "template_type":"button",
                        "text":"系館教室連結~",
                        "buttons":[
                        {
                        "type":"web_url",
                        "url":URL,
                        "title":"點我借教室!!"
                        }
                    ]
                }
            }
        }
        }

    else:
        payload = {
            "recipient": {"id": id},
            "message": {
                "attachment":{
                    "type":"template",
                    "payload":{
                        "template_type":"button",
                        "text":"成功大學網路選課系統",
                        "buttons":[
                        {
                        "type":"web_url",
                        "url":URL,
                        "title":"快來搶課吧!!"
                        }
                    ]
                }
            }
        }
        }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

