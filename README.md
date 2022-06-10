# Hamming-distance

Hamming distance
In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols
are different. In other words, it measures the minimum number of substitutions required to change one string into the other, or the minimum
number of errors that could have transformed one string into the other. (Wikipedia)

Now you are going to write a program that will compare strings based on their Hamming distance.

Write a function which takes two parameters: a string and a list of strings in which the strings have the same length as the 
first parameter. The function returns a new list. The return value contains the strings with a hamming distance less than or
equal to (<=) 3 compared to the first parameter.

Example 1
Input text
"apple"
Input array
["apple", "apply", "tuple", "alter"]

Output
["apple", "apply", "tuple"]

Example 2
Input text
"monkey"

Input array
["donkey", "monday", "shaker"]

Output
["donkey", "monday"]
