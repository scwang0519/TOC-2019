from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "123456789000"
machine = TocMachine(
    states=[
        'user',
        'dogs',
        'cats',
        'others',
        'pic_dogs',
        'pic_cats',
        'corgipic',
        'huskypic',
        'shibainupic',
        'kittenpic',
        'catpic'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'dogs',
            'conditions': 'is_going_to_dogs'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'cats',
            'conditions': 'is_going_to_cats'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'others',
            'conditions': 'is_going_to_others'
        },
        {
            'trigger': 'advance',
            'source': 'dogs',
            'dest': 'pic_dogs',
            'conditions': 'dogs_to_pic_dogs'
        },
        {
            'trigger': 'advance',
            'source': 'cats',
            'dest': 'pic_cats',
            'conditions': 'cats_to_pic_cats'
        },
        {
            'trigger': 'advance',
            'source': 'pic_dogs',
            'dest': 'corgipic',
            'conditions': 'to_corgipic'
        },
        {
            'trigger': 'advance',
            'source': 'pic_dogs',
            'dest': 'huskypic',
            'conditions': 'to_huskypic'
        },
        {
            'trigger': 'advance',
            'source': 'pic_dogs',
            'dest': 'shibainupic',
            'conditions': 'to_shibainupic'
        },
        {
            'trigger': 'advance',
            'source': 'pic_cats',
            'dest': 'kittenpic',
            'conditions': 'to_kittenpic'
        },
        {
            'trigger': 'advance',
            'source': 'pic_cats',
            'dest': 'catpic',
            'conditions': 'to_catpic'
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
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
