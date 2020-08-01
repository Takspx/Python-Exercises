def to_camel_case(text):
    for i in ['_', '-']:
        text = text.replace(i,' ')
    text = text.title() # must be changed
    for i in [' ']:
        text = text.replace(i, '')
    print(text)

def main():
    user_input = input('Enter text: ')
    to_camel_case(user_input)

main()
