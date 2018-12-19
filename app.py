from bottle import route, run, request, abort, static_file

from fsm import TocMachine

VERIFY_TOKEN = "123456789"
machine = TocMachine(
    states=[
        'user',
        'help',
        'find course',
        'talk',
        'classroom',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'help',
            'conditions': 'is_going_to_state0'
        },
        {
            'trigger': 'advance',
            'source': 'help',
            'dest': 'find course',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'talk',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'help',
            'dest': 'classroom',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'go_4',
            'source': 'find course',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'go_5',
            'source': 'state4',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'go_6',
            'source': 'classroom',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'go_7',
            'source': 'state6',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'go_back',
            'source': [
                'talk',
                'state8'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'go_user',
            'source': [
                'state5',
                'state7'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    # return 'OK'
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state == "find course":
            machine.go_4(event)
            return 'OK'
        elif machine.state == "state4":
            machine.go_5(event)
            return 'OK'
        elif machine.state == "classroom":
            machine.go_6(event)
            return 'OK'
        elif machine.state == "state6":
            machine.go_7(event)
            return 'OK'
           
        machine.advance(event)
        print(machine.state)
        return 'OK'


# @route('/show-fsm', methods=['GET'])
# def show_fsm():
#     machine.get_graph().draw('fsm.png', prog='dot', format='png')
#     return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
