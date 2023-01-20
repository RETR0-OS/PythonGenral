def print_formatted(number):
    x = len("{0:b}".format(number))
    for i in range(1,number+1):
        print(" "*(x-len(str(i))-1), int(i), end="")
        print(" "*(x-len("{0:o}".format(i))), int("{0:o}".format(i)), end="")
        print(" "*(x-len("{0:x}".format(i))), "{0:x}".format(i).upper(),end="")
        print(" "*(x-len("{0:b}".format(i))), int("{0:b}".format(i)))

if __name__ == '__main__':
