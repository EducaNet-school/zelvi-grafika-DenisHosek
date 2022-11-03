def end(a):
    di = {}
    di.update(a)
    for i in sorted(di.items()):
        pass
    print(dict(sorted(di.items())))


def pis(a):
    from collections import Counter
    d = []
    for l in a:
        if l in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            d.append(l)
    else:
        a = Counter(d)
        end(a)
       

p = str(input("Zadejte větu: "))

pis(p)
