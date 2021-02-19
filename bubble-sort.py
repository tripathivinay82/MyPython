
#!/usr/bin/python3.7

# Option-1: Bubble sort function
def MyProg(num_lst):

    print(f'Bubble Sort Input: {num_lst}')
    for i in range(len(num_lst)):
        for j in range(len(num_lst)):
            if num_lst[i] < num_lst[j]:
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
    print(f'Bubble Sort Output: {num_lst}')

num_lst = [5, 1, 6, 2, 4, 3]
#num_lst = [1,5,2,4,3]
MyProg(num_lst)

