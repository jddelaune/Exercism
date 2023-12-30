def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # find the factors
    factors = [n for n in range(1, number) if number % n == 0]
    
    # calculate the aliquot sum
    aliquot = sum(factors)
    
    # classify the number
    if number == 1:
        return 'deficient'
    
    if number == aliquot:
        return 'perfect'

    if number < aliquot:
        return 'abundant'

    if number > aliquot:
        return 'deficient'

    
