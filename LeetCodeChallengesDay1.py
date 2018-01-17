import string
import pdb

def add_two_binary_strings(string_1, string_2):
    # Goal of this function is to be able to add two binary strings

    # Convert both of the strings to digit lists


    binary_string_1_list = list(map(int, string_1))
    print(binary_string_1_list)

    binary_string_2_list = list(map(int, string_2))
    print( binary_string_2_list)

    string_1_count = 0

    string_2_count = 0

    more_than_one_digit_for_string_1 = []

    more_than_one_digit_for_string_2 = []

    len_of_binary_string_1_digit_list = len(binary_string_1_list)

    len_of_binary_string_2_digit_list = len(binary_string_2_list)

    for index, digit in enumerate(binary_string_1_list):
        power_position = len_of_binary_string_1_digit_list - index

        string_1_count = (2 ** (power_position - 1)) * digit
        more_than_one_digit_for_string_1.append(string_1_count)

    for index_2, digit_2 in enumerate(binary_string_2_list):
        power_position_2 = len_of_binary_string_2_digit_list - index_2

        string_2_count = 2 ** (power_position_2 - 1) * digit_2
        more_than_one_digit_for_string_2.append(string_2_count)

    new_string_1 = ''.join(map(str, more_than_one_digit_for_string_1))
    new_string_2 = ''.join(map(str, more_than_one_digit_for_string_2))

    return int(new_string_1) + int(new_string_2)


# print(add_two_binary_strings("11", "11"))

def palindromes(word):
    if word == word[::-1]:
        return True

    return False

def reverse_given_text(word):

    word_list = list(word)

    len_of_word_list = len(word_list)

    reversed_word_list = []

    for index, _ in enumerate(word_list):
        reversal_indexes = (len_of_word_list - index) - 1
        reversed_word_list.append(word_list[reversal_indexes])

    formatted_word = ''.join(reversed_word_list)
    return formatted_word



reversed_word_list = []


def reverse_text_recursively(word, index=None):
    word_list = list(word)

    len_of_word_list = len(word_list)


    if index == None:
        index = 0

    reversal_indexes = (len_of_word_list - index)

    reversed_word_list.append(word_list[reversal_indexes - 1])

    index += 1

    if index >= len(word_list):
        formatted_word = ''.join(reversed_word_list)
        return formatted_word



    return reverse_text_recursively(word, index)


# print(reverse_text_recursively('race car'))


def is_palindrome(word):

    new_word = word.replace(' ', '')

    formatted_word = new_word.lower()

    if type(word) != str:
        raise ValueError('Function undefined for illegitimate words')

    for character in string.punctuation:
        formatted_word = formatted_word.replace(character, '')

    if formatted_word == reverse_text_recursively(formatted_word):
        return True

    print(reverse_text_recursively(formatted_word))

    return False


# STRING SEARCHING ALGORITHM

def contains(text, pattern):
    '''Returns a boolean indicating whether or not a pattern occurs in text or not'''

    text_list = list(text)

    len_text_list = len(text_list)

    index = 0

    while len_text_list > 0:

        for word in pattern:
            if word == text_list[index]:
                return True
            return False

        index += 1
        len_text_list -= 1

list_holder = [0,0,0,0]



def prefix_table_recursively(text, index_at_i=None, index_at_j=None):
    text_list = list(text)
    # pdb.set_trace()

    if index_at_i == None and index_at_j == None:
        index_at_i = 0
        index_at_j = 1
        list_holder[index_at_i] = 0

    first_element = text_list[index_at_i]
    second_element = text_list[index_at_j]
    # pdb.set_trace()
    if first_element == second_element:
        list_holder[index_at_j] = index_at_i + 1
        index_at_i += 1
        index_at_j += 1

    if first_element != second_element and index_at_i != 0:
        index_at_i -= 1

    if index_at_i == 0 and first_element != second_element:
        list_holder[index_at_j] = 0
        index_at_j += 1

    # We need to stop the recursion
    if index_at_j >= len(text_list):
        return list_holder



    return prefix_table_recursively(text, index_at_i, index_at_j)

# print(prefix_table_recursively("aabaacaabaa"))
print(prefix_table_recursively("cacc"))





