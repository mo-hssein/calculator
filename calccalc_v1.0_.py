# This function is used to add two numbers, taking two arguments
def add(first_num, last_num):
    return first_num + last_num


# This function is used to divide two numbers, taking two arguments
def divide(first_num, last_num):
    if last_nam == 0:
        raise ValueError("Division by zero is not allowed")
    return first_num / last_num


# This function is used to multiply two numbers, taking two arguments
def multiply(first_num, last_num):
    return first_num * last_num


# This function is used to subtract two numbers, taking two arguments
def subtract(first_num, last_num):
    return first_num - last_num


# Processes used in our project
process = ["*", "-", "+", "/"]

# input takes the first number from the user
first_nam = int(input("Enter the first number :"))

# input that accepts the operation type from the user
the_process = str(input(f"Enter the process (*)  (-)  (+)  (/) : ").strip())

# # input takes the last number from the user
last_nam = int(input("Enter the last number :"))


# loop that repeats the loop if the user chooses an operation that is not supported by us
while the_process not in process:
    first_nam = int(input("We do not support this process\nEnter the first number : "))

    # input that accepts the operation type from the user
    the_process = str(input(f"Enter the process (*)  (-)  (+)  (/) : ").strip())

    # # input takes the last number from the user
    last_nam = int(input("Enter the last number :"))
else:
    # If conditional to check process
    if the_process == process[0]:
        print(multiply(first_nam, last_nam))
    elif the_process == process[1]:
        print(subtract(first_nam, last_nam))
    elif the_process == process[2]:
        print(add(first_nam, last_nam))
    elif the_process == process[3]:
        print(divide(first_nam, last_nam))
