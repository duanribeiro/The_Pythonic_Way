# Exercises from: https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/classes/exercisesclasses.html

# EXERCISE 1 ########################################################################################################################################################################
# Follow the steps:
# 1. Create a class, Triangle.
#     Its __init__() method should take self, angle1, angle2, and angle3 as arguments.
# 2. Create a variable named number_of_sides and set it equal to 3.
# 3. Create a method named check_angles.
#     The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
# 4. Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

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

my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# EXERCISE 2 ########################################################################################################################################################################
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

GodOfThunder = Songs(["You've got something about you", "You've got something I need", "Daughter of Aphrodite","Hear my words and take heed"])