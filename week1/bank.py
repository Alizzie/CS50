users_input = input("Greeting: ")
users_input = str(users_input)

if users_input.startswith("hello"):
    print("$0")
elif users_input.startswith("h") or users_input.startswith("H"):
    print("$20")
else:
    print("$100")
