def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def get_num_char(text):
    count = {}
    for ch in text:
        char_lower = ch.lower()
        if char_lower not in count:
            count[char_lower] = 1
        else:
            count[char_lower] += 1
    return count

def sort_on(d):
    return d["num"]

def get_sorted_char(text):
    sorted = []
    for ch in text:
        if ch.isalpha():
            sorted.append({"char": ch, "num": text[ch]})  

    sorted.sort(reverse=True, key=sort_on)
    return sorted