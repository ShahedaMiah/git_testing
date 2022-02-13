pin = 4321
attempts_allowed = 3
attempt = 1
# want to calculate how many attempts left
supplied_pin = int(input('Enter Your 4 Digit Pin: '))
# allows user to input a 4 digit pin using 'int'(intergers)
while attempt <= attempts_allowed:
# the loop will run whist the 'attempt value is smaller than or equal to 'attempts_allowed' value
    if supplied_pin != pin:
    # 'supplied_pin' is not equal to 'pin'
        print('Pin is incorrect')
        print('This was your', (attempt), 'out of', (attempts_allowed), 'attempt')
        # takes the value of 'attempt' and 'attempts_allowed' variables and inputs into print string
        attempt += 1
         # increases the 'attempt' value by adding 1 to the 'attempt' value at th end of the loop, the new loop has an 'attempt' value that is 1 more than the loop just carried out
        print('You have', (attempts_left), 'attempt/s left')
        # can't figure out how to get the 'attempt' value to increase
        attempts_left = attempts_allowed - attempt
        if attempt <= attempts_allowed:
        # 'if' nested in an 'if'
            supplied_pin = int(input('Enter Your 4 Digit Pin: '))
            # print the input line to allow t inout new attempt
    else:
        supplied_pin == pin
        print('Pin is correct')
        break
        # breaks the loop when the right pin is entered
else:
    print('Access denied, your card is now blocked and you need to contact your bank to unblock your card')