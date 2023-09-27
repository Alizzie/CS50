import requests
import sys

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    
    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Number cannot get converted into float")
    
    


except requests.RequestException:
    ...