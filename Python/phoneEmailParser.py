#! /usr/bin/env python3

import re,pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    (\S)+
    (@)
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

copied_text = str(pyperclip.paste())

matches = []
for group in phoneRegex.findall(copied_text):
    phonenum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phonenum += 'x' + group[8]
    matches.append(phonenum)

for group in emailRegex.findall(copied_text):
    matches.append(group[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
