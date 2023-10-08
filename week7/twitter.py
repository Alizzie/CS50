# Extracting username from URL
url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/")

# REGULAR EXPRESSION
import re

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))