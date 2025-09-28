# Practice Problem 1: Track Unique Visitors
# Task: Given a list of user IDs, return the number of unique visitors.

def count_unique_visitors(user_ids):
    unique_users = set(user_ids)
    return len(unique_users)

# Justification:
# A set is ideal for tracking unique values because it automatically removes duplicates.
# The insertion and lookup operations in a set are O(1) on average, making this efficient for large lists.


# Practice Problem 2: Browser History Navigation
# Task: Implement a simple browser history with back and forward functionality.

class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None

    def visit(self, url):
        if self.current:
            self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current

# Justification:
# Stacks are perfect for LIFO operations like browser history.
# Pushing and popping from a stack are O(1), making navigation fast and predictable.


# Practice Problem 3: Word Frequency Counter
# Task: Count how many times each word appears in a paragraph.

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Justification:
# A dictionary is ideal for key-value mapping, such as word → count.
# Lookup and update operations in a dictionary are O(1) on average.
