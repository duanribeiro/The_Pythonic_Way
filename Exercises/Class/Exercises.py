# Exercises from: https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/classes/exercisesclasses.html

# EXERCISE 1 ##############################################################################################################
# Follow the steps:
# 1. Create a class, Triangle.
#     Its __init__() method should take self, angle1, angle2, and angle3 as arguments.
# 2. Create a variable named number_of_sides and set it equal to 3.
# 3. Create a method named check_angles.
#     If the sum of self.angle1, self.angle2, and self.angle3 is equal 180 return True, else False.
# 4. Create a variable named my_triangle and set it equal to a new instance of your Triangle class.
#    Pass it three angles that sum to 180 (e.g. 90, 30, 60).
#    Print out my_triangle.number_of_sides and print out my_triangle.check_angles().
class Triangle:
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
# EXERCISE 2 ##############################################################################################################
# Define a class called Songs, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics. Lyrics a list.
# Inside your class create a method called sing_me_a_songthat prints each element of lyrics his own line. Define a varible:
# Call the sing_me_a_song method on this variable.
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)

GodOfThunder = Songs(["You've got something about you",
                      "You've got something I need",
                      "Daughter of Aphrodite",
                      "Hear my words and take heed"])
GodOfThunder.sing_me_a_song()
# EXERCISE 3 ##############################################################################################################
# Define a class called Lunch. Its __init__() method should have two arguments: self and menu. Where menu is a string.
# Add a method called menu_price. It will involve a if statement:
# if "menu 1" print "Your choice:", menu, "Price 12.00",
#  if "menu 2" print "Your choice:", menu, "Price 13.40",
#  else print "Error in menu".
# To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self) -> object:
        if self.menu == 'menu 1':
            print('Your choice: {} - Price: R$11.00'.format(self.menu))
        elif self.menu == 'menu 2':
            print('Your choice: {} - Price: R$13.40'.format(self.menu))
        else:
            print('Error in menu')

Paul = Lunch('menu 1')
Paul.menu_price()
# EXERCISE 4 ##############################################################################################################
# Define a Point3D class that inherits from object Inside the Point3D class,
# define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x,self.y,self.z.
# Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z).
# This tells Python to represent this object in the following format: (x, y, z).
# Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3.
# Finally, print my_point.
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
       return '({}, {}, {})'.format(self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print(my_point)
# Exercises from: https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/classes/exercisesclasses.html
