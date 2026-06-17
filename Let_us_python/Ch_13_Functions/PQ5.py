def ispangram(s):
    alphaset = set('abcdefghijklmopqrstuvwxyz')
    return alphaset<=set(s.lower())
print(ispangram('The quick brown fox jumps over the lazy dog'))
print(ispangram('Crazy Fredric bought many very exquiest opal jewels'))