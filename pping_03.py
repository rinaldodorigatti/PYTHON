
from tcping import Ping


def main():
    def ping_server():
        """Ping test servers"""

        print("------------------------ START OF PROGRAM -------------------------")
        try:
            pport = int(input("Which port do you need to test ? : "))
            with open("FILES/hostname2", "r") as f:
                temp = f.read().splitlines()
                for j in sorted(temp):
                    ping = Ping(j, port=pport, timeout=2)
                    ping.ping(1)
                    ret = ping.result.rows[0][2]
                    if ret:
                        print("\t\x1b[6;30;42mSuccess\x1b[0m")
                    else:
                        print("\t\x1b[6;30;41mFailed\x1b[0m")
        except OSError as err:
            print("Error to ping server : %s : %s : %s" % (j, err, err.errno))
        finally:
            print("------------------------- END OF PROGRAM --------------------------")

    ping_server()


if __name__ == '__main__':
    main()
