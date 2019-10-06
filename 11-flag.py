verbose = True

def example():
    if verbose:
        print('Running example')

been_called = False

def example2():
    been_called = True
    print(been_called)

def example3():
    global been_called
    been_called = True

print(been_called)
example2()
print(been_called)
example3()
print(been_called)

example()
