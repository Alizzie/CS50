email = input("What's your email? ").strip()

# @@ would be still valid
#if "@" in email:
#    print("Valid")
#else:
#    print("Invalid")

# @. would be valid
#if "@" in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")

# only with .edu and malan@.edu is valid
#username, domain = email.split("@") 
#if username and domain.endswith(".edu"):
#    print("Valid")
#else:
#    print("Invalid")

# malan@havard is valid
#username, domain = email.split("@")
#if username and "." in domain:
#    print("Valid")
#else:
#    print("Invalid")

# Python library re contains number of built-in functions
# For validating user inputs against patterns

# REGULAR EXPRESSIONS
#.   any character except a new line
#*   0 or more repetitions
#+   1 or more repetitions
#?   0 or 1 repetition
#{m} m repetitions
#{m,n} m-n repetitions
# \ for escaping a character 
#^   matches the start of the string
#$   matches the end of the string or just before the newline at the end of the string
#[]    set of characters
#[^]   complementing the set
#\d    decimal digit
#\D    not a decimal digit
#\s    whitespace characters
#\S    not a whitespace character
#\w    word character, as well as numbers and the underscore = [a-zA-Z0-9_]
#\W    not a word character
#A|B     either A or B
#(...)   a group
#(?:...) non-capturing version

import re

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

# FLAGS within re.search function
#re.IGNORECASE
#re.MULTILINE
#re.DOTALL

if re.search(r"^\w+@\w.+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# For only two dots after @
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# Other functions re.match and re.fullmatch

