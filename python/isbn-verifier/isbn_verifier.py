def is_valid(isbn):

    isbn = isbn.replace('-','')
    ten_digits = len(isbn) == 10
    
    if not ten_digits:
        return False
    
    numbers_X = isbn[0:9].isnumeric() and (isbn[9].isnumeric() or isbn[9] == 'X')
   
    if not numbers_X:
        return False
        
    checksum = 0
    factor = 10

    for i in range(0, 9):
        checksum += int(isbn[i]) * factor
        factor -= 1
        
    if isbn[-1] == 'X':
        checksum += 10
    else:
        checksum += int(isbn[-1])
    
    if checksum % 11 == 0:
        return True
    return False
