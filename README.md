# caesarscode
This project will contain a simple script to encript and decript text files using the Caesar's Code. 
The usage follows the suggested instructions:
1) Put the files caesar.sh, caesar_function.py, test.txt in the same directory
2) From terminal set caesar.sh as executable. In Linux: 
  sudo chmod +x path/to/caesar.sh
3) Execute the script in the following way:
  path/to/caesar.sh key filename [-d | --decript]
  
  Arguments:
  key -> mandatory argument. Positive integer 0 to Inf
  filename -> mandatory argument. Is the path to the file to encript/decript
  -d -> optional argument. Insert this flag if you whant to decript a previously encripted file.
