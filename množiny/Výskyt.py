def vypis(a):
    dict = {}
    for i in a:
        pass

def pis(a):
    dic = []
    for l in a:
        if l in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef":
            dic.append(l)
    else:
        vypis(dic)


p = str(input("Kolik chcete zadat pismen "))

pis(p)