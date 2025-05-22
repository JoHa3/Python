def main ():
    total = 0
    line = input("Enter a number(blank to quit): ")
    while line != "":
        try:
            number = int(line)
            total += number
            print("Current total is", total)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        line = input("Enter a number(blank to quit): ")

    print("Final total is", total)
    
    if __name__ == "__main__":

        main()