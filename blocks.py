# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2,i ** 3))
#     print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? : ".format(name)))
# if statements
if age >= 18:
    print("You are old enough to vote.")
    vote = input("Would you like to vote?  Y or N : ")
    if (vote == "Y") | (vote == "y"):
        voteChoice = input("Are you a republican or communist?\n Type R or C : ")
        if (voteChoice == "R") | (voteChoice == "r"):
            print("You are an American Patriot! Go ahead and vote! ")
        elif (voteChoice == "C") | (voteChoice == "c"):
            print("You are a communist bastard! Get the hell out of our country!! ")
else:
    print("\n" + name +  ", Please come back in {0} years. ".format(18-age))



answer = 5
guess = 0


print("\nGuess a number between 1 and 10: ")
guess = int(input())
if guess == answer:
    print("Congrats you guessed correctly!")
elif guess > answer:
    print("Your guess is to high. Guess lower. ")
elif guess < answer:
    print("Your guess is to low. Guess higher")

