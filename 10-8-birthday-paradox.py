import random

def has_duplicates(t):
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] == t[j]:
                return True
    return False

def generate_birthdays(n_birthdays):
    i = 0
    t = []
    for i in range(n_birthdays):
        birthday = random.randint(1, 365)
        t.append(birthday)
    return t

def generate_samples(n_examples, n_birthdays):
    i = 0
    count = 0
    for i in range(n_examples):
        if has_duplicates(generate_birthdays(n_birthdays)):
            count += 1
    return count/n_examples

def go_through_n_birthdays(n_examples):
    i = 0
    print('Birthdays:','Percentage for two same birthdays:')

    for i in range(80):
        print(i, generate_samples(n_examples, i))
        
        

n_birthdays = 40
n_examples = 1000

go_through_n_birthdays(n_examples)

            




    
