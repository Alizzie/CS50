def main():
    user_input = input("Input: ")


def shorten(word):
        
    vowels = ['A','E', 'I','O', 'U']
    for vowel in vowels:
        word = word.replace(vowel, '')
        word = word.replace(str.lower(vowel), '')
    return word


if __name__ == "__main__":
    main()