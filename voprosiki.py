import random
hamster = ["Sonya", "Pen", "Epam"]
fruit = ["pineapple", "cocos", "program"]
random.shuffle(hamster)
random.shuffle(fruit)
range(20)
for item in range(3):
    print(str(item + 1) + ". " + hamster[item] + " eats " + (fruit[item]) + ".")
