# Timed Challenge: "Find the first non-repeating character in a string"
# Given a string, return the first character that does not repeat. If all characters repeat, return None.

def first_non_repeating_char(s):
    from collections import OrderedDict

    freq = OrderedDict()
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char, count in freq.items():
        if count == 1:
            return char
    return None

# Test cases
print(first_non_repeating_char("aabbccddeeffg"))  # Output: 'g'
print(first_non_repeating_char("aabbcc"))         # Output: None
print(first_non_repeating_char("swiss"))          # Output: 'w'

# Reflection (200–300 words):
"""
I chose an OrderedDict for this challenge because it preserves insertion order while allowing fast lookups.
This is crucial for identifying the first non-repeating character in the original sequence.

The 30-minute time limit pushed me to prioritize readability and correctness over optimization.
I avoided more complex structures like heaps or custom linked lists, which might have added unnecessary overhead.

One trade-off I made was using Python’s built-in data structures instead of implementing my own.
This saved time but might be less impressive in a technical interview where low-level implementation is valued.

Overall, the time constraint helped me focus on simplicity and edge case coverage.
I tested with empty strings, all repeating characters, and mixed cases to ensure robustness.
This exercise reminded me how important it is to balance performance with clarity under pressure.
"""
