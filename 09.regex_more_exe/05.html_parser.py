import re


def remove_html_tags(text):
    """Remove html tags from a string"""

    clean = re.compile('(<[^>]+>)|(\n)')  # (<.*?>)|(\\n)')
    return re.sub(clean, '', text)


pattern_title = r'<title>(.+)</title>'
pattern_body = r'<body>(.+)</body>'
title_string = ''
body_string = ''

some_input = input()

title = re.findall(pattern_title, some_input)
if title:
    for symbol in title:
        title_string += symbol
    title_string = remove_html_tags(title_string)
    title_string = title_string.replace('\\n', '')
print(f'Title: {title_string}')

body = re.findall(pattern_body, some_input)

if body:
    for symbol in body:
        body_string += symbol
    body_string = remove_html_tags(body_string)
    body_string = body_string.replace('\\n', '')

print(f'Content: {body_string}')
