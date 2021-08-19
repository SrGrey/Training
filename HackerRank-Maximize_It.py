'''You are given a f(X) = X^2 function . You are also given K lists. The i-th list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:

S = (f(X1) + f(X2) + ... + f(Xk)) % M

 Xi denotes the element picked from the i-th list . Find the maximized value Smax obtained.
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format:
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the i-th list, followed by Ni space separated integers denoting the elements in the list.

Constraints
1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7
1 <= Magnitude of elements in list <= 10^9

Output Format
Output a single integer denoting the value Smax.

Sample Input:
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output:
206

Explanation

Picking 5 from the 1-st list, 9 from the 2-nd list and 10 from the 3-rd list gives the maximum S value equal to (5^2 + 9^2 + 10^2) % 1000 = 206
'''
###MY SOLUTION###
from itertools import product

first_line = input()
k = int(first_line.split()[0])
m = int(first_line.split()[1])
list_of_square_lists = []
summa = 0
list_of_combined_numbers = []
n = []
for i in range(k):
    s = input().split()[1:]
    s = list(set(map(lambda x: int(x)**2, s)))
    list_of_square_lists.append(s)
list_of_combined_numbers = list(product(*list_of_square_lists))
for el in list_of_combined_numbers:
    if summa % m < sum(el) % m:
        summa = sum(el)
print(summa % m)

###Short SOLUTION### BUT THIS SOLUTION DOES NOT CUT OFF repeated combination my solution could work faster with big data  ^_^ 
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))


