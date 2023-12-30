def translate(text):
# check if input is a multi-word phrase; if so, piggify each word and return
# the whole phrase. If not, piggify the single word and return it.
    
    if text.count(' ') > 0:
        piglatin = ''
        words = text.split(' ')
        for w in words:
            if piglatin: # if not empty string, add a space
                piglatin = piglatin + ' '
            piglatin = piglatin + piggify(w) 

        return piglatin

    return piggify(text)

def piggify(text):
  
    VOWELS = ['a','e','i','o','u']
    VOWELSY = ['a', 'e', 'i', 'o', 'u', 'y']

    text = text.lower()
    
    # get index of first vowel or y
    for i in range(0, len(text)):
        if text[i] in VOWELSY:
            first_vowel_idx = i
            break
    
    begin_vowel = text[0] in VOWELS
    begin_qu = text[first_vowel_idx] == 'u' and text[first_vowel_idx - 1] == 'q' 
    two_letter_word_end_in_y = len(text) == 2 and text[1] == 'y'
    begin_consonant = text[0].isalpha() and text[0] not in VOWELS
    begin_y = text[0] == 'y'
    begin_xr = text[0:2] == 'xr'
    begin_yt = text[0:2] == 'yt'

    if begin_vowel or begin_xr or begin_yt:
        return text + 'ay'

    if two_letter_word_end_in_y:
        return text[1] + text[0] + 'ay'
    
    if begin_qu:
        # do not treat the 'u' in 'qu' as a first vowel; keep it with 
        # consonants that get sliced and moved to end of word
        first_vowel_idx = first_vowel_idx + 1

    if begin_y:
        return text[1:] + text[0] + 'ay'        

    if begin_consonant:
        return text[first_vowel_idx:] + text[0:first_vowel_idx] + 'ay'
    

