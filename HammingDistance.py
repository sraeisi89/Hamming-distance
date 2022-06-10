# Hamming distance
# In information theory, the Hamming distance between two strings of equal length is the number of positions at which
# the corresponding symbols are different. In other words, it measures the minimum number of substitutions required to
# change one string into the other, or the minimum number of errors that could have
# transformed one string into the other.
# Now you are going to write a program that will compare strings based on their Hamming distance.
#
# Write a function which takes two parameters: a string and a list of strings in which the strings have the same length
# as the first parameter. The function returns a new list. The return value contains the strings with
# a hamming distance less than or equal to (<=) 3 compared to the first parameter.
#
# Example 1
# Input text
# "apple"
# Input array
# ["apple", "apply", "tuple", "alter"]
#
# Output
# ["apple", "apply", "tuple"]
#
# Example 2
# Input text
# "monkey"
#
# Input array
# ["donkey", "monday", "shaker"]
#
# Output
# ["donkey", "monday"]


a = "monkey"
arr = ["donkey", "monday", "shaker"]

def hamming_distance(target, word_list):
    final_result = []
    for word in word_list:
        similar_char = 0
        for i in range(len(target)):
            if target[i] == word[i]:
                similar_char += 1
        if len(target)-similar_char <= 3:
            final_result.append(word)
    print(final_result)

hamming_distance(a , arr)


def distance_calculation(string,list_of_strings):
    new_list = []
    for strings in list_of_strings:
        initializer = 0
        count = 0
        while initializer < len(string):
            if string[initializer] != strings[initializer]:
                count += 1
            initializer += 1
        if count <= 3:
            new_list.append(strings)
    return   f'The new list is {new_list}'

print(distance_calculation("apple",['apple', 'apply', 'tuple', 'alter']))