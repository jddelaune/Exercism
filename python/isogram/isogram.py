def is_isogram(string):
    characters = [char for char in string]

    for c in characters:
        if string.lower().count(c) > 1 and c.isalpha():
            return False

    return True
