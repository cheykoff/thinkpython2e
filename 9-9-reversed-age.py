def reversed_age():
    my_age = 0
    age_diff = 18
    moms_age = my_age + age_diff
    count_reversed_ages = 0
    end = 150
    while age_diff < 50:
        while my_age < end:
            moms_age = my_age + age_diff
            if str(my_age).zfill(2) == str(moms_age)[::-1] or str(my_age).zfill(2) == str(moms_age + 1)[::-1]:
                print(my_age, moms_age)
                count_reversed_ages = count_reversed_ages + 1
            my_age = my_age + 1
        age_diff = age_diff + 1
    print(count_reversed_ages)
        

reversed_age()
