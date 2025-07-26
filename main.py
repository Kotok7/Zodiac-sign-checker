import time

def main():
    print("Sprawdzacz znaku zodiaku")

    month = input("W jakim miesiącu się urodziłeś? ")

    day = input("Jaki jest twój dzień urodzenia? ")

    _ = input("Powtórz bo nie usłyszałem ")

    _ = input("Podaj rok upadku Cesarstwa Rzymskiego ")

    print(f"nwm jaki masz ten znak ale wiem że urodziłeś się {day} {month}")
    time.sleep(3)
    print("pa")
    time.sleep(2)

if __name__ == "__main__":
    main()