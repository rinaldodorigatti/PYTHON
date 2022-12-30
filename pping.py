
from ping3 import ping, verbose_ping, errors

"""temp = [line.rstrip('\n') for line in f]
temp = [line[:-1] for line in f]
temp = [line.rstrip('\n') for line in f]
print(f.readlines())
test = [f.strip('\n\r') for f in temp]"""


def main():
    try:
        with open("hostname2", mode="r") as f:
            temp = f.read().splitlines()
            for h in sorted(temp):
                verbose_ping(h, timeout=2, count=1)
                try:
                    pp = ping(h, timeout=2, unit='ms')
                    if not pp:
                        print("Not OK", end=' ')
                    else:
                        print("OK", end=' ')
                except errors.Timeout as terr:
                    print("Timeout error ", terr)
                except errors.PingError as perr:
                    print("Ping error ", perr)
    except FileNotFoundError as ferr:
        print("Error file : ", ferr)
    finally:
        print("Program done")


if __name__ == '__main__':
    main()
