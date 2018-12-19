from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message
# from bs4 import BeautifulSoup
# import requests
from find_course import course_url, find_classroom
department_list = ["E8", "E2", "F7", "E1", "E3", "E4", "E5", "E6", "E7", "A9"]
department_name = "F7"
class_num = "009"
date = "2018/12/24"
time = "8-9"
talk = "hi"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state0(self, event):
        if event.get("message"):
            print("in state0")
            # text = event['message']['text']
            return event['message']['text'].lower() == '小幫手'
        return False

    def is_going_to_state1(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            # print(department_list)
            # print("your entering :")
            # print(text)
            return text.lower() == '課程查詢'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            
            return text.lower() == 'hi'
            # return True
        return False

    def is_going_to_state3(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            #print(department_list)
            return text.lower() == '教室查詢'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            for tmp in department_list:
                if text.upper() == tmp:
                    print("i find it ", end=",")
                    print(tmp)
                    global department_name
                    department_name = tmp
                    # print(department_name)
                    return True
                else:
                    print("Not find department_num")
        return False

    def is_going_to_state5(self, event):
        # print("name", end = "=")
        # print(department_name)
        if event.get("message"):
            text = event['message']['text']
            global class_num 
            class_num = text
            return True
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            #get date
            global date
            date = text
            return True
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            #get time
            global time
            time = text
            return True
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            global talk
            talk = text
            return True
        return False

    def on_enter_state0(self, event):
        print("I'm entering state0")

        sender_id = event['sender']['id']
        send_button_message(sender_id, "hi", 1)

    def on_enter_state1(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請輸入系所代號 (Ex: F7)")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "hi")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入想要借的日期: (Ex:12/14)")

    def on_enter_state4(self, event):
        print("I'm entering state4")
        # course_url(department_name)
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入課程代號: (Ex:001)")

    def on_enter_state5(self, event):
        print("I'm entering state5")
        print(department_name + class_num)
        tmp = course_url(department_name, class_num)
        sender_id = event['sender']['id']
        send_text_message(sender_id, tmp)
        if tmp != '沒有這堂課喔~':
            send_button_message(sender_id, "https://course.ncku.edu.tw/course/signin.php", 2)
        self.go_user();

    def on_exit_state5(self):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入使用時段: (Ex:8-21)")

    def on_enter_state7(self, event):
        print("I'm entering state7")
        print(date + " "+ time)
        # find_classroom(date, time)
        tmp = find_classroom(date, time)
        sender_id = event['sender']['id']
        send_text_message(sender_id, tmp)
        send_button_message(sender_id, "http://www.csie.ncku.edu.tw/Class2014/class/2018/" + date, 0)
        self.go_user()

    def on_exit_state7(self):
        print('Leaving state7')

    def on_enter_state8(self, event):
        print("I'm entering state8")
        sender_id = event['sender']['id']
        send_text_message(sender_id, talk)
        self.go_back()

    def on_exit_state8(self):
        print('Leaving state8')