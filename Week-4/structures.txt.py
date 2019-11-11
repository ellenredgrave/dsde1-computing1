'''
structures.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containing the first and the last element
# of "the_list".
def first_and_last(the_list):
    '''lol'''
    return [the_list[0], the_list[-1]]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    '''part rev'''
    if end < beginning:
        raise ValueError('End larger than beginning!')
    return the_list[beginning:end][::-1] # hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    '''repeat at index'''
    first = the_list[0:index]
    mid = [index]*3
    second = the_list[index + 1:]
    final = first + mid + second
    return final


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    '''palindrome word'''
    return word.lower() == word.lower()[::-1]

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    '''palindrome sentence'''
    the_list = []
    for char in sentence:
        if char.isalpha():
            the_list.append(char.lower())
    return the_list == the_list[::-1]

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    '''concatenate sentences'''
    stsent1 = sentence1.strip()
    stsent2 = sentence2.strip()
    if not stsent1[0].isupper():
        raise ValueError('lol ur wrong')
    if stsent1[-1] not in ['.', '?', '!']:
        raise ValueError('plz punctuate your sentence')

    sentence3 = stsent1 + ' ' + stsent2
    return sentence3


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    '''index exists'''
    return key in dictionary

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    '''check value exists'''
    return value in dictionary.values()

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''merge dictionaries'''
    return {**dictionary1, **dictionary2}

if __name__ == '__main__':
    X = 0