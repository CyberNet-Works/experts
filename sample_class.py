y = {"fname":"Alex", "lname":"Kuznetsov", 2:1000}
new_dict = {}
x = new_dict

for key, value in enumerate(y):
    new_dict[key] = value
    
for key in new_dict:
    print(x)
    print(f' x key: {x[key]}')
    print(f' x items: {x.items()}')
    print(f' x vlaues: {x.values()}')
    print(f' x items: {x.items()}')
    
    #integers immutable
    #dict keys are immutable
    orig_dict = {1:"Python", 2:"JAav", 3:"C"}
    orig_dict[1]
    id(orig_dict)
    orig_dict[1] = "Bash"
    id(orig_dict)
    orig_dict
    orig_dict.update({1:"Go", 4:"Matlab"})
    orig_dict
    id(orig_dict)
    orig_dict.pop() #error
    orig_dict.pop(3) #the 3 is key
    #no indexes in dictionaries
        