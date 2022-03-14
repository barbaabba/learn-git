def calc_born_year(n: int):
    current_year = 2022
    born_year = current_year - n
    return str(born_year)


if __name__ == "__main__":
    name = input("Whats your name ? : ")
    age = int(input("What your old ? : "))
    user_born_year = calc_born_year(age)
    print(f"{name}, You born on {user_born_year}")
