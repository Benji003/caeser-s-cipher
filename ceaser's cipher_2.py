alphabet='abcdefghijklmnopqrstuvwxyz'
command=input("Enter a code or decrypt a message: ")
new_message=""
cipher_position=int(input("Enter a position: "))
if command=="code":
    message=input("Enter a message: ")
    for character in message:
        if character in alphabet:
            position=alphabet.find(character)
            new_position=(position+cipher_position)%26
            new_message+=alphabet[new_position]
        else:
            new_message+=character
    print(new_message)
elif command=="decrypt":
    message = input("Enter a message: ")
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            new_position = (position - cipher_position) % 26
            new_message += alphabet[new_position]
        else:
            new_message += character
    print(new_message)

