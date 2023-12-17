f = open("inpu.txt", "r")
container = []

for line in f:
    number = ''
    good_line = line
    reversed_line = good_line[::-1]

    for item in good_line:
        if item.isdigit():
            number = item
            break

    for item in reversed_line:
        if item.isdigit():
            number += item
            break

    container.append(int(number))

f.close()

print(sum(container))