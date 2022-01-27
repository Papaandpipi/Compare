import difflib
import re

def tokenize(s):
    return re.split('\s(?<!\n)', s)

def untokenize(ts):
    return ' '.join(ts)


l1 = tokenize("This is a very cold \nhot summer. How are you? I am no.")
l2 = tokenize("This is mildly cold \nwinter. What are you? You are yes.")
res1 = []

prev = difflib.Match(0,0,0)
for match in difflib.SequenceMatcher(a=l1, b=l2).get_matching_blocks():
    if (prev.a + prev.size != match.a):
        for i in range(prev.a + prev.size, match.a):
            res1 += ['-' + l1[i] + '-']
        
    if (prev.b + prev.size != match.b):
        for i in range(prev.b + prev.size, match.b):
            res1 += ['+' + l2[i] + '+']

    res1 += l1[match.a:match.a+match.size]

    prev = match

print(res1)

result = untokenize(res1)

print(result)

