answer = 5
guess = 0

while guess != answer:
    print("\nGuess a number between 1 and 10: ")
    guess = int(input())
    if guess == answer:
        print("Congrats you guessed correctly!")
    elif guess < answer:
        print("Your guess is to low. Guess higher")
    elif (guess > answer) and (guess <= 10):
        print("Your guess is to high. Guess lower. ")
    elif guess > 10:
        print("That number is out of range! ")

tree1 = input("Enter your first tree name : ")
tree2 = input("Enter your second tree name: ")

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

if x == y:
    print("x equals y")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")
