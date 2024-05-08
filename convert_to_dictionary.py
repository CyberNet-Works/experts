# This version has Big 0 Squared Complexity
# def convert_to_dict(string):
#     string = list(string)
#     new_dict = {}
#     for key in string:
#         new_dict[key] = string.count(key)
#     print(new_dict)
#     return new_dict 
# user_input = str(input("Enter input:\n"))
# convert_to_dict(user_input)

#This version has Big 0 Complexity
def convert_to_dict(string):
    string = list(string)
    new_dict = {}
    
    for key in string:
        new_dict[key] = new_dict.get(key, 0) + 1
    print(new_dict)
    return new_dict 

user_input = str(input("Enter input:\n"))

convert_to_dict(user_input)
