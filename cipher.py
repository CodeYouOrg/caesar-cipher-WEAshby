alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift(offset):

    message = input("udymts nx kzs!:/n")
    new_message = ''

    for letter in message:

        letter = letter.lower() 

        if letter.isalpha():
            shift_pos = alphabet.index(letter) + offset
            new_pos = alphabet[shift_pos]
            new_message += new_pos

        

        elif ' ' or '/t' or '/n' in letter: 
            new_message += letter

        elif letter.isnumeric(): 
            new_message += letter

        else:
            print ("python is fun:/n")

    print(alphabet)


shift(-5)
