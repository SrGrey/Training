''' Script searching for .py files in directory 'main'
'''

import os

result = [cur_dir for cur_dir, dirs, files in os.walk("main") if any((fl.endswith(".py")
    for fl in files))]

with open("py_dirs.txt", "w") as w:
    w.write("\n".join(sorted(result)))
    
    
''' other solution
import os

os.chdir('main')

lst = []
for current_dir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            lst.append(current_dir.replace('\\', '/').replace('.', 'main'))

with open('output.txt', 'w') as f:
    for line in sorted(set(lst)):
        line +='\n'
        f.write(line)
'''
