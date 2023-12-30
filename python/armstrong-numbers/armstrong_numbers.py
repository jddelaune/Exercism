def is_armstrong_number(number):
    number_of_digits = len(str(number))
    digits = [int(n) for n in str(number)]

    armstrong_test = 0
    
    for i in digits:
        armstrong_test = armstrong_test + i ** len(digits)

    return number == armstrong_test
