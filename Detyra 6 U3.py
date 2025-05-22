def isInteger(s):
    if len(s) == 0:
        return False
    if s[0] in ["+", "-"]:
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()

def main():
    s = input("Enter a string: ")
    if isInteger(s):
        print("That is a valid integer.")
    else:
        print("That is not a valid integer.")
    main()
if __name__ == "__main__":
    main()