
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

result = message()

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
    print(shift_number)
    for letter in message:
        ind = cipher.index(letter)
        print(ind)
        if (ind + shift_number % len(cipher))  >= len(cipher):
            print("Groot shift_number")
            print(f"index cipher: {ind + (shift_number % len(cipher))}")
            word += cipher[ind + (shift_number % len(cipher)) - len(cipher)]
        else:
            word += cipher[ind + (shift_number % len(cipher))]
    print(word)
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
    print(encrypted_message, shift_number)
    for letter in encrypted_message:
        ind = cipher.index(letter)
        if (ind - shift_number % len(cipher)) <= len(cipher):
            print(ind - shift_number % len(cipher), len(cipher))
            print(f"index cipher: {ind - (shift_number % len(cipher)) + len(cipher)}")
            word += cipher[ind - (shift_number % len(cipher)) + len(cipher)]
        else:
            word += cipher[ind - (shift_number % len(cipher))]
    return word

encoded = encode(*result)
decoded = decode(encoded, result[1])

print(encoded, decoded)

