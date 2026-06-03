# def count_vowels(text):
#     vowels="aeiou"
#     vowels_count=0

#     clean_text = text.lower()

#     for char in clean_text:
#         if char in vowels:
#             vowels_count += 1
#         return vowels_count

# print(count_vowels(""))

def count_vowels(text):
    # 1. Define what we are looking for (all in lowercase)
    vowels = "aeiou"
    vowel_count = 0
    
    # 2. Convert the entire input text to lowercase to handle case-insensitivity
    clean_text = text.lower()
    
    # 3. Loop through each character in the string
    for char in clean_text:
        # Check if the character is one of our vowels
        if char in vowels:
            vowel_count += 1  # Add 1 to our counter
            
    return vowel_count

# Test Cases
print(count_vowels("Hello World"))    # Output: 3 (e, o, o)
print(count_vowels("PYTHON rules"))   # Output: 3 (o, u, e)
print(count_vowels("bcdfg"))          # Output: 0