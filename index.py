import requests
from bs4 import BeautifulSoup

def get_user_word():
    print("\nWhat word do you want to look up?")
    word = input("> ")
    return word

def get_ud_data():

    word = get_user_word()
    # Get Urban Dictionary thumbs_up_count for input word.
    r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))

    soup = BeautifulSoup(r.content, features="html.parser")
    # only run the soup.find once, capture in variable - then check if it's equal to None
    meaning = soup.find("div", attrs={"class":"meaning"})

    # If the word doesn't have a meaning on UD, return the word and None
    if meaning is None:
        thumbs_up_count = None
        print("word not found")
        return [word, None]
    else:
        meaning = str(meaning)
        clean_meaning = BeautifulSoup(meaning, features="html.parser")
        clean_meaning = clean_meaning.get_text()
        clean_meaning = clean_meaning.replace("&apos", "'")
        thumbs_count_list = soup.findAll("span", attrs={"class":"count"})
        thumbs_type_count_dict = {"Up": [], "Down": []}
        # even is up
        # odd is down
        count_type = 1
        for count in thumbs_count_list:
            count = str(count)
            clean_count = BeautifulSoup(count, features="html.parser")
            clean_count = clean_count.get_text()
            # if count_type is even, it's thumbs up, otherwise it's thumbs down count
            if count_type %2 != 0:
                thumbs_type_count_dict["Up"].append(int(clean_count))
            elif count_type %2 == 0:
                thumbs_type_count_dict["Down"].append(int(clean_count))
            count_type = count_type + 1

        thumb_up_count_list = thumbs_type_count_dict["Up"]
        largest_up_thumb_count = max(thumb_up_count_list)
        thumb_down_count_list = thumbs_type_count_dict["Down"]
        largest_down_thumb_count = max(thumb_down_count_list)

        return [word, largest_up_thumb_count, largest_down_thumb_count, clean_meaning]

def print_data():
    output_data = get_ud_data()

    if output_data[1] != None:
        word = output_data[0]
        largest_up_thumb_count = output_data[1]
        largest_down_thumb_count = output_data[2]
        clean_meaning = output_data[3]

        if largest_up_thumb_count < 300:
            prominance_level = "low"
        elif largest_up_thumb_count > 300 and largest_up_thumb_count < 1000:
            prominance_level = "medium"
        elif largest_up_thumb_count > 1000:
            prominance_level = "high"

        print("\n\nThe word '{}' has relatively {} prominance on Urban Dictionary.\n\nTop definition:\n{}\n\n".format(word.title(),
        prominance_level, clean_meaning.capitalize()))
    else:
        word = output_data[0]
        print("\n\n{} not found on Urban Dictionary\n\n.".format(word.title()))

print_data()
