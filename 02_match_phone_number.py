import re

text = input()
expression = r"\+359([ -])2\1\d{3}\1\d{4}\b"

matches = re.finditer(expression, text)

result = []
for match in matches:
    result.append(match.group())

print(', '.join(result))
