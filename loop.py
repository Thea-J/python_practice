# Define a for loop with a range iterator
# That prints each element in the range 
for i in range(5):
    print(i)


# Define a for loop using the enumerate() function    
for i, value in enumerate((1, 2, 3, 4, 5)): # Enumerate elements in a tuple
    if i % 2 == 0: #Continue loop for even indexes 
        continue
    print(value)  # Otherwise print the value

# enumerate method will return a tuple with (index, value)