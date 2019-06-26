def compute_it(a, b, c, d):
    return not((a or b) and ()) and a and b or not (c and d) or (a and b or c)


def main():
    values = [True, False, True, False]
    a, b, c, d = values
    print(compute_it(a, b, c, d))


if __name__ == '__main__':
    main()
