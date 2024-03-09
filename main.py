def read_text_from_file(file_path):
    with open(file_path) as file:
        return file.read()


def count_letter(text):
    text = text.lower()
    dictionary = {}
    for char in text:
        if char in dictionary:
            dictionary[char] +=1
        else:
            dictionary[char] = 1
    return dictionary


def get_count(dict_item):
    return dict_item['count']



def count_char(text):
    char_dict = {}
    for char in text:
        if char.isalpha() and char in char_dict:
            char == char.lower()
            char_dict[char] += 1
        else:
            if char.isalpha():
             char_dict[char] = 1

            
    
    list_dict = []
    for key, value  in char_dict.items():
        list_dict.append({'character':key, 'count':value})
    list_dict.sort(key = get_count, reverse = True)


    print('----Begin report')
    for item in list_dict:
        print(f'The character ' + item['character'] +' was found ' + str(item['count']) + ' times!')
    print('__end report__')


        


def main():
    file_path = '/Users/admin/workspace/github.com/jrfowr9fiw2p9/bookbot/books/frankenstein.txt'

    text = read_text_from_file(file_path)

    letter_counts = count_letter(text)

    print(letter_counts)

    count_char(text)


if __name__ == "__main__":
    main()
