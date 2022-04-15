def message():
    """
    input = None
    output = tuple with message(string)  and shiftnumber(int) for encoding/decoding
    """
    message = input("Type your message:\n")
    
    flag = True
    shift_number = None 
    while flag:
        try:
            shift_number = int(input("Type the shift number:\n"))
            flag = False
        except:
            print("That is not a number, try again")
    return (message, shift_number)


def encode(message, shift_number):
    """
    input = message to encode, shiftnumber for encoding
    function converts message into an encrypted message based on the shiftnumber 
    output = string with encoded message
    """
    print("entering encoding...")
    cipher = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,./<>?!@#$%^&*(){}[];:'"
    indices = []
    word = ""
    for letter in message:
        ind = cipher.index(letter)
        if (ind + shift_number % len(cipher))  >= len(cipher):
            word += cipher[ind + (shift_number % len(cipher)) - len(cipher)]
        else:
            word += cipher[ind + (shift_number % len(cipher))]
    return word


def decode(encrypted_message, shift_number):
    """
    input = string: message to decode, int: shiftnumber
    function converts encrypted message back to the original message
    output = string with original message 
    """
    print("entering decoding...")
    cipher = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,./<>?!@#$%^&*(){}[];:'"
    indices = []
    word = ""
    for letter in encrypted_message:
        ind = cipher.index(letter)
        if (ind - shift_number % len(cipher)) < 0:
            word += cipher[ind - (shift_number % len(cipher)) + len(cipher)]
        else:
            word += cipher[ind - (shift_number % len(cipher))]
    return word


def menu():
    print("e - Encode your message\n")
    print("d - Decode your message\n")
    print("q -Quit\n")
    
while True:
    menu()
    choice = input("What do you want to do?\n")
    if choice.lower() == "e":
        e_message = message()
        encoded = encode(*e_message)
        print(encoded)
    elif choice.lower() == "d":
        d_message = message()
        decoded = decode(*d_message)
        print(decoded)
    elif choice.lower() == "q":
        print("Thank you for using Caesar's Cipher\nGoodbye!\n")
        break
    else:
        print("That's not a valid choice.\n")
        continue

