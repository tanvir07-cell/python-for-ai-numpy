# write a code that takes in a positive integer "x" from the user and creates a 1*10 array with random numbers ranging from 0 to "x"

import numpy as np;
x = int(input("Enter any number : "));

randomNum = np.random.randint(0,x,10)
print(randomNum)
