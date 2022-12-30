
import os
import getopt
import sys


def usage():
    path = "/home/rickyd/next.py"
    base = os.path.basename(path)
    print("Usage : python3", base) 
    print("[options]\n\t-h | --help\n\t-v | --verbose=True or False\n\t-o | --output=file name")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output=", "verbose="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"

    print(f"Verbose = {verbose}\toutput = {output}")


if __name__ == "__main__":
    main()
