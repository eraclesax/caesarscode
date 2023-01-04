#!/usr/bin/env python

def encript(key,text):
    pass

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