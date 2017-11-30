def somefunc():
    print ("hi")
psyco.bind(somefunc)          # or method, class
newname = psyco.proxy(func)
newname()
