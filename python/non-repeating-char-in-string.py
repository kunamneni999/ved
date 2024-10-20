'''
Problem: Find the First Non-Repeating Character in a String
Problem Statement:
Given a string, find the first character that does not repeat. If all characters repeat, return None.

Example:
Input:

s = "leetcode"
Output:

'l' (since 'l' is the first character that doesn't repeat)
Input:

s = "aabbcc"
Output:

None (since all characters repeat)
Constraints:
The input string will only contain lowercase English letters.
Tasks:
Implement a function that uses a hash map (dictionary) to count the occurrences of each character.
Iterate through the string to find the first character with a count of 1.
Bonus (Optional):
Try to solve the problem in O(n) time complexity, where n is the length of the string
'''