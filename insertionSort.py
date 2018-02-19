list = [1, 8, 5, 2, 3, 4, 6, 9, 10]

a = 0
b = 1
l_len = len(list)
step = 0

while (b < l_len):
    step = step + 1
    print("Step #", step, sep="")

    el = list[b]
    a = b-1
    loc = b

    while el < list[a] and a > -1:
        print([list[loc], list[a]])
        list[loc] = list[a]
        list[a] = el
        a = a-1
        loc = loc-1
        print(list)

    b = b+1

print(list)
