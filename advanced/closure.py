def outer():

    number = 1

    def inner():
        nonlocal number # get 'number' from outer scope
        print(number)
        number += 1

    return inner

calculate = outer()

calculate()
calculate()
calculate()


# ---------- simple function without closure
def simpleFunc():

    number = 1

    print(number)
    number += 1

simpleFunc()
simpleFunc()        
simpleFunc()
