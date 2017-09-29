# server.py
#
# Blair Sharpe
# September 29, 2017

import socket

from evdev import InputDevice, categorize, ecodes, KeyEvent

gamepad = InputDevice('/dev/input/event12')

# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:

    # establish a connection
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))

    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            keyevent = categorize(event)
            if keyevent.keystate == KeyEvent.key_down:

                if keyevent.keycode[0] == 'BTN_A':
                    message = "left"
                    clientsocket.send(message.encode('ascii'))
                elif keyevent.keycode[0] == 'BTN_NORTH':
                    message = "up"
                    clientsocket.send(message.encode('ascii'))
                elif keyevent.keycode == 'BTN_C':
                    message = "right"
                    clientsocket.send(message.encode('ascii'))
                elif keyevent.keycode[0] == 'BTN_B':
                    message = "down"
                    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
