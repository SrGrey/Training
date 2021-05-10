def in_array(array1, array2):
    # your code
    r = []
    for elem in array1:
        for i in range(len(array2)):
            if elem in array2[i] and elem not in r:
                r.append(elem)
    
    return sorted(r)       

#short version:
#(elem for elem in array1 for elem2 in array2 if elem in elem2)   


#test
r = []
a1 = ["arp", "mice", "bull"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
