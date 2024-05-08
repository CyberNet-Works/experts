# orig_list = [1,2,2,3,3,3,3,2,2,1,1,1,]

# set_list = set(orig_list)
# new_list = list(set(orig_list))


# orig_set = {1,2,3}
# #orig_set[0]

# print(new_list)
# print(type(orig_set))
# orig_set.add(1000) #add method
# dictionary = {"a": "b", "z": 1, "abc": "def", 0:32, 1:3823}
# dict_set = set(dictionary)
# print(dict_set)

#unordered, mutable


orig_set = {1,4}
orig_set.add((5,200))
print(orig_set)

print(id(orig_set))


orig_set.update([100,200]) #will add as separate items
orig_set.remove(100) #will remove until none left then key error
orig_set.pop() #always takes the first item in the set.  Does not accept key?
orig_set.add(23)
