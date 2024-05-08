first_set = {1, 4, 5}
second_set = {3, 4, 5, 6}


third_set = first_set.intersection(second_set)

fourth_set = first_set.union(second_set)

fifth_set = first_set | second_set

seventh_set = second_set - first_set
eighth_set = first_set & second_set
ninth_set = second_set ^ first_set

print(f'first_set = {first_set}')
print(f'second_set = {second_set}')
print(f'third_set = {third_set}')
print(f'fourth_set = {fourth_set}')
print(f'fifth_set = {fifth_set}')
#print(f'sixth_set = {sixth_set}')
print(f'seventh_set = {seventh_set}')
print(f'eight_set = {eighth_set}')