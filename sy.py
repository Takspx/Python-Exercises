#! python3
# sy.py - Copy symbols that are not easily found on the keyboard

SYMBOLS = {'backtick': '`', 'enye': 'ñ', 'ENYE' : 'Ñ',
           'tab': '\t', 'minplus': '\u2213', 'plusmin': '\u00B1',
           'cspace': '    '}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python sy.py [symbol name] - copy symbol')
    sys.exit()

symbol_name = sys.argv[1]

if symbol_name in SYMBOLS:
    pyperclip.copy(SYMBOLS[symbol_name])
    print('Symbol ' + symbol_name + ' is copied to clipboard.')
else:
    print('There is no symbol named ' + symbol_name)
