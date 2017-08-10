from datetime import date
year = date.today().year
year = int (year)
name = input("Give me your name: ")
age = input("Enter your age: ")
when100 =  year+(100 - int (age))
when100 = str (when100)
howOften = int(input("How often should the message be displayed:")) 
print(howOften * (name +" will turn 100 in " + when100 + "\n"))