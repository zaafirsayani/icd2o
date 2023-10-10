print("Game 1: ")
game1opponentname = input("Opponents name: ")
game1points = int(input("Your points: "))
game1_opponentpoints = int(input("Opponents points: "))

print()

print("Game 2: ")
game2opponentname = input("Opponent name: ")
game2points = int(input("Your points: "))
game2_opponentpoints = int(input("Opponents points: "))

print()

print("Game 3: ")
game3opponentname = input("Opponent name: ")
game3points = int(input("Your points: "))
game3_opponentpoints = int(input("Opponents points: "))

print()

print("Game 4: ")
game4opponentname = input("Opponents name: ")
game4points = int(input("Your points: "))
game4_opponentpoints = int(input("Opponents points: "))

print()

print("Game 5: ")
game5opponentname = input("Opponents name: ")
game5points = int(input("Your points: "))
game5_opponentpoints = int(input("Opponents points: "))

player_name= input("Enter your name: ")

box1 = game1points/36
box2 = game2points/36
box3 = game3points/36
box4 = game4points/36
box5 = game5points/36
print()
print("Dots and Boxes Score Tracker")
print()
print(f"Player's Name: {player_name}")
print()
print(f"{'Opponent':<15}{'Your Points':<15}{'Opponent Points':<15}{'Box%':<15}")
print(f"{'===================================================================':<60}")
print(f"{game1opponentname:<15}{game1points:<15}{game1_opponentpoints:<15}{box1:<15.2%}")
print(f"{game2opponentname:<15}{game2points:<15}{game2_opponentpoints:<15}{box2:<15.2%}")
print(f"{game3opponentname:<15}{game3points:<15}{game3_opponentpoints:<15}{box3:<15.2%}")
print(f"{game4opponentname:<15}{game4points:<15}{game4_opponentpoints:<15}{box4:<15.2%}")
print(f"{game5opponentname:<15}{game5points:<15}{game5_opponentpoints:<15}{box5:<15.2%}")
print(f"{'===================================================================':<60}")
print()
totalpoints=game1points+game2points+game3points+game4points+game5points
opponentpoints=game1_opponentpoints+game2_opponentpoints+game3_opponentpoints+game4_opponentpoints+game5_opponentpoints
percentagepoints = totalpoints / (totalpoints + opponentpoints)
print("Summary")
print(f"Total points: {totalpoints}")
print(f"Opponent point total: {opponentpoints}")
print(f"Percentage points received: {percentagepoints:.2%}")
