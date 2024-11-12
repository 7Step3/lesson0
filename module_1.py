grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
print(students)
students = sorted(students)
print(students)
sum_0 = sum(grades[0])
len_0 = len(grades[0])
avg0 = sum_0/len_0
print(avg0)
sum_1 = sum(grades[1])
len_1 = len(grades[1])
avg1 = sum_1/len_1
print(avg1)
sum_2 = sum(grades[2])
len_2 = len(grades[2])
avg2 = sum_2/len_2
print(avg2)
sum_3 = sum(grades[3])
len_3 = len(grades[3])
avg3 = sum_3/len_3
print(avg3)
sum_4 = sum(grades[4])
len_4 = len(grades[4])
avg4 = sum_4/len_4
print(avg4)
dict_ = {students[0]:avg0, students[1]:avg1, students[2]:avg2, students[3]:avg3, students[4]:avg4}
print(dict_)