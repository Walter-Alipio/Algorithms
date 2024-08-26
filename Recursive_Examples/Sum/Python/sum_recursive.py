def sum(list_itens, index = 0):
    try:
        if list_itens[index]:
            return 1 + sum(list_itens, index + 1)
    except:
        return 0
    
items = [1,2,3,4,5]

print(sum(items))
