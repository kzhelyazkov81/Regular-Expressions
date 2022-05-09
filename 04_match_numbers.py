import re

text = input()

expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

matches = re.finditer(expression, text)

result = []
for match in matches:
    result.append(match.group())

print(' '.join(result))


