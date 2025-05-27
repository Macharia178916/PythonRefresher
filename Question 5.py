def main():
    x = 0
    y = 20

    while y >= 6:
        y -= 4
        x += 2 / y

    print("Final value of x:", x)

# Run the main function
main()