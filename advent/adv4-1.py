with open("input4.1.txt", "r") as file:
    data = file.read()
    all_cards = data.strip().split("\n")

def to_int(item):
    new_list = []
    for i in item:
        if i != '':
            new_list.append(int(i))

    return new_list

ans = 0

for card in all_cards:
    your_numbers = []
    winning_numbers = []
    win = 0
    doubles = 0

    no_id = card.split(":")
    container = no_id[1].split("|")
    your_numbers = to_int(container[0].strip().split(" "))

    winning_numbers = to_int(container[1].strip().split(" "))

    for num in your_numbers:
        if num in winning_numbers:
           if win == 0:
               win += 1
           elif win > 0:
               win *= 2

    ans += win

print(ans)