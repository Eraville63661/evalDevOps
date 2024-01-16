import numpy as np
# import log from numpy

def loga():
    a = os.variables.A
    b = os.variables.B

    c = np.log(a*b) #ils vont etre égaux ?
    d = np.log(a) + np.log(b)

    # c = log(a*b) #ils vont etre égaux ?
    # d = log(a) + log(b)

    print(c)
    print(d)
