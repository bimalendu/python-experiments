greeting = "heLLo woRld"
another_greeting = 'This world is beautiful'
length_greeting = len(greeting) 
print(length_greeting) #11
print(greeting.count("o")) #2
print(greeting.find("e")) #1
print(greeting.find("g")) #-1
print(greeting.upper()) #HELLO WORLD
print(greeting.lower()) #hello world
print(greeting.capitalize()) #HeLLo WoRld
num = "15"
print(num.isdigit()) #True
num = "15.7"
print(num.isdigit()) #False
print(greeting.isdigit()) #False
print(greeting.split(" ")) #["heLLo", "woRld"]
print(greeting.replace(" ","@")) #"heLLo@woRld"
print("Hello" * 3) # HelloHelloHello
print("Todays\"s Menu") #Today's Menu
multiline_string = """ Hello, This is a
Multiline string """
print("|".join(["c","a","t"])) #c|a|t
print("*".join(["c","a","t"])) #c*a*t
print(f"{greeting} and {another_greeting} also {greeting}") #f-strings to easily manipulate data or expressions in strings
