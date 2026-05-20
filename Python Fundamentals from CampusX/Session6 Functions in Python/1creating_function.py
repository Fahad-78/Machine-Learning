def  is_even(num): # num is parameter
    """
    This function return is the number is odd or even
    input - any valid integer
    output - even/odd
    created - 04th april 2026
    """

    if num%2 == 0:
        return 'even'
    else:
        return 'odd'

#function
#function_name(input)
while True:
    user_input = input("Enter a number (or 'q' to quit): ") 
    
    if user_input == "q":
        print("Goodbye!")
        break
    try:
        x = is_even(int(user_input)) #user_input is argument
        print(x)
    except:
        print("Invalide input. Please enter only valid integer or 'q' to quit.")

print(is_even.__doc__)