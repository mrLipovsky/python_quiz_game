print("Welcome to my Weed shop!")

playing = input("Do you want something? ")

score = 1

if playing.lower() != "yes":
        quit(print("Fuck off!"))

answer = input("Are you 18 Years old? ")
if answer.lower() == "yes":
    print("Perfect ")
    
else:
    print("Fuck off!")
    quit()

answer = input("What drug do you want to buy? I have weed1, weed2, weed3: ")
if answer.lower() == "weed1":
    print("Perfect, that is good a weed  ")
else:
    print("Fuck off!")
    quit()

answer = input("It will be 5Eur. ")
if answer.lower() == "ok":
    print("Do you have money? ")
elif answer.lower() == "yes":
    print("You have paid 5eur")
    score += 5
else:
    print("Fuck off!")
    quit()

print("You have bought " + str(score) + " weed for 5Eur")

