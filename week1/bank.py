users_input = input("Greeting: ")

if users_input == "hello":
    print("$0")
elif str(users_input).startswith("h") or users_input.startswith("H"):
    print("$20")
else:
    print("$100")
