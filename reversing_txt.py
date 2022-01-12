''' Script reversing txt file'''

with open("input.txt", 'r') as f, open("out.txt", 'w') as w:
    w.writelines(reversed(f.readlines()))
    
