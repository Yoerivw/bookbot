import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()

    return file_contents


def main():

    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    dic = character_count(text)
    sorted_list = sort_dictionaries(dic)
    # print(f"Found {num_words} total words")
    print_report(sys.argv[1], num_words, sorted_list)


from stats import *

main()
