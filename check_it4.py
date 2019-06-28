def do_it(value):
    val2 = not(not(value))
    val3 = value and val2
    val4 = val2 and val3
    val5 = val3 and val4
    val6 = val4 and val5
    val7 = val5 and val6
    val8 = val6 and val7
    val9 = val7 and val8
    val10 = val8 and val9
    val11 = val9 and val10
    val12 = val10 and val11
    val13 = val11 and val12
    val14 = val12 and val13
    val15 = val13 and val14
    if value:
        if val2:
            if val3:
                if val4:
                    if val5:
                        if val6:
                            if val7:
                                if val8:
                                    if val9:
                                        if val10:
                                            if val11:
                                                if val12:
                                                    if val13:
                                                        if val14:
                                                            if val15:
                                                                print(value)


def main():
    do_it(True)


if __name__ == '__main__':
    main()
