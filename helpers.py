import difflib
import re

def tokenize(s):
    return re.split('\s(?<!\n)', s)

def untokenize(ts):
    return ' '.join(ts)

def compare(s1, s2):
    l1 = tokenize(s1)
    l2 = tokenize(s2)
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
        
    result = res1

    return result