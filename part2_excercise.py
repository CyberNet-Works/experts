#Create 2 dicts with duplicates keys where keys are chars and values are ints
#combine both dictionaries and multiply the values for common keys


#Bad code below:
#-------------------------------
# d1 = {'a':2,'b':4,'c':3}
# d2 = {'a':3,'b':-2,'c':5}
# d3 = {}

# d1_keys = list(d1.keys())
# d2_keys = list(d2.keys())

# for key in d1_keys:
#     if key in d2_keys:
#         d3[key] = d1[key] * d2[key]
#         d2_keys.remove(key)
#     else:
#         d3[key] = d1[key]

# for key in d2_keys:
#     d3[key] = d2[key]
# print(d3)

d1 = {'a':2,'b':4,'c':3}
d2 = {'a':3,'b':-2,'c':5}
d3 = {}

d1_keys = set(d1.keys())
d2_keys = set(d2.keys())
all_keys = d1_keys | d2_keys

for key in all_keys:
    d3[key] = d1.get(key,1) * d2.get(key, 1)
print(d3)