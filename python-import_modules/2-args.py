#!/usr/bin/python3
if __name__ == "__main__":
        import sys

        for i in range(0, len(sys.argv)):
                i = i + 1

        i = i - 1

        if i == 1:
            print("{} argument:".format(i))
        elif i == 0:
            print("{} arguments.".format(i))
        else:
            print("{} arguments:".format(i))

            for a in range(0, len(sys.argv)):
                if a != 0:
                    print("{}: {}".format(a, sys.argv[a]))
