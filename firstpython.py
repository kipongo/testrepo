# creating a basic function to square all the numbers in a list.

def num_square(mylist):
    squared = []
    for num in mylist:
        squared.append(num**2)
    return squared
num_square([1,2,3,4,5])
