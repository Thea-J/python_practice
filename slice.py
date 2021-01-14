# Slice Syntax: sequence[start:stop:step] 
x = "Hello World"

#Slice x[0:5:1] = "Hello"
y = x[:5]

#Slice x[4:-3] = "o Wo"
y = x[4:-3]

#Slice x[0:N:-1] = "dlroW olleH"
y = x[::-1]