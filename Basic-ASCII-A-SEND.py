t = 1000
to_send = [0,1,0,0,0,0,0,1]
index = 0

def onEvery_interval():
    global index
    if to_send[index] == 1:
        basic.set_led_color(0xff0000)
    if to_send[index] == 0:
        basic.turn_rgb_led_off()
    index += 1
    if index > len(to_send) - 1:
        index = 0

loops.every_interval(t, onEvery_interval)
