f = open('input2.2.txt', 'r')

game_dict = {'red': 12,
             'green': 13,
             'blue': 14,
             }

games = []
power_sum = 0
# ans = 0

reds = 0
greens = 0
blues = 0

for line in f:
    reds = 0
    greens = 0
    blues = 0
    # flag = True
    x = line.strip()
    x = x.replace(';', ',')
    x = x.split(': ')
    x[0] = x[0].split(' ')
    x[0] = int(x[0][1])

    games = [game.split(' ') for game in x[1].split(', ')]

    for item in games:
        if item[1] == "blue" and int(item[0]) > blues:
            blues = int(item[0])
        elif item[1] == "green" and int(item[0]) > greens:
            greens = int(item[0])
        elif item[1] == "red" and int(item[0]) > reds:
            reds = int(item[0])

    power = reds * greens * blues
    power_sum += power
    # print("reds = ", reds, ", greens = ", greens, ", blues = ", blues, ", POWER = ", power)

print(power_sum)

    # if flag == True:
    #     alls.append(x)
    #     ans += x[0]


f.close()