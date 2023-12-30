def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    grains = 1 # number of grains on the first square

    if number == 1:
        return grains
        
    for squares in range(1, number):
        grains = grains * 2

    return grains   
    

def total():
    total_grains = 0
    
    for i in range(1, 65):
        total_grains += square(i)
        
    return total_grains
        
    
    
