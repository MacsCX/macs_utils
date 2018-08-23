from math import sqrt


def init_nums(limit: int):
    init_nums = [2]
    for i in range(3, limit):
        if i % 10000 == 0:
            print(i)
        is_initial = True

        if i % 2 == 0:
            continue

        if int(sqrt(i)) == sqrt(i):
            continue

        to_check = set(init_nums).intersection(set(range(3, int(sqrt(i)))))
        for m in to_check:
            if i % m == 0:
                is_initial = False
                break
        if is_initial:
            init_nums.append(i)

    return init_nums


print(init_nums(2000000))
