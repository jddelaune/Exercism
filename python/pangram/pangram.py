def is_pangram(sentence):
    alphabet = [l for l in 'abcdefghijklmnopqrstuvwxyz']

    for letter in alphabet:
        if letter not in sentence.lower():
            return False

    return True
