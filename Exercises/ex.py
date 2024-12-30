def freq(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    def keyval(k):
        return d[k]

    return max(d.keys(), key = keyval)

print(freq('abacacacasasadddddd'))