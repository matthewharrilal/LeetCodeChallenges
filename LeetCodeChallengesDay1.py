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



def reverse_text_recursively(word, reversed_word_list=None,index=None):
    word_list = list(word)

    len_of_word_list = len(word_list)


    if index == None and reversed_word_list == None:
        index = 0
        reversed_word_list = []

    reversal_indexes = (len_of_word_list - index)

    reversed_word_list.append(word_list[reversal_indexes - 1])

    index += 1

    if index >= len(word_list):
        formatted_word = ''.join(reversed_word_list)
        return formatted_word



    return reverse_text_recursively(word, reversed_word_list,index)


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

# print(is_palindrome("race car"))


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

# list_holder = [0,0,0,0,0,0,0,0]



def prefix_table_recursively(pattern,list_holder=None,index_at_i=None, index_at_j=None):
    pattern_list = list(pattern)
    # pdb.set_trace()

    if index_at_i == None and index_at_j == None and list_holder == None:
        index_at_i = 0
        index_at_j = 1
        list_holder = [0] * (len(pattern_list))
        list_holder[index_at_i] = 0


    first_element = pattern_list[index_at_i]
    second_element = pattern_list[index_at_j]
    if first_element == second_element:
        list_holder[index_at_j] = index_at_i + 1
        index_at_i += 1
        index_at_j += 1

    if first_element != second_element and index_at_i != 0:
        index_at_i -= 1
        first_element = pattern_list[index_at_i]

    if index_at_i == 0 and first_element != second_element:
        # print('This /is the first element: %s and this is the second element: %s' %(first_element,second_element))
        list_holder[index_at_j] = 0
        index_at_j += 1

    # We need to stop the recursion
    if index_at_j >= len(pattern_list):
        return list_holder



    return prefix_table_recursively(pattern ,list_holder,index_at_i, index_at_j)


def string_searching(pattern,text):

    # This is the boiler plate code for formatting the pattern and the text into lists as well as caculating the length of the texts
    pattern_list = list(pattern)
    text_list = list(text)

    pattern_length = len(pattern)

    text_length = len(text)

    # Creating a counter for the pattern and the index
    text_counter = 0
    pattern_counter = 0


    # Iterating through the text to look for the pattern, do not want a list index out of range error therefore we put the condition while the counter is less than the text length
    while text_counter < text_length:
        # So while iterationg through the text if we see there is a match we are going to increment both the counts so we can compare the next set of letters
        if pattern_list[pattern_counter] == text_list[text_counter]:
            text_counter += 1
            pattern_counter += 1

        # If the counter eventually iterates to be its full length then we know that the pattern has come to a full spin meaning we found the pattern
        # This answers the question when do we know if the full pattern was found?
        if pattern_counter == pattern_length:
            return("Found pattern at index %s" %(str(text_counter-pattern_counter)))


        # And then for the other case if the text is still being iterated through meaning the counter has not reached the full length of the text as well as the letter
        # that we are currently at in the pattern does not match the letter we are at in the text
        elif text_counter < text_length and pattern_list[pattern_counter] != text_list[text_counter]:
            # Whilst checking for that we also check if the pattern counter is zero
            if pattern_counter != 0:
                pattern_counter = prefix_table_recursively(text)[pattern_counter - 1]
            else:
                text_counter += 1

        # return("No pattern was found")


def recursive_string_search(pattern,text, counter_for_pattern=None,counter_for_text=None, pattern_list=None,text_list=None):
    #
    # if type(pattern) or type(text) != str:
    #     raise ValueError('Function is undefined for patterns other than strings')

    if counter_for_text is None and counter_for_pattern is None and pattern_list is None and text_list is None:
        counter_for_text = 0
        counter_for_pattern = 0
        pattern_list = list(pattern)
        text_list = list(text)

    if pattern_list[counter_for_pattern] == text_list[counter_for_text]:
        # If the letter in the pattern matches the letter in the text we want to increment the count by 1 for each
        #  to iterate to the next letter and
        # compare them
        counter_for_pattern += 1
        counter_for_text += 1

    if counter_for_pattern == len(pattern_list):
        print(counter_for_pattern,counter_for_text)
        return 'This is where the pattern starts: %s'%(counter_for_text - counter_for_pattern)


    if pattern_list[counter_for_pattern] != text_list[counter_for_text] and counter_for_text < len(text_list):
        if counter_for_pattern > 1:
            counter_for_pattern = counter_for_pattern - prefix_table_recursively(pattern)[counter_for_pattern - 1]
        else:

            # Why do we have to increment the text counter if it is the pattern that is shifting by 1?
            counter_for_text += 1

    # If we are iterating through the text and the counter exceeds the length of the text
    # that means we could not find the pattern
    if counter_for_pattern > len(text_list):
        return 'Pattern is not present in text'

    return recursive_string_search(pattern,text,counter_for_pattern,counter_for_text,pattern_list,text_list)


print(recursive_string_search('tthe', 'Matthew'))
print(string_searching('at', 'Matthew'))



# print(prefix_table_recursively("abababca"))
# print(string_searching("ab","aaab"))  # Since for now we are just testing the index functions then these are the tests that do not pass assert find_index('abc', '') == 0  # all strings contain empty string






