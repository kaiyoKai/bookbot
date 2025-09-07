
def get_book_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_book_char_count(book_text):
    chardic = {}
    for c in list(book_text.lower()):
        chardic[c] = chardic.get(c, 0) + 1
    return chardic


def get_sorted_dic(book_dic):
    items = [{"char": k, "num": v} for k, v in book_dic.items()]
    return sorted(items, key=lambda item: item["num"], reverse=True)
