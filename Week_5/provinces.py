provinces = r"C:/Users/Arthur/repos/CSE111/Week_5/provinces.txt"


def main():
    province_names = get_provinces(provinces)
    return province_names

def get_provinces(filename):
    province_list = []
    with open(filename, "rt") as province_file:
        for province in province_file:
            text_line = province.strip()

            province_list.append(text_line)
        print(province_list)
        province_list.pop(0)
        province_list.pop(70)
        print(province_list)
        for i in range(len(province_list)):
            if province_list[i] == "AB":
                province_list[i] = "Alberta"
        print(province_list)
        print(province_list.count("Alberta"))

if __name__ == "__main__":
    main()