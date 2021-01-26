#Declare a class called Counter
#To create an instance of Counter do Counter()

class Counter:
     def __init__(self):   # define __init__ method passing self
         self.count = 0    # set instance attribute count to 0
         
     def increment(self):  # define increment method passing self
         self.count += 1   # add 1 to instance attribute count
        
c1 = Counter()             # create Counter instance
c2 = Counter()             # create another instance
c1.increment()             # increment counter for c1
c1.count                   # count is 1
c2.count                   # count is 0