def integer(n, m):
    string = str(n)
    sums = n
    sum_string = str(n)

    i = 1
    while i < m:
        i += 1

        sum_string = sum_string + string

        sums = sums + int(sum_string)

        return sums


n = int(input("Number: "))
m = int(input("Many: "))
total = integer(n, m)
print(total)
