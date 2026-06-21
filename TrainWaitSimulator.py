
# import time

# Making a simulator that waits for a train. We will need: #

"""

Prerequisite tasks/projects:

- Familiarity with    time   module
- Sleep module?
- Make a countdown timer 



Potential functions, variables etc... 

wait_train() function
closing_door() function
while loop on time
while loop on time door is taking to close

Version I:

Keep it simple. Just have a list of trains + their times
You choose a train, you wait X seconds, you're given the option:
 Ready to board y/n?
 Y = you have borded the train!
 N = choose another train or press 'X' to leave the stationx

Ideas:

- Have list + times continually updating e.g., When Nottingham train goes, update the list with a new train + destination

"""

# from datetime import datetime

# import time
# import random

# # right_now = datetime.today().minute
# # print('The time is' + right_now)

# # Experiment with    time: can we get the programme to wait? 
# wait_time = random.randint(1, 5)
# time.sleep(wait_time)

# print('Welcome to the train wait simulator!')
# print('These are the trains and when they arrive: \n' \
# 'Nottingham | 1 min \n' \
# 'London | 30 secs \n' \
# 'Sandhurst | 10 secs')

# Trains = ['Nottingham', 'London', 'Sandhurst']


# while True:
#     user_input = (input('Choose which train you want to wait for: ')) 
#     if user_input == "q":
#         break

#     if user_input not in Trains:
#         continue

#     """Output messages:"""
    
#     if user_input == 'Nottingham':
#         print('Have a nice time in Nottingham!')

#     if user_input == 'London':
#         print('Have a nice time in London!')

#     if user_input == 'Sandhurst':
#         print('Have a nice time in Sandhurst!')

################################ Class Homework ###########################################

"""
We are making objects. Ideas:

Buses, Trains, Alan, Guitars, Jiu-Jitsu Moves, Band members, skateboard tricks, Food. 
 Bloody anything mate! :)


"""

class Dog:

    species = "Canis familiaris" # this is a class  attribute - they keep the same for every instance

    def __init__(self, name, age):  # these are instance attributes - they vary from one instance to another
        self.name = name
        self.age = age    

my_dog = Dog('Milo', 8)

print(my_dog.name)


# def roll_over(self):
#     print(f'{self.name} loves to roll over')













