
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


print(add_two_binary_strings("11", "11"))

