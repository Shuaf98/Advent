import collections
valid = 0
#diction = {}
attrib_set = ['byr', 'iyr','hgt', 'ecl', 'pid', 'eyr', 'hcl']
attrib_cid = ['byr', 'iyr', 'cid','hgt', 'ecl', 'pid', 'eyr', 'hcl']
key_set = []

# =============================================================================
#     list_1 = file.read()
#     string_1 = list_1.split('\n\n')
#     #print(string_1)
#     string_2 = [x.replace('\n', ' ') for x in string_1]
#     #print(string_2)
#     string_3 = [x.split() for x in string_2]
# =============================================================================
data = open(r'C:\Users\sfrie\Python\AdventofCode\Day4.txt').read().split('\n\n')
data = [x.replace('\n', ' ').replace(' ', ', ').split(', ') for x in data]
for x in data:
    key_set=[]
    diction = {}
    for y in x:
        attribute, value = y.split(':')
        diction.setdefault(attribute)
        diction[attribute] = value
    for key in diction:
        key_set.append(key)
    print(key_set)

    if collections.Counter(attrib_set) == collections.Counter(key_set) or collections.Counter(attrib_cid) ==collections.Counter(key_set):
        valid += 1
        
        print('yes')
print(valid)

