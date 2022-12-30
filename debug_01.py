import traceback
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start programm')


def boxprint(symbol, weight, height):
    """ box print debug """

    if len(symbol) != 1:
        raise Exception('symbol need only 1 character')

    if weight <= 2:
        raise Exception('weight must be greater than 2')

    if height <= 2:
        raise Exception('height must be greater than 2')

    print(symbol * weight)

    for ii in range(height - 2):
        print(symbol + (' ' * (weight - 2)) + symbol)
    print(symbol * weight)


datas = (('*', 4, 4), ('0', 20, 5), ('x', 4, 3), ('Z', 3, 3))
for sym, wei, hig in datas:
    try:
        boxprint(sym, wei, hig)
    except Exception as err:
        print('An exception happened: ' + str(err))


datas2 = (('E', 10, 30), ('S', 40, 50))


def jointuple(datas_02) -> str:
    return ':'.join(str(datas_02))


result = map(jointuple, datas2)
print(list(result))

for a in datas2:
    for j in a:
        print(j, end=':')

print()

datas3 = [('E', 'D', 'S'), ('A', 'M', 'N')]
res = [':'.join(tups) for tups in datas3]
print(res)
for o in res:
    print(o)

res2 = list(map("".join, datas3))
print(res2)
for r in res2:
    print(r)

e = (('ABC', 10, 5, 'DEF'), ('KHJ', 90, 8, 'LKJ'))
print(','.join(map(str, e)))
for k in e:
    rr = ','.join(map(str, k))
    print(rr)

print('=' * 40)
for p, o, i in (('A', 1, 10), ('B', 2, 20), ('C', 3, 30), ('D', 4, 40)):
    print(p, end=' ')
    print(o, end=' ')
    print(i)

print('=' * 40)
for p in (('A', 1, 10), ('B', 2, 20), ('C', 3, 30), ('D', 4, 40)):
    print(p[0], end=' ')
    print(p[1], end=' ')
    print(p[2])
print('=' * 40)

"""
def spam():
    becom()


def becom():
    raise Exception('This is the error message.')


spam()
"""

try:
    raise Exception('This is the error message.')
except Exception as err:
    errorFile = open('errorTextMessage.log', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.', err)


ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
# assert ages[0] <= ages[-1]


def showcolor(dictcolor):
    for key in dictcolor.keys():
        if dictcolor[key] == "vert":
            dictcolor[key] = "jaune"
        elif dictcolor[key] == "jaune":
            dictcolor[key] = "red"
        elif dictcolor[key] == "red":
            dictcolor[key] = "vert"
        else:
            dictcolor[key] = "good"
    return dictcolor


print(showcolor({1: "lala", 2: "red", 3: "jaune"}))


def facteur(fact):
    """ function facteur """
    logging.debug('start of factorial(%s%%)' % fact)
    total = 1
    for h in range(1, fact + 1):
        total *= h
        logging.debug('h is ' + str(h) + ' total is ' + str(total))
    logging.debug('end of factorial(%s%%)' % fact)
    return total


print(facteur(5))
logging.debug('End of program')
