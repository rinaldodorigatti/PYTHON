import sys
import getopt


def fullname():
    first_name = None
    last_name = None

    av = sys.argv[1:]

    opts = ''

    try:
        opts, args = getopt.getopt(av, "f:l:", ["first=", "last="])
    except getopt.GetoptError as err:
        print("Error", err)
    for op, arg in opts:
        if op in ['-f', '--first']:
            first_name = arg
        elif op in ['-l', '--last']:
            last_name = arg
        else:
            print("Error: unknow option !!!")
            # assert False, "unhandled option"

    if first_name is None or last_name is None:
        first_name = "first_name  : Pas renseigné"
        last_name = "last_name   : Pas renseigné"

    print(first_name + "\n" + last_name)


fullname()
