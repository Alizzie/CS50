import sys

def main():

    filename = get_filename(sys.argv)
    line_counter = 0
    try:

        with open(filename) as file:
            for line in file:
                if line.lstrip().startswith("#") or not line.rstrip():
                    continue
                else:
                    line_counter += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_counter)

def get_filename(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    
    filename = sys.argv[1]

    if filename[-3:] != ".py":
        sys.exit("Not a Python file")

    return filename

if __name__ == "__main__":
    main()