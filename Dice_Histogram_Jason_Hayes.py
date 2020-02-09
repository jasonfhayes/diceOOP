# Dice - count totals in user-defined number of rounds

import random

class Bin():
    def __init__(self, binIdentifier):
        # This method runs whenever you create a Bin object
        self.binIdentifier = binIdentifier

    def reset(self):
        # This is called when you start or restart
        self.counter = 0

    def increment(self):
        # Called when the roll total is the value of the binIdentifier
        self.counter += 1

    def show(self, nRoundsDone):
        # Called at the end to show the contents of this bin
        print(str(self.binIdentifier) + '\t' + str(self.counter) + '\t' + str('{:.2f}'.format((self.counter/nRoundsDone) * 100) + '%'))
        
# Build a list of Bin objects            
binList = [ ]  # start off as the empty list

# Here, you need to write a loop that runs 13 times (0 to 12)
for i in range(13):
    binList.append(Bin(str(i)))
    
# Main code loop begins here
while True:
    nRounds = input('How many rounds do you want to do? (or Enter to exit): ')
    if nRounds == '':
        break
    nRounds = int(nRounds)
    
    # Tell each bin object to reset itself
    for oBin in binList:
        oBin.reset()
    
    # For each round (build a loop, roll 2 die, add, increment):
    for i in range(nRounds):
        total = random.randrange(1,7) + random.randrange(1,7)
        binList[total].increment()
    
    # Print some information and headings:
    print()
    print('After', nRounds, 'rounds:')
    print()
    print('Value:\tCount:\tPercentage:')
    
    # Tell each bin to show itself
    for oBin in binList:
        if int(oBin.binIdentifier) >= 2:
            oBin.show(nRounds)
    
    # Print a blank line to seperate the previous run from the next
    print()

print('OK bye')