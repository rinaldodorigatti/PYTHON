
import socket


def main():
    def ping_server(server: str, port: int, timeout=3):
        """ping server"""
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server, port))
        except OSError as error:
            return False
        else:
            s.close()
            return True

    print("------------------------ START OF PROGRAM -------------------------")
    pport = int(input("Which port do you want to test ? : "))
    try:
        with open("FILES/hostname2", mode="r") as f:
            temp = f.read().splitlines()
            for h in sorted(temp):
                status = ping_server(h, port=pport, timeout=2)
                if status:
                    print("| %-10s| %-40s| %-10s|" % ("System", h, "is UP"))
                else:
                    print("| %-10s| %-40s| %-10s|" % ("System", h, "is DOWN"))
    except FileNotFoundError as ferr:
        print("Error file : ", ferr)
    finally:
        print("------------------------- END OF PROGRAM --------------------------")


if __name__ == '__main__':
    main()
