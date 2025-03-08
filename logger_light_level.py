serial.redirect_to_usb()
t = 1000
threshold = 20

res = [0] 
def onEvery_interval():
    global res
    res.append(input.light_level())
loops.every_interval(t, onEvery_interval)

def on_button_event_a():
    global res
    res = [0]
input.on_button_event(Button.A, input.button_event_click(), on_button_event_a)

def on_button_event_b():
    serial.write_numbers(res)
input.on_button_event(Button.B, input.button_event_click(), on_button_event_b)
