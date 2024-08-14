alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift(offset):

    sentence = input("enter sentence")
    new_sentence = '"udymts nx kzs!"'

    for letter in sentence:

        letter = letter.lower() 

        if letter.isalpha():
            shift_pos = alphabet.index(letter) + offset
            new_pos = alphabet[shift_pos]
            new_sentence += new_pos

        

        elif ' ' or '/t' or '/n' in letter: 
            new_sentence += letter

        elif letter.isnumeric(): 
            new_sentence += letter

        else:
            print ("python is fun")

    print(new_sentence)


shift(-21)
