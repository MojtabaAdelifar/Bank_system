from classes.User import User

person1 = User("Mojtaba Adelifar")
person2 = User("Ali Siyani")
person3 = User("AliReza Talebi")
person4 = User("Pezhman ZarePour")

people = {"1348": person1, "2001": person2, "9480": person3, "0410": person4}

number = input("Enter your number: ")
person = people[number]
print("You are", person.name)


check = True
while check:

    person.menu()

    choice = int(input("Choose the function: "))

    if choice == 1:
        print("Your credit is:", person.getCredit())

    elif choice == 2:
        depositAmount = float(input("Enter deposit amount: "))
        person.deposit(depositAmount)

    elif choice == 3:
        decreasedAmount = float(input("How much money do you need? "))
        person.decrease(decreasedAmount)

    elif choice == 4:
        print("Thanks for using this ATM")
        print("Have a greate time")
        check = False

