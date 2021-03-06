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

    # Boiler plate code formatting the parameters into types that will be useful to us
    word_list = list(word)

    len_of_word_list = len(word_list)

    # Since the call is recursive so list and the index do not get redefined each iteration
    if index == None and reversed_word_list == None:
        index = 0
        reversed_word_list = []

    # Reverse the indexes
    reversal_indexes = (len_of_word_list - index)

    # Take those reversed indexes subscript the original list and append them to reversed
    # version of the original word list
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


# print(is_palindrome("race car!!"))

# STRING SEARCHING ALGORITHM


def prefix_table_recursively(pattern, list_holder=None, index_at_i=None, index_at_j=None):
    pattern_list = list(pattern)

    if index_at_i is None and index_at_j is None and list_holder is None:
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


def recursive_string_search(pattern, text, counter_for_pattern=None,counter_for_text=None, pattern_list=None,text_list=None):


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
        return('The pattern starts at the index %s'%(counter_for_text - counter_for_pattern))



    if pattern_list[counter_for_pattern] != text_list[counter_for_text] and counter_for_text < len(text_list):
        if counter_for_pattern > 1:
            counter_for_pattern = counter_for_pattern - prefix_table_recursively(pattern)[counter_for_pattern - 1]
        else:

            # Why do we have to increment the text counter if it is the pattern that is shifting by 1?
            counter_for_text += 1

    # If we are iterating through the text and the counter exceeds the length of the text
    # that means we could not find the pattern
    if counter_for_text > len(text_list):
        return 'Pattern is not present in text'

    return recursive_string_search(pattern,text,counter_for_pattern,counter_for_text,pattern_list,text_list)


# print(recursive_string_search('boy', 'The boy Matthew is actually someone who is worth looking up to boy' ))
# Have to track for the multiple occurences


def recursive_string_search_contains(text, pattern, text_counter=None, pattern_counter=None, text_list=None, pattern_list=None):


    if text_counter is None and pattern_counter is None and text_list is None and pattern_list is None:
        # The reason we are doing this is because since this function is recursive to save
        # memory so that these lists are not created every single time we only create them if they are set to none
        # therefore they are only created once and this is on the very first iteration so we can use them on every
        # iteration afterwards
        text_counter = 0
        pattern_counter = 0
        text_list = list(text)
        pattern_list = list(pattern)

    print('This is the length of the text list: %s and this is the text counter: %s' % (len(text_list), text_counter))

    # When approaching these recursive functions we want to always highlight the base cases
    # The first base case would be the error base case
    if text_counter > len(text_list):
        # If the counter for the text exceeds the length of the text that means that the pattern could not
        # be found in the provided text therefore return False
        return False

    # Now that we have highlighted the error base case then we want to write the rest of the conditionals and then put
    # the base case at the end what this case accounts for if the letter in the pattern matches the letter in the text
    if pattern_list[pattern_counter] == text_list[text_counter]:
        pattern_counter += 1
        text_counter += 1

    # And then this base case checks if the whole pattern was found in the provided text
    if pattern_counter == len(pattern_list):
        return True

    # This conditional checks if the letter in the pattern does not match the letter in the text and if more than one
    # element in the pattern matched because if so then we can apply the formula
    if pattern_list[pattern_counter] != text_list[text_counter] and text_counter < len(text_list):

        if pattern_counter > 1:
            # What this formula checks for is how many elements we can skip so we can save ourselves some unnecessary work
            pattern_counter = pattern_counter - prefix_table_recursively(pattern)[pattern_counter - 1]
        else:
            text_counter += 1


    return recursive_string_search_contains(text, pattern, text_counter, pattern_counter, text_list, pattern_list)

# print(recursive_string_search_contains('matthew', 'at'))


def recursive_brute_force_string_search(text, pattern, text_counter=None, pattern_counter=None,list_of_occurences=None):

    # Boilerplate code so certain elements do not get redefined every iteration of this recursive call
    if text_counter is None and pattern_counter is None and list_of_occurences is None:
        text_counter = 0
        pattern_counter = 0
        text_list = list(text)
        pattern_list = list(pattern)
        list_of_occurences = []

    # Lastly we have to handle the base case where the pattern did not end up being found in the text provided
    if text_counter > len(text) - 1:
        if len(list_of_occurences) == 0:
            return None
        return list_of_occurences

    # Now let us handle if the character in the pattern equals the character in the text
    if pattern[pattern_counter] == text[text_counter]:

        # If the character in the pattern is equal to character in the text then we want to increment both the
        # the text counter as well as the pattern counter so we can compare the next set of letters

        text_counter += 1
        pattern_counter += 1

    # Let us handle the case where the character does not equal the character in the text
    # character_in_pattern = pattern_list[pattern_counter]
    # if pattern_list[pattern_counter] != text_list[text_counter]:
    else:
        # If the characters do not match then we want to increment the text so we can essentially compare the
        # next letter in the text to the first character in the pattern as oppose to comparing the next letter in the
        # pattern to the first character in the text

        text_counter += 1

    # Now we have to handle our different base cases let us start with our stopping of the recursion base case
    if len(pattern) == pattern_counter and pattern_counter > 0:
        # So what is happening in this block of code, firstly what we are doing with this occurrences
        #  of pattern variable is that we are finding the first index where the successful pattern occurs

        occurrences_of_pattern = text_counter - pattern_counter
        print('The pattern you are looking for starts at index: %s' %(occurrences_of_pattern))

        # We then append those occurrences to a list so we can display it for the user
        list_of_occurences.append(occurrences_of_pattern)

        # pattern -= 1 This wont work becuase if we decrement it means we would be looking for a different pattern
        # where if we start at 0 we are looking for the same pattern again

        # Restart at the beginning of the pattern so we can keep looking for it in the rest of the text
        pattern_counter = 0


    # To make the function recursive we return the function call itself
    return recursive_brute_force_string_search(text, pattern, text_counter, pattern_counter, list_of_occurences)

print(recursive_brute_force_string_search('aaa', 'a'))


def string_search_boolean_return(string_search):
    if string_search is None:
        return False
    return True

# print(string_search_boolean_return(recursive_brute_force_string_search('abc', 'a'))) # The tests that do not work 'abc', 'ac'))) as well as the empty strings ''
# assert find_index('abc', 'ac') is None WE HAVE TO TEST THE CLOSE CASES


