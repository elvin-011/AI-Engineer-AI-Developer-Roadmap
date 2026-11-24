name = input("Whats your name:")            #the input function accepts a String from the CLI and the name variable stores that string in itself.if the value to be accepted is not String(eg: int,float,etc) use those before the input function).
print(f"hello,{name}")                      #the print function prints any value given inside its paranthesis and the 'f' string helps in printing a value which is stored in a variable by using it in t he print statement enclosed in '{ }'.
print("hello, ",name)                       #another way of adding variable values in print function but this automatically adds a space in between two arguments so extra spaces are unnecessary
print("hello, "+ name)                      #another way of letting values inside print function

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)  #official python doc for print statement
* objects means any number of objects can be added in the print function

sep=' ' means by default there is a seperator " " in between two arguments

end='\n' means at the end by default the cursor or the access goes to the next line,it can be made to end='' to not go the next line.

file =sys.stdout() means the output will be printed in the output terminal

flush=false means by default no clear screen will be initialised

"""
