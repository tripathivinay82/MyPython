readme="https://www.hackerrank.com/challenges/nested-list/problem"
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])

second_high = sorted(set([i[1] for i in students]))[1]
print("\n".join(sorted([i[0] for i in students if i[1] == second_high])))