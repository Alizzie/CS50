user_input = input("camelCase: ")

print(user_input[0], end="")
for character in user_input[1:]:
    if character.isupper():
        print(f"_{str.lower(character)}", end="")
    else:
        print(character, end="")