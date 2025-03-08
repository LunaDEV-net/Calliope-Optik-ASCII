serial.redirect_to_usb()

def onEvery_interval():
    serial.write_number(input.light_level())
    serial.write_line(r"\n")
loops.every_interval(500, onEvery_interval)
