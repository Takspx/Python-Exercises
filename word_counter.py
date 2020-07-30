import pprint

def remove_punctuation(punctuations, message):
    for i in punctuations:
        message = message.replace(i, '')
    return message

def word_count_display(message):
    dictionary = {}
    for word in message:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print(pprint.pformat(dictionary))

def main():
    bad_chars = [",", ".", "!", "?"]
    text = input('Enter the text: ').lower()
    text = remove_punctuation(bad_chars, text)
    message_list = text.split()
    word_count_display(message_list)
    
main()