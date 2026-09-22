"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
• Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output."""
Glossary = {'variable':'A variable is used to declare the number,word etc.',
           'loop':'A loop is used to run the number time which n == n',
           'list':'A list is store which store in 0 index format with this [] bracket',
           'tuple':'A tuple is the form list which is denoted by () this not changable.',
           'dictionary':'A dictionary is the method where we give key and value and bracket is {} and , in last after each list'}
for word,meaning in Glossary.items():
    print(f"{word.title()}:\n {meaning}")