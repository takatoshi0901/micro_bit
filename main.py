def on_pin_pressed_p0():
    led.plot(2, 2)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global Display
    Display = Display / 2
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Display
    Display = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global Display
    Display = input.compass_heading()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Display
    Display = Display * 2
input.on_button_pressed(Button.B, on_button_pressed_b)

Display = 0
Display = 1

def on_forever():
    basic.show_number(Display)
basic.forever(on_forever)
