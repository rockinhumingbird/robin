def reverseStr(s, k):
    sp =  list()
    for i in range(0, len(s), 2*k):
        sp += reversed(s[i:i+k])
        sp += s[i+k:i+2*k]
    return ''.join(sp)
reverseStr('abeccd', 2)