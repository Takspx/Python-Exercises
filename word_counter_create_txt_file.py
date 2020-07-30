import pprint


def char_remover(chars, message):
    for i in chars:
        message = message.replace(i, '')
    return message


def word_counter(message):
    dictionary = {}
    for word in message:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return pprint.pformat(dictionary)


def main():
    bad_chars = ['.', ',', '!', '?',
                 '(', ')', '[', ']',
                 ':', ';', '-', '\"',
                 "\'", '0', '1', '2',
                 '3', '4', '5', '6',
                 '7', '8', '9']
    
    text = input('Enter a text: ').lower()
    text = char_remover(bad_chars, text)
    message_list = text.split()
    #  creates and writes a text file named counter_word.txt
    f = open('counted_words.txt', 'w+')
    f.write(str(word_counter(message_list)))

main()