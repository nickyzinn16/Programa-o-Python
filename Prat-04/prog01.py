import random
num = (random.randint(1,20))
print(f"{num}")

# Gerar o numero decimal
num2 = random.random()
print(f"{num2}")

num3 = random.uniform(5,6)
print(f"{num3}")

# Escolha de elemento de lista
modulos = ["ASGBD", "AC", "MSI", "MMSI", "SS"]
chosen_mod = random.choice(modulos)
print(f"{chosen_mod}")

numbers = [1,2,3,4,5,6,7,8]
random.shuffle(members)
print(f"{numbers}")

outter_list = random.sample(numbers, 4)
print(outter_list)



