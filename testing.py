def testing(a, b):
    try:
        return a/b 
    except ZeroDivisionError:
        return "You can't divide a number with zero"
    except AttributeError:
        return "attribute error"
    except NameError:
        return "use a number to divide you moron"

print(testing(8,l))