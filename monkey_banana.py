import random
class Monkey:
 def __init__(self, bananas):
 self.bananas = bananas
 def __repr__(self):
 return "Monkey with %d bananas." %self.bananas

monkeys = [Monkey(random.randint(0,50))for i in range(5)]
print("Random Monkeys")
print(monkeys)
def number_of_bananas(monkey):
 return monkey.bananas
print("Bananas with (first monkey):",number_of_bananas(monkeys[0]))
max_monkey = max(monkeys, key = number_of_bananas)
print("Max Monkey:",max_monkey)
