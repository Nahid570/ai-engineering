# Ask user for their name and greet them

"""
This is a comment!
strip() is a method that removes any leading and trailing whitespace from the input string. This ensures that if the user accidentally adds extra spaces before or after their name, it won't affect the greeting.
"""
first, last = input("what's your name? ").strip().title().split(" ")
print(f"hello, {first}!")