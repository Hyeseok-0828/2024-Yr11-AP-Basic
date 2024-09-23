#1 
print('Welcome to the math quiz')
print()
print('Please enter whole numbers only')

# get input
# ask user for name
name =input("What is your name? ")

# ask user for two numbers
num_1 = float(input('What is your favorite number? ')) # num_1 is a variable. int converts the input to an integer
num_2 = float(input('Enter your second favorite number? '))
num_3 = float(input('What is your favorite number? ')) # num_1 is a variable. int converts the input to an integer, float은 소수점 
num_4 = float(input('Enter your second favorite number? '))
# add numbers together 
sum_of = num_1 + num_2
sum_of_3_4 = num_3 + num_4

# multiply numbers together
multiply = num_1 * num_2

# greet user and display added numbers 
print (f"kia ora {name}")
print (f"{num_1} + {num_2} = {sum_of}") # Print mean showing the answer to user
print (f"{num_3} + {num_4} = {sum_of_3_4}")
print (f"{num_1} X {num_2} = {multiply}")
#print (f"{num_3} X {num_4} = {multiply}")
