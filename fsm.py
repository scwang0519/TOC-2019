from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_button_message
from utils import send_img_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_dogs(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'go to dogs'
        return False

    def is_going_to_cats(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'go to cats'
        return False

    def is_going_to_others(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'go to others'
        return False

    def dogs_to_pic_dogs(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'pictures'
        return False

    def cats_to_pic_cats(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'pictures'
        return False


    def to_corgipic(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'corgipic'
            return False


    def to_huskypic(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'huskypic'
            return False


    def to_shibainupic(self, event):
        if event.get('postback'):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'shibainupic'
            return False


    def on_enter_dogs(self, event):
        print("I'm entering dogs")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering dogs")
        #self.go_back()

    def on_exit_dogs(self, event):
        print('Leaving dogs')

    def on_enter_cats(self, event):
        print("I'm entering cats")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering cats")
        #self.go_back()

    def on_exit_cats(self, event):
        print('Leaving cats')

    def on_enter_pic_dogs(self, event):
        print("ENTERING PIC_DOGS")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Corgi',
            'payload':'corgipic'
        },{
            'type':'postback',
            'title':'Husky',
            'payload':'huskypic'
        },{
            'type':'postback',
            'title':'Shiba Inu',
            'payload':'shibainupic'
        }]

        responese = send_button_message(sender_id, "Which kind of dogs?", buttons)

    def on_enter_pic_cats(self, event):
        print("ENTERING PIC_CATS")
        sender_id = event['sender']['id']
        buttons = [{
            'type':'postback',
            'title':'Kitten',
            'payload':'kittenpic'
        },{
            'type':'postback',
            'title':'Cat',
            'payload':'catpic'
        }]

        responese = send_button_message(sender_id, "Which kind of cats?", buttons)


    def on_enter_corgipic(self, event):
        print("SEND CORGI PIC")
        sender_id = event['sender']['id']

        responese = send_img_message(sender_id, "http://35.201.204.238/wp-content/uploads/2017/06/6342537513_5b6f4b0c09_b.jpg")


    def on_enter_huskypic(self, event):
        print("SEND HUSKY PIC")
        sender_id = event['sender']['id']

        responese = send_img_message(sender_id, "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/9/2/asset/buzzfeed-prod-fastlane-01/sub-buzz-3052-1494312731-1.jpg?downsize=800:*&output-format=auto&output-quality=auto")


    def on_enter_shibainupic(self, event):
        print("SEND SHIBA INU PIC")
        sender_id = event['sender']['id']

        #responese = send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/5/58/Shiba_inu_taiki.jpg")
        responese = send_img_message(sender_id, "https://www.catster.com/wp-content/uploads/2018/05/A-gray-cat-crying-looking-upset.jpg")






