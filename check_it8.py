def do_it(value):
    if 0 < value < 10:
        return 'low'
    elif 11 < value < 20:
        return 'fair'
    elif 21 < value < 30:
        return 'medium'
    elif 31 < value < 40:
        return 'high'
    return 'super_high'


def main():
    print(do_it(42))


if __name__ == '__main__':
    main()
