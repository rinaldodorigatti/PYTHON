# python map

numbers = [2,4,6,8,10]

def square(number):
    return number * number

square_numbers = map(square, numbers)
square_numbers_list = list(square_numbers)
print(square_numbers_list)


nm = (1,2,3,4)
result = map(lambda x: x*x, nm)

result_list = set(result)
print(result_list)

num1 = [1,3,5,7]
num2 = [2,4,6,8]
result01 = map(lambda n1, n2: n1+n2, num1, num2)
result01_list = list(result01)
print(result01_list)

def myFunc(n):
    return len(n)

x = map(myFunc, ('bananas', 'apple', 'cherry'))
print(list(x))

def addChain(a, b):
    return a + b

v = map(addChain, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
vv = list(v)
for i in vv:
    print(i)

chiffres = [10, 15, 20, 25, 30]
mapped_chiffres = list(map(lambda c: c + 2 + 3, chiffres))
print(mapped_chiffres)
print(mapped_chiffres[0])
print(mapped_chiffres[2])


aquarium_creatures = [
	{"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
	{"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
	{"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
	{"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
	{"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
	{"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]

def assign_to_tank(aquarium_creatures, new_tank_number):
	def apply(x):
		x["tank number"] = new_tank_number
		return x
	return map(apply, aquarium_creatures)

assigned_tanks = assign_to_tank(aquarium_creatures, 42)
print(list(assigned_tanks))

base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)
