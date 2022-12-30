
import platform
import subprocess


def main():
    def ping():
        """Ping servers"""

        print("-" * 51)
        print("| %-30s| %-15s |" % ("Hostname", "Status"))
        print("-" * 51)
        try:
            with open("FILES/hostname2", "r") as f:
                com = 'ping'
                countc = '-c'
                count = '1'
                ipv4 = '-4'
                temp = f.read().splitlines()
                for j in sorted(temp):
                    command = [com, countc, count, ipv4, j]
                    response = subprocess.run(command, capture_output=True)
                    if response.returncode:
                        print("| %-30s| \x1b[0;32;47m%-15s\x1b[0m |" % (j, "Success"))
                    else:
                        print("| %-30s| \x1b[0;31;47m%-15s\x1b[0m |" % (j, "Failed"))
        except OSError as err:
            print("Error to ping server : %s : %s" % (err, err.errno))
        finally:
            print("-" * 51)

    ping()


if __name__ == '__main__':
    main()
