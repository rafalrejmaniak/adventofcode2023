with open('input3.1.txt') as fin:
    data = fin.read()
    lines = data.strip().split('\n')

all_lines = len(lines)
all_in_line = len(lines[0])

goods = [[[] for _ in range(all_in_line)] for _ in range(all_lines)]

def is_symbol(row, column, num):
    if not (0 <= row < all_lines and 0 <= column < all_in_line):
        return False

    if lines[row][column] == "*":
        goods[row][column].append(num)
    return lines[row][column] != "." and not lines[row][column].isdigit()

ans = 0

for i, line in enumerate(lines):
    start = 0

    current_column = 0

    while current_column < all_in_line:
        start = current_column
        num = ""
        while current_column < all_in_line and line[current_column].isdigit():
            num += line[current_column]
            current_column += 1

        if num == "":
            current_column += 1
            continue

        num = int(num)

        is_symbol(i, start-1, num) or is_symbol(i, current_column, num)


        for k in range(start-1, current_column+1):
            is_symbol(i-1, k, num) or is_symbol(i+1, k, num)


for i in range(all_lines):
    for j in range(all_in_line):
        nums = goods[i][j]
        if lines[i][j] == "*" and len(nums) == 2:
            ans += nums[0] * nums[1]



print(ans)
