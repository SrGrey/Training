# Script for change character in any string
def replacement():
    symbol_to_change = input('Which character need to change? ')
    symbol_to_place = input('Which character need to place instead? ')
    changed_string = string_to_change.replace(symbol_to_change, symbol_to_place)
    return changed_string


string_to_change = input('input string to change: ')
method = ''
while method not in {'R', 'r', 'T', 't', 'Q', 'q'}:
    method = input('for replace put R, for quit put Q : ')

if method in {'R', 'r'}:
    print(replacement())
elif method in {'Q', 'q'}:
    print('buy!')
