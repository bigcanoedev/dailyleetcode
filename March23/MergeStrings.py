"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the 
end of the merged string.

Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""

def merge_string_alt(a, b):
    """
    Merge Two Strings in alternating order.
    """
    new_string = ""
    len1 = len(a)
    len2 = len(b)

    #iterate in alternating order
    for i in range(max(len1,len2)):
        if i < len1:
            new_string += a[i]
        if i < len2:
            new_string += b[i]

    return new_string

print(merge_string_alt("abc", "pqr"))