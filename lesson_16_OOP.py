#Lesson 16, Object oriented programming

#Procedural Programming
#OOP is reusing certain parts of the code to do things
#the most import part of a reusable object are attributes and methods


#objects are a way of company data and functionality with that data

#the blueprint for an object is called a class
#to create an object from a blueprint,
#we have to inject data into a class

#CLASS EXAMPLE
from car import CarBlueprint()

car = CarBluperint()
#Classes are never underscored, they are camel cased

#a funciton tied to an object is called a method
#e.g.
my_screen = my_screen()
#ALLOWS THE FUNCTION TO RUN, BUT EXITS WHEN SCREEN IS CLICKED

my_screen.exitonclick()

my_screen.exit

#USING PRETTY TABLE PACKAGE
from prettytable import PtrettyTable
table = PrettyTable()
table.add_column('Pkemon', ['Pikachu'])
table.add_column('type', ['fire'])
#maybe i want to align left
table.align = 'l'
print(table)
#COFFEE EXERCISE IN OOP
----->