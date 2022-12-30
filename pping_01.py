
import subprocess as sp


def main():
    print("------------------------ START OF PROGRAM -------------------------")
    try:
        with open("FILES/hostname2", mode="r") as f:
            temp = f.read().splitlines()
            for h in sorted(temp):
                status, result = sp.getstatusoutput("ping -c1 -w2 " + h)
                if status == 0:
                    print("| %-10s| %-40s| %-10s|" % ("System", h, "is UP"))
                else:
                    print("| %-10s| %-40s| %-10s|" % ("System", h, "is DOWN"))
    except FileNotFoundError as ferr:
        print("Error file : ", ferr)
    finally:
        print("------------------------- END OF PROGRAM --------------------------")


if __name__ == '__main__':
    main()
