
def message():
    """
    input = None
    output = tuple with message and shifnumber for encoding/decoding
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
    cipher = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,./<>?!@#$%^&*(){}[];:'"
    indices = []
    word = ""
    for letter in message:
        ind = cipher.index(letter)
        indices.append(cipher[ind + (shift_number % len(cipher))])
        word += cipher[ind + (shift_number % len(cipher))]
    print(word)
encode(*result)

