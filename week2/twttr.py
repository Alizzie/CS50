user_input = input("Input: ")


vowels = ['A','E', 'I','O', 'U']
for vowel in vowels:
    user_input = user_input.replace(vowel, '')
    user_input = user_input.replace(str.lower(vowel), '')
print(f"Output: {user_input}")