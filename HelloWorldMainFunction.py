# define a main() to start py script execution, this module would be the main program
# Not to be used as an import!

def main():
    print("Hello, World!")

    name = input("What is your name?: ")

    print("Nice to meet you,", name)
# end of Main()

if __name__ == "__main__":
    main()