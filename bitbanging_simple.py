t = 1000
to_send = [1,0,1,0,1,0,1,0]
for i in range(8*2):
    to_send.append(0) # Break
index = 0

def onEvery_interval():
    global index
    if to_send[index] == 1:
        basic.set_led_color(0xffffff)
    if to_send[index] == 0:
        basic.turn_rgb_led_off()
    index += 1
    if index > len(to_send) - 1:
        index = 0

loops.every_interval(t, onEvery_interval)
