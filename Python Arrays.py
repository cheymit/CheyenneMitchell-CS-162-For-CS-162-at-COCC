import numpy as np #inport numpy for arrays

#Create array  - size 5x5 - 2dimensional means rows and columns - random number 1 through 100
array = np.random.randint(1, 101, size=(5, 5), dtype=int)

# Print the entire array - displays entire array in a 5x5 grid
print("Full Array:")
print(array)

print() #blank
# Print the number from the 2nd row, 3rd column - indexing starts at 0
print("Number at 2nd row, 3rd column:")
print(array[1, 2])

print() #blank
# Print the sum of all elements in the array
print("Sum of all elements:")
print(np.sum(array)) #calculates and prints the total sum of all the numbers in entire array

print() #blank
# Print the mean of each row
print("Mean of each row:")
print(np.mean(array, axis=1)) #calculates the mean of each row

print() #blank
# Print the maximum value in each column
print("Max value in each column:")
print(np.max(array, axis=0)) #calculates the the sum of each column
