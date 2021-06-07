'''Pretty use of recursion:
   sum of digits in number till it more than 9'''

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
  
