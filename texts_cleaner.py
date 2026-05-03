def texts_cleaner(bad_texts):
    text = bad_texts.strip().lower()

    bad_words = "@#$&"
    for x in bad_words:
        text = text.replace(x, "")
    clean_text = " ".join(text.split())
    return clean_text

a = "H#ello# Pyth$&on"
b = texts_cleaner(a)
print(b)