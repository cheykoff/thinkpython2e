count = 0
known = {0:0, 1:1}

def reassign_wrong():
    count = 0
    count = count + 1

def reassign():
    global count
    count = + 1

def modify_mutable():
	known[2] = 1

print(count)
reassign_wrong()
print(count)
reassign()
print(count)

print("\n", known)
modify_mutable()
print("\n", known)
