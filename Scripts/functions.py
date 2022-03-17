def findSum(num, bound):
    if num == 255:
        return 255
    else:
        return num + bound

def findDif(num, bound):
    if num == 0:
        return 0
    else:
        return num - bound

def returnAvg(a, b, c=False, d=False, e=False, f=False):
    if a != False and b != False and c != False and d != False and e != False and f != False:
        return (a + b + c + d + e + f)/6
    elif a != False and b != False and c != False and d != False and e != False:
        return (a + b + c + d + e)/5
    elif a != False and b != False and c != False and d != False:
        return (a + b + c + d)/4
    elif a != False and b != False and c != False:
        return (a + b + c)/3
    elif a != False and b != False:
        return (a + b)/2

def returnGreat(a, b, c):
    if a == b == c:
        return a
    if a >= b:
        if a >= c:
            return a
    if b >= c:
        if b >= a:
            return b
    if c >= a: 
        if c >= b:
            return c

def returnLow(a, b, c):
    if a <= b:
        if a <= c:
            return a
    if b <= c:
        if b <= a:
            return b
    if c <= a: 
        if c <= b:
            return c

def returnGreatString(a, b, c):
    if a == b == c:
        return "all"
    if a >= b:
        if a >= c:
            return 'r'
    if b >= c:
        if b >= a:
            return 'g'
    if c >= a: 
        if c >= b:
            return 'b'

def difGreat(great, low, threashDif):
    if (great - low) <= threashDif:
        return True
    else:
        return False

def determineMax(inputVal, inputCol):
    r = "r"
    g = "g"
    b = "b"
    both = "all"
    if inputVal == inputCol:
        return True
    elif inputCol == "all":
        return True
    else:
        return False
    
from scipy.spatial import KDTree
from webcolors import (
    CSS3_NAMES_TO_HEX,
    hex_to_rgb,
)
def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_NAMES_TO_HEX
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'{names[index]}'