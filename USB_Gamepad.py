#!/usr/bin/python3.5

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event12')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:

                if keyevent.keycode[0] == 'BTN_A':
                    print ("left")
                elif keyevent.keycode[0] == 'BTN_NORTH':
                    print ("up")
                elif keyevent.keycode == 'BTN_C':
                    print ("Right")
                elif keyevent.keycode[0] == 'BTN_B':
                    print ("down")

