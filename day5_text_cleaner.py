import re

sentence: str = """
This may not be the correct way to use them, but it's how I do it. 
If it's a quick if-else statement, I use if If there's an else if and the 
compare statement is short, I use if If it's a lot to compare or I'd have more than 1 
else if and I can't do it with a dictionary, I use a match-case If logistically a match 
statement makes sense in the context, I'd use match (coding with others) I honestly haven't needed 
to use them too much, but when I do it's a god send. Basically I use it when it's easier to read.
"""

sentence = re.sub(r"[^\w\s]", "", sentence)

sentence = " ".join(sentence.split()).lower()

print(sentence)