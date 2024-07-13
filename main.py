


def count_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> list[dict[str, int]]:
    
    chars = {}
    char_list = []
    
    for word in text.split():
        for char in word:
            char_list.append(char.lower())

    for char in char_list:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return [{'char': key, "num": value} for key, value in chars.items()]


def print_report(num_words: int, chars: list[dict[str, int]]):
    chars.sort(reverse= True, key= lambda i: i['num'])

    print(f"{num_words} words found in the document")

    for record in chars:
        letter = record['char']
        num = record['num']
        print(f"The '{letter}' character was found {num} times")
    

def main():
    with open('./books/frankenstein.txt') as f:
        text = f.read()

    chars = count_chars(text)

    print_report(
        count_words(text),
        chars
    )

main()
