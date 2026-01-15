mpti, res, q = [int(x) for x in open('51')], [], 0

mx = min(int(x) for x in mpti if str(x)[-1] == str(x)[-2])

def google1(x1, x2): return str(x1)[-1] == str(x2)[-2]

def google2(x): return x % 13 == 0

for x in range(len(mpti) - 1):
    a, b    = mpti[x], mpti[x+1]
    if google1(a, b) or google1(b, a):
        if google2(a) + google2(b) == 1:
            if mx ** 2 > a ** 2 + b ** 2:
                q   += 1
                res += [a ** 2 + b ** 2]
print(q, max(res))

# 115 96944186 
