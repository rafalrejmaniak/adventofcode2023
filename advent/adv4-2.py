with open("input4.1.txt", "r") as file:
    data = file.read()
    all_cards = data.strip().split("\n")

def to_int(item):
    new_list = []
    for i in item:
        if i != '':
            new_list.append(int(i))

    return new_list

cards_dict = {}

for i, card in enumerate(all_cards):
    if i not in cards_dict:
        cards_dict[i] = 1

    win = 0
    no_id = card.split(":")
    container = no_id[1].split("|")
    your_numbers = to_int(container[0].strip().split(" "))

    winning_numbers = to_int(container[1].strip().split(" "))


    for num in your_numbers:
        if num in winning_numbers:
            win += 1

    for next in range(i + 1, i + win + 1):
        cards_dict[next] = cards_dict.get(next, 1) + cards_dict[i]

print(sum(cards_dict.values()))


