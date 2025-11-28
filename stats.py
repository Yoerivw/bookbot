def count_words(text):
    word_list = text.split()
    length = len(word_list)
    return length

def character_count(text):
    character_count = {}
    lower_case_text = text.lower()

    # answered a similar question in the counting practice question
    for char in lower_case_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sort_on(items):
    return items["num"]


def sort_dictionaries(dictionary):
    us_list = []
    for key_value in dictionary:
        if key_value.isalpha() == True:
          temp_dic = {"char": "", "num":0}
          dic_val = dictionary[key_value]
          temp_dic["char"] = key_value
          temp_dic["num"] = dic_val
          us_list.append(temp_dic)
    us_list.sort(reverse=True, key=sort_on)



    return us_list

def print_st_list(list):
    for dict in list:
        print(f"{dict['char']}: {dict['num']}")


def print_report(path,num_words, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_st_list(list)
    print("============= END ===============")
