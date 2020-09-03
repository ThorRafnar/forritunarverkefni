user_int = 0
max_int = 0

while user_int >= 0:
    user_int = int(input("Input a number: "))
    if user_int > max_int:
        max_int = user_int   

print("The maximum is", max_int)

"""
initialize values
get user input while input is more than or equal to zero
    if user input is larger than max value
            user input is stored as max value
when negative number is put in, print max number
"""