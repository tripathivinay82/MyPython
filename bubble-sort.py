
#!/usr/bin/python3.7

# Option-1: Function for bubble sort
#def MyProg(num_lst):
#    num_lst = [1,5,2,4,3]
#    nl = []
#    for i in range(len(num_lst)):
#        for j in range(len(num_lst)):
#            if num_lst[i] <= num_lst[j]:
#                nl.append(num_lst[i])
#    print(list(set(nl)))

#num_lst = [1,5,2,4,3]
#MyProg(num_lst)

# Option-2: Nested List Comprehension 
#num_lst = [1,5,2,4,3]
num_lst = [5, 1, 6, 2, 4, 3]
print(list(set([num_lst[i] for i in range(len(num_lst)) for j in range(len(num_lst)) if num_lst[i] <= num_lst[j]])))


