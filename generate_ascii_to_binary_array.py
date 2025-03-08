def ascii_to_binary_array(text):
    binary_array = []
    for char in text:
        binary_array.extend([int(bit) for bit in f"{ord(char):08b}"])
    return binary_array

start_byte = ascii_to_binary_array("\x02")  # ASCII Start of Text (STX)
hello = ascii_to_binary_array("HELLO")
stop_byte = ascii_to_binary_array("\x03")  # ASCII End of Text (ETX)

to_send = start_byte + hello + stop_byte
print(to_send)
