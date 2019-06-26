def print_it(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g)


def main():
    msg = "Hej code checker, please check this code."
    a, b, c, d, e, f, g = msg.split()
    print_it(a, b, c, d, e, f, g)


if __name__ == '__main__':
    main()
