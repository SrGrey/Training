'''
Work with visibilty scopes
PROBLEM description 
Implement a program that emulates namespaces. You need to implement support for creating namespaces and adding variables to them.

In this task, each namespace has a unique textual identifier — its name.

The following requests are submitted to your program:

create <namespace> <parent> - create a new namespace named <namespace> inside the <parent> space
add <namespace> <var> - add a variable <var> to the <namespace> space
get <namespace> <var> - get the name of the space from which the variable <var> will be taken when requesting from the space <namespace>, or None if such a space does not exist
Consider a set of queries

add global a
create foo global
add foo b
create bar foo
add bar a
The structure of namespaces described by these queries will be equivalent to the structure of namespaces created when this code is executed.

a = 0
def foo ():
  b = 1
  def bar ():
    a = 2
In the main body of the program, we declare the variable a, thereby adding it to the global space. Next, we declare a function foo, which entails creating a local namespace for it within the global space. In our case, this is described by the create foo global command. Next, we declare the bar function inside the foo function, thereby creating the bar space inside the foo space, and add the variable a to bar.

Add get requests to our requests

get foo a
get foo c
get bar a
get bar b
Let's imagine how it might look in the code

a = 0
def foo ():
  b = 1
  get (a)
  get (c)
  def bar ():
    a = 2
    get (a)
    get (b)
The result of the get request will be the name of the space from which the desired variable will be taken.
For example, get foo a returns global, because the variable a is not declared in the foo space, but the variable a is declared in the global space, which contains the foo space. Similarly, get bar b returns foo, and get bar a returns bar.

Get foo c returns None because no c has been declared in either foo or global.

More formally, the output from get <namespace> <var> is

<namespace> if <var> was declared in <namespace>
get <parent> <var> - the result of a query to the space within which the <namespace> space was created, if the variable was not declared
None if <parent> does not exist, i.e. <namespace> is global
Input data format
The first line contains number n (1 ≤ n ≤ 100) - the number of requests.
Each of the next n lines contains one query.
Queries are executed in the order in which they are given in the input.
Namespace names and variable names are strings of length no more than 10, consisting of lowercase Latin letters.

Output data format
For each get request, print its result on a separate line.

Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
Sample Output:

global
None
bar
foo
'''
def create_namespace(namespace, parent):
    namespaces[f'{namespace}'] = dict(parent=f'{parent}', vars=set())

def add_var(namespace, var):
    namespaces[f'{namespace}']['vars'].add(var)

def get_namespace(namespace, var):
    if var in namespaces[f'{namespace}']['vars']:
        return namespace
    elif namespace != 'global':
        return get_namespace(namespaces[f'{namespace}']['parent'], var)
    return 'None'


namespaces = {
    'global': {'parent': None, 'vars': set()},
}
result = []
n = int(input())
for _ in range(n):
    instruction = input().split()
    if instruction[0] == 'create':
        create_namespace(instruction[1], instruction[2])
    elif instruction[0] == 'add':
        add_var(instruction[1], instruction[2])
    elif instruction[0] == 'get':
        result.append(get_namespace(instruction[1], instruction[2]))
for el in result:
    print(el)

