#Write a function tree_reverse to reverse elements of a nested-list recursively.
#ree_reverse([[1, 2], [3, [4, 5]], 6])
#[6, [[5, 4], 3], [2, 1]]


def reverse_tree(listi):
     result =[]
     for i in listi[::-1]:
        if isinstance(i,list):
             result.append(reverse_tree(i))
        else:
             result.append(i)
     return result
print reverse_tree([[1, 2], [3, [4, 5]], 6])   
