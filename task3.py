import string
import random
if __name__ == '__main__':
    a = string.ascii_letters
    b = string.punctuation
    c= string.digits
    paslen = int(input(("Enter the length of Password ")))
    p = list(a)
    q =list(b)
    r = list(c)
    s =p+q+r
    random.shuffle(s)
    print("".join(s[0:paslen]))
    
    
    