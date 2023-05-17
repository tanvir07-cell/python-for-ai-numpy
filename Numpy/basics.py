import numpy as np
# creating a numpy from list:
# l = [1,2,3,4];

# n = np.array(l);
# print(type(n));

# creating a multidimensional(2*3) numpy array:
npArray = np.array([[1,2,3],[4,5,6]])
# print(npArray)

# creating a random number from numpy array(1 dimensional):
randomNum = np.random.rand(3)


# creating multidimensional(3*2) random array:
randomNum = np.random.rand(3,2)

# creating a random integer number and it doesn't return any array:
randomNum = np.random.randint(1,10)


# creating a random integer number and it returns an array:
# er means hocceh 1-10 er moddeh random number generate kore dibe and prottekbar 5 ti kore number ei array te thakbe:
randomNum = np.random.randint(1,10,5)

# print(randomNum);

# arange():
# 1 - 9 obdi data ei arangeNum array er moddeh jabe:
arangeNum = np.arange(1,10)
# print(arangeNum)

# creating a diagonal array:
diagonalArray = np.eye(3,3);
# print(diagonalArray)

# creating a zero's of all array's element:
zerosArray = np.zeros((2,3));
# print(zerosArray);

# all items 1 inside the array:
onesArray = np.ones((2,3));
print(onesArray)











