'''Exercise 2: Glossary :ballot_box_with_check:
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
* Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
each word-meaning pair in your output.'''

glossary = {
    'input': 'Allows user input.',
    'f-string': 'a way to embed expressions inside string literals in Python, using curly braces {}.',
    'Triple Quotes': 'Are used to span multiple lines',
    'list': 'A list of items in a particular order.',
    'dictionary': "A collection of key:value pairs.",
    }

word = 'input'
print(f"\n{word.title()}: {glossary[word]}")

word = 'f-string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'Triple Quotes'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")