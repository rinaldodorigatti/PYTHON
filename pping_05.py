
import os


def main():
    print("-" * 50)
    print("| %-30s| %-15s|" % ("Hostname", "Status"))
    print("-" * 50)
    try:
        with open("hostname2", "r") as f:
            temp = f.read().splitlines()
            for j in sorted(temp):
                response = os.system("ping -c 1 -4 > /dev/null 2>&1 " + j)
                if response == 0:
                    print("| %-30s| \x1b[0;32;40m%-15s\x1b[0m|" % (j, "Success"))
                else:
                    print("| %-30s| \x1b[0;31;40m%-15s\x1b[0m|" % (j, "Failed"))
    except OSError as err:
        print("Error to ping server : %s : %s : %s" % (j, err, err.errno))
    finally:
        print("-" * 50)


if __name__ == '__main__':
    main()
