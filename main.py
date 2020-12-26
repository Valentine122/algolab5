from boyer_mure import BoyerMure


def main():
    input_string = BoyerMure("Do you have iot drugs ?)")
    print(input_string.search("iot"))


if __name__ == '__main__':
    main()
