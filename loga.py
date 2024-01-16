def loga(a, b):
    import log from numpy
    # c = np.log(a*b) #ils vont etre égaux ?
    # d = np.log(a) + np.log(b)

    c = log(a*b) #ils vont etre égaux ?
    d = log(a) + log(b)

    print(c)
    print(d)
