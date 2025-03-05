# ''' 
# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user 
# enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and 
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
# match the output below.

# '''

##code

mini, maxi = None, None

while True:
    s_num = input('enter a number: ')

    if s_num == 'done':
        break

    try:
        f_num = float(s_num)
    except:
        print('invalid input') 
        continue

    # to find maximum number
    if maxi is None:
        maxi = f_num
    elif f_num > maxi:
        maxi = f_num

    # to find minimum number
    if mini is None:
        mini = f_num
    elif f_num < mini:
        mini = f_num        

print('Maximum is', maxi)
print('Minimum is', mini)        
    


