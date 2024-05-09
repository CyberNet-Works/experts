import re
regex = re.compile('[^a-zA-Z]')

def get_strip_string(translation_string: str) -> str: #wasnt sure how to do regex
    stripped_string = ""

    for char in translation_string:
        if char.isalpha():
            stripped_string += char
    return stripped_string

def get_etor_count(stripped_string: str) -> list:
    etor_dict = {}
    for key in stripped_string.lower():
        etor_dict[key] = etor_dict.get(key, 0) + 1
    sorted_etor_keys = sorted(etor_dict, key=etor_dict.get, reverse=True)[0:4]

    return sorted_etor_keys

def get_translation(sorted_etor_keys: list, translation_string: str) -> str: #if or version, not str.translate or dictionary translation
    letters = [char for char in translation_string] 
    translation = ""
    
    for letter in letters:
        if letter == sorted_etor_keys[0]:
            translation += 'e'
        elif letter == 'e':
            translation += sorted_etor_keys[0]
        elif letter == sorted_etor_keys[0].upper():
            translation += 'E'
        elif letter == 'E':
            translation += sorted_etor_keys[0].upper()
            
        elif letter == sorted_etor_keys[1]:
            translation += 't'    
        elif letter == 't':
            translation += sorted_etor_keys[1]
        elif letter == sorted_etor_keys[1].upper():
            translation += 'T'
        elif letter == 'T':
            translation += sorted_etor_keys[1].upper()            
            
        elif letter == sorted_etor_keys[2]:
            translation += 'o'
        elif letter == 'o':
            translation += sorted_etor_keys[2]
        elif letter == sorted_etor_keys[2].upper():
            translation += 'O'
        elif letter == 'O':
            translation += sorted_etor_keys[2].upper()
            
        elif letter == 'r':
            translation += sorted_etor_keys[3]
        elif letter == sorted_etor_keys[3]:
            translation += 'r'
        elif letter == sorted_etor_keys[3].upper():
            translation += 'R'
        elif letter == 'R':
            translation += sorted_etor_keys[3].upper()
        else:
            translation += letter
    
    print(''.join(translation))


def main():
    translation_string =  "'Puackich, hvhnkrally oaths phufhck.  All ymr nhhd Pykemn.' J.U.U.U Kmltin. mmps iks nmk eio; ---> hkmu"
    stripped_string = get_strip_string(translation_string)
    sorted_etor_keys = get_etor_count(stripped_string)
    #print(f'sorted keys: {sorted_etor_keys}\nsplit string:{translation_string.split()}')
    translation = get_translation(sorted_etor_keys, translation_string)
    
    
    
if __name__ == "__main__":
    main()

