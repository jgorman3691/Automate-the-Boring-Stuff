#! python3

import pyperclip
text = pyperclip.paste()
print(type(text))
# TODO, bullet points
lines = text.split('\n')
print(type(lines))
map(lambda: '* ' + lines)
text = '\n'.join(lines)
pyperclip.copy(text)
