def on_button_event_a():
    basic.show_number(input.light_level())
input.on_button_event(Button.A, input.button_event_click(), on_button_event_a)

"""
basic.set_led_color(0xffffff)

"""

"""
Normal in Box ~10
Mit Weißer LED >100
"""
