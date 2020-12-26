from find_by_boyera_mure import FindByBoyeraMure


def main():
    input_string = FindByBoyeraMure("Do you have iot drugs ?)")
    print(input_string.search("iot"))


if __name__ == '__main__':
    main()
