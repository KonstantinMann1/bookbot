def count_words(text):
    return len(text.split())

def sort_on(items):
    return items["num"]

def count_character(text):
    text_lower = text.lower()
    amount_character = {}
    for char in text_lower:
        if not char.isalpha():
            continue
        value = amount_character.get(char, {}).get("num", 0)
        value += 1
        amount_character[char] = {"char": char, "num": value}
    return sorted(amount_character.values(), key=sort_on, reverse=True)

