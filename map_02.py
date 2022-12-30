import re

# map, filtre, re, tuple, list, eval


def main():
    numbers = [2, 4, 6, 8, 10]


    def square(number):
        return number * number


    square_map = map(square, numbers)
    square_map_list = list(square_map)

    print(square_map_list)


    def calculator(n):
        return n*n


    chiffres = (1, 2, 3, 4, 5)
    chiffres_map = map(calculator, chiffres)
    print(chiffres_map)

    chiffres_sett = set(chiffres_map)
    # chiffres_list = list(chiffres_map)
    # print(chiffres_list)
    print(chiffres_sett)

    chiffres01 = (3, 6, 9, 12)
    result = map(lambda x: x+x, chiffres01)
    result_set = set(result)
    print(result_set)

    num01 = [10, 20, 30, 40]
    num02 = [1, 2, 3, 4]
    map_nums = map(lambda n1, n2: n1 + n2, num01, num02)
    map_nums_list = list(map_nums)
    print(map_nums_list)


    # filter

    list_chiffre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def check_numbers(nums):
        if nums % 2 == 0:
            return True
        return False


    return_modulo = filter(check_numbers, list_chiffre)
    return_modulo_list = list(return_modulo)
    print(return_modulo_list)

    letters = ['a', 'z', 'y', 'e', 'f', 'r', 'q', 'h', 'm', 'l']


    def get_vowel(vow):
        wovel = ['a', 'e', 'i', 'o', 'u']
        return True if vow in wovel else False


    filter_letters = filter(get_vowel, letters)
    filter_letters_set = set(filter_letters)
    print(filter_letters_set)


    letters_1 = ['ahs', 'zud', 'ah', 'ehd', 'fhq', 'jkc', 'ah']
    filter_letters_1 = filter(lambda m: len(m) == 2, letters_1)
    filter_letters_1_list = list(filter_letters_1)
    print(filter_letters_1_list)

    letters_2 = ['ah', 'zu', 'ah', 'ehd', 'fhq', 'jkc', 'ah']
    letters_2_2 = ['ah', 'zu']
    filter_letters_2 = filter(lambda m: m in letters_2_2, letters_2)
    filter_letters_2_list = list(filter_letters_2)
    print(filter_letters_2_list)

    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array2 = [3, 10]
    filter_array = filter(lambda c: c not in array2, array1)
    filter_array_tuple = tuple(filter_array)
    print(filter_array_tuple)


    def lenOfString(string):
        if len(string) == 2:
            return True
        else:
            return False


    letters_4 = ['ai', 'zuf', 'ah', 'ehd', 'fhq', 'jkc', 'ai']
    letters_4_filter = list(filter(lenOfString, letters_4))
    print(letters_4_filter)


    def checkifany(mainstr, listofstr):
        for substr in listofstr:
            if substr in mainstr:
                return (True, substr)
        return (False, "")


    mainstr = "Je recherche un mot dans une phrase"
    liststr = ["dans"]
    resultat = checkifany(mainstr, liststr)
    if resultat[0]:
        print("Sub string found : ", resultat[1])
    else:
        print("Sub string NOT found")

    res, b = checkifany(mainstr, liststr)
    print(res, b)

    mainStr = "This is a sample String with sample message."
    listOfstrs = ['sample', 'String', 'with']
    result = all(([True if subStr in mainStr else False for subStr in listOfstrs]))
    if result:
       print('All strings from list Found in main String ')


    searchObj = re.compile("sample", flags=re.IGNORECASE)
    # searchObj = re.compile("sample")
    mainStr1 = "This is a Sample String with Sample message."
    matchObj = searchObj.search(mainStr1)
    if matchObj:
        print("sample is in mainStr1")
    else:
        print("sample is NOT in mainStr1")


    strg = "Hello!!!"
    print("**** Iterate over string with index using range() ****")
    for k in range(len(strg)):
        print(strg[k], end=' ')
    print("")

    strg1 = "Hello!!!"
    tabb = []
    print("**** Iterate over string with index using range() ****")
    for k in range(len(strg1)):
        tabb.append(strg1[k])
    print("")
    total = ''
    for j in tabb:
        total += j + " | "
    print(total)

    numTuple = ('1', '2', '3', '4')
    separator = ', '
    print(separator.join(numTuple))

    numList = ['UN', 'DEUX', 'TROIS', 'QUATRE']
    sep = ':'
    let = 'abc'
    print(sep.join(numList))
    print(let.join(numList))

    numSetDate = set({'10', '03', '2022'})
    numSetHeure = set({'08', '56', '28'})
    sortedNumSet = sorted(numSetDate)
    sortedNumSetHeure = sorted(numSetHeure)
    sepDate = '.'
    sepHeure = ':'
    print(numSetDate)
    print(sepDate.join(sortedNumSet), sepHeure.join(numSetHeure))

    x = 1
    print(eval('x + 1'))


    def calculatePerimeter(l):
        return 4*l


    def calculateArea(l):
        return l*l

    expression = input("Type a function [calculatePerimeter(l), calculateArea(l)] : ")

    for l in range(1, 5):
        if (expression == 'calculatePerimeter(l)'):
            print("If length is ", l, ", Perimeter = ", eval(expression))
        elif (expression == 'calculateArea(l)'):
            print("If length is ", l, ", Area = ", eval(expression))
        else:
            print('Wrong Function')
            break


if __name__ == '__main__':
    main()
