#my favorite solution
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
  
 #my version below 
 def to_hex(*args):
    s = ''
    for i in args:
        print(hex(i))
        if len(hex(i)) == 3:
            s += '0'
        s += (hex(i)[2:])
        print(s, type(s))
    return s.upper()

a, b, c = int(input()), int(input()), int(input())
print(to_hex(a, b, c))
