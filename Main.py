import Armstrong
import Palindrome
import Happy
import Harshad

while True:

    num = int(input("\nEnter a number: "))

    print("\n----- CHOOSE AN OPERATION -----")
    print("1. Check Armstrong")
    print("2. Check Palindrome")
    print("3. Check Happy")
    print("4. Check Harshad")
    print("5. Check All")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if Armstrong.check_armstrong(num):
            print(num, "is an Armstrong number.")
        else:
            print(num, "is not an Armstrong number.")

    elif choice == 2:
        if Palindrome.check_palindrome(num):
            print(num, "is a Palindrome number.")
        else:
            print(num, "is not a Palindrome number.")

    elif choice == 3:
        if Happy.check_happy(num):
            print(num, "is a Happy number.")
        else:
            print(num, "is not a Happy number.")

    elif choice == 4:
        if Harshad.check_harshad(num):
            print(num, "is a Harshad number.")
        else:
            print(num, "is not a Harshad number.")

    elif choice == 5:
        print("\nResults for", num)

        print("Armstrong :", Armstrong.check_armstrong(num))
        print("Palindrome:", Palindrome.check_palindrome(num))
        print("Happy     :", Happy.check_happy(num))
        print("Harshad   :", Harshad.check_harshad(num))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")