#!/usr/bin/env python

def encript(key,text):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    alph_len = len(alph)
    encription = {alph[i]:alph[(i+key)%alph_len] for i in range(alph_len)} # for performance reasons I use prebuilt dictionaries

    encripted_text = ""
    for character in text:
        if character.isalpha():
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
    decript = int(sys.argv[3])
    abs_key = int(sys.argv[1])
    file_name = str(sys.argv[2])
    
    key = abs_key * (1-2*decript)
    file = open(file_name, "r")
    text = file.read()

    encripted_text = encript(key,text)
    print(encripted_text)