from die import Die
die = Die(10)
money = 100
results = []
play_game = input("do you wanna play? press y if yes press something else if no")
while play_game == "y":
    for roll_num in range(10):
        result = die.roll()
        results.append(result)
        if result == 9:
            print("you won")
            money = money +1000 
    game_rules = input("do you wanna continue? type y to countinue and n to stop")
    if game_rules == "y":
        money = money-10
        print(money)
    if game_rules == "n":
        print (money)
        break