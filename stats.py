def count_words(text):
    return f"Found {len(text.split()) } total words"

def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dicts(dict):
    sorted_list = []
    for key in dict:
        new_dict = {
                "character": key,
                "count": dict[key]
        }

        sorted_list.append(new_dict)
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list