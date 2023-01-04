#!/usr/bin/env python

def encript(key,text):
    """This function accept an encription key (negative or positive) and a text to convert following the
    Caesar encription. If the key K is negative the encription correspond to a decription of an encripted text
    with key |K|. 
    The function returns a string with the encripted text
    """

    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ" # TODO: command to insert a custom alphabet
    alph_len = len(alph)
    encription = {alph[i]:alph[(i+key)%alph_len] for i in range(alph_len)} # for performance reasons I use prebuilt dictionaries

    encripted_text = ""
    # Cycle on the text's characters
    for character in text:
        # Perform encription only if the character is an alphabetic one
        if character.isalpha():
            # If the character is lowercase, change in uppercase and remember to change it back after encription 
            if character.islower():
                upper_character = character.upper()
                case_changed = True
            else:
                upper_character = character
                case_changed = False
            encripted_character = encription[upper_character]
            if case_changed:
                encripted_character = encripted_character.lower()
        else:
            encripted_character = character
        encripted_text += encripted_character
            
    return encripted_text

if __name__=="__main__":
    import sys
    # Reads the arguments (there are no controls here because this module is expected 
    # to be used only with the caesar.sh script, that already have controls)
    decript = int(sys.argv[3])
    abs_key = int(sys.argv[1])
    file_name = str(sys.argv[2])
    # Transform the key including decription in only one function.
    key = abs_key * (1-2*decript)
    file = open(file_name, "r")
    text = file.read()

    encripted_text = encript(key,text)
    print(encripted_text)