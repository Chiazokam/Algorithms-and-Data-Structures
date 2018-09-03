def reverse_ls(ls):
    if len(ls) == 0:
        return []
    else:
        return [ls[-1]] + reverse_ls(ls[:-1])
        
lists = [3, 6, 5, 8, 10]
print(reverse_ls(lists))
