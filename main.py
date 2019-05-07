#Import Statements for Program

#Cprint Package Import
from cprint import cprint

#Bloody Terminal Package Import
from bloodyterminal import btext

#User Input
fullName= str(input("Enter your full name: "))

#Combine user input and sentence
sentence = fullName + " watch this sentence flash in green which is excellent way to debug a program!"

#Print Statements in the Terminal

#Success Message
cprint(sentence, c='gF)

#Custom Message
btext.custom("This is a custom alert message", "You have reached the end of the program. Thanks!")
