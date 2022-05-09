import re

text = input()
expression = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(expression, text)
print(' '.join(matches))
