'''Exercise 3: Glossary 2 :ballot_box_with_check:
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.'''

glossary = {
    'input': 'Allows user input.',
    'f-string': 'a way to embed expressions inside string literals in Python, using curly braces {}.',
    'Triple Quotes': 'Are used to span multiple lines',
    'list': 'A list of items in a particular order.',
    'dictionary': "A collection of key:value pairs.",
    'comment': "Are the lines in the code that are ignored by the interpreter.",
    'float': "A number with a decimal part.",
    'if/elif/else':"A conditional statement that automatically executes different code when set conditions are met",
    'string':"A series of characters",
    'variables':"Basically containers for storing data values",
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")