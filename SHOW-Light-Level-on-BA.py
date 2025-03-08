def on_button_event_a():
    basic.show_number(input.light_level())
input.on_button_event(Button.A, input.button_event_click(), on_button_event_a)
