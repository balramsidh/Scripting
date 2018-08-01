def csv (anylist):
    con_val = ''
    for i in range(len(anylist)):
        if i == 0:
            con_val = anylist[i]
        else:
            con_val = con_val + ',' + anylist[i]
    return con_val

spam = ['apples', 'bananas', 'tofu', 'cats']

print(csv(spam))
