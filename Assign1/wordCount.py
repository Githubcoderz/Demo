import argparse

def countWords(text):
    return len(text.split())

def countCharacters(text):
    return len(text)

def countLines(text):
    return len(text.splitlines())

def main():
    parser = argparse.ArgumentParser(description="Count words, characters, and lines in a file")
    
    parser.add_argument("filename", help="File to be processed")
    
    parser.add_argument("-w", "--word", action="store_true", help="Count words")
    parser.add_argument("-c", "--char", action="store_true", help="Count characters")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")

    args = parser.parse_args()

    try:
        with open(args.filename, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File '{args.filename}' not found.")
        return

    if args.word:
        print(countWords(text), args.filename)
    elif args.char:
        print(countCharacters(text), args.filename)
    elif args.lines:
        print(countLines(text), args.filename)
    else:
        lines = countLines(text)
        words = countWords(text)
        chars = countCharacters(text)
        print(f"{lines} {words} {chars} {args.filename}")

if __name__ == "__main__":
    main()