#add some title 
print('\nCHECK IF THE FIRST NUMBER ARE THE SAME.')

# this function is for checking numbers if the first and last are the same
def check(numbers):
    print('\nGIVEN: ', numbers)
#these are variable to define the numbers
    first_number = numbers[0]
    last_number = numbers[-1]

#this function checks if the given are correct or not
    if first_number == last_number:
       return True
      
    elif first_number != last_number:
        return  False