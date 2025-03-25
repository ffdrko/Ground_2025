# String Methods
first = "Fahim"
print(first)
print(first.lower())
print(first.upper())

multiline = '''
Hey, I'm a multi-line string.
I can contain multiple lines of text.
'''

print(multiline.title())
print(multiline.replace("text", "letter"))

print(len(multiline))

multiline += "                 "

multiline = "      "+multiline

print(multiline)
print(len(multiline))