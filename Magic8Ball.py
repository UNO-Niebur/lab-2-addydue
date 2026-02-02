#Magic8Ball.py
#Name: Addy Duering
#Date: 2/1/26
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers = ("Defintely NOT", "For Sure", "No clue", "Prolly not", "Fairly Likely")
  #Prompt the user for their question.
input("Enter Your Question Here")
  #Answer question randomly with one of the options from your earlier list.
response = random.choice(answers)
print(responce)

if __name__ == '__main__':
  main()
