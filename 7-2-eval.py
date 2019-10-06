def eval_loop():
    while True:
        line = (input("Please enter input: "))
        if line == 'done':
            break
        print(eval(line))
        last_line_result = eval(line)
    print(last_line_result)

print(eval('1+2'))
eval_loop()
