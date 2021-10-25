def valid_parentheses(string):

    if  '(' not in set(string) and ')' not in set(string):
        return True
    elif '(' not in set(string) or ')' not in set(string):
        return False 
    else:
        return next(string)
    
def next(string):
    open_parentesis_count = 0
    close_parentesis_count = 0
    for symbol in list(string):
        if symbol == '(':
            open_parentesis_count += 1
            if open_parentesis_count < close_parentesis_count:
                return False
        if symbol == ')':
            close_parentesis_count += 1
            if open_parentesis_count < close_parentesis_count:
                return False
    if open_parentesis_count != close_parentesis_count:
        return False
    return True
  
  #---short---
  #def valid_parentheses(string):
  #cnt = 0
  #  for char in string:
  #      if char == '(': cnt += 1
  #      if char == ')': cnt -= 1
  #      if cnt < 0: return False
  #  return True if cnt == 0 else False
    
    
a = "  ("
b = ")test"
c = ""
d = "hi())("
e = "hi(hi)()"
print(valid_parentheses(a))
print(valid_parentheses(b))
print(valid_parentheses(c))
print(valid_parentheses(d))
print(valid_parentheses(e))
