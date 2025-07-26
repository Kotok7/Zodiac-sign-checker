import time

def main():
    print("Zodiac Sign Checker")

    month = input("What month were you born in? ")

    day = input("What day of the month were you born? ")

    _ = input("Repeat, I didn't hear it. ")

    _ = input("What year did the Roman Empire fall? ")

    print(f"Idk about your zodiac sign, but I know you were born on {day} {month}.")
    time.sleep(3)
    print("Bye")
    time.sleep(2)

if __name__ == "__main__":
    main()
