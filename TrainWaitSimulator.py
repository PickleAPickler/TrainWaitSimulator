
import time

# Making a simulator that waits for a train. We will need: #

"""


wait_train() function
closing_door() function
while loop on time
while loop on time door is taking to close

Version I:

Keep it simple. Just have a list of trains + their times
You choose a train, you wait X seconds, you're given the option:
 Ready to board y/n?
 Y = you have borded the train!
 N = choose another train or press 'X' to leave the station

Ideas:

- Have list + times continually updating e.g., When Nottingham train goes, update the list with a new train + destination

"""

print('Welcome to the train wait simulator!')
print('These are the trains and when they arrive: \n' \
'Nottingham | 1 min \n' \
'London | 30 secs \n' \
'Sandhurst | 10 secs')
print(input('Choose which train you want to wait for: ')) 


Trains = ['Nottingham', 'London', 'Sandhurst']

