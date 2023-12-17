with open('input3.1.txt') as fin:
    data = fin.read()
    lines = data.strip().split('\n')

all_lines = len(lines)
all_in_line = len(lines[0])

def is_symbol(row, column):
    if not (0 <= row < all_lines and 0 <= column < all_in_line):
        return False

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

        if is_symbol(i, start-1) or is_symbol(i, current_column):
            ans += num
            continue

        for k in range(start-1, current_column+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                ans += num
                break

print(ans)
