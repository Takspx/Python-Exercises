text = input()
punc_remove = [",", ".", "!", "?"]

for i in punc_remove:
    text = text.replace(i, "")
print(text.lower())
