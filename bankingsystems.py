
print("="*501)

customerNames = ['m.mohith','k.kiran','y.nagaraju','j.janvi','v.ganesh','ch.pooja']
customerPins = ['7894', '1212', '7410', '3698', '2580','1414']
customerBalances = [50000, 45000, 75000, 100000, 90000,95000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 6
i = 0


while True:
    # os.system("cls")
    print("=====================================")
    print(" ----Welcome to AI Bank----       ")
    print("*************************************")
    print("*** 1. Open a new account         ***")
    print("*** 2. Money Withdrawl            ***")
    print("*** 3. Deposit Money              ***")
    print("*** 4. Check Customers & Balance  ***")
    print("*** 5. Exit                       ***")
    print("*************************************")
    
    SelectOptions = input("Select your Options from the above menu : ")
    if SelectOptions == "1":
        print("Option 1 is selected")
        NOC = eval(input("Number of Customers : "))
 
        i = i + NOC
        if i > 6:
            print("\n")
            print("Customer registration exceed reached")
            i = i - NOC
        else:
           
            while counter_1 <= i:
                name = input("Enter Fullname : ")
                customerNames.append(name)
                pin = str(input("Please select a new pin : "))
                customerPins.append(pin)
                balance = 0
                deposit = eval(input("Please make deposit to start an account : "))
                balance = balance + deposit
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account is created successfully----")
                print("\n")
                print(" now you are a customer of AI bank : ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
                
        mainMenu = input("Please press enter key to go back to main menu or exit ...")
    elif SelectOptions == "2":
        j = 0
        print("Options 2 is selected")

        while j < 1:
            k = -1
            name = input("Please Enter the name : ")
            pin = input("Please Enter the pin : ")
            
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Input value to Withdraw : "))
                        if withdrawal > balance:
                            
                            deposit = eval(input("Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            balance = balance + deposit
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n") 
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu or exit ...")
    elif SelectOptions == "3":
        print("Options 3 is selected")
        n = 0
        while n < 1:
            k = -1
            name = input("Please Enter the name : ")
            pin = input("Please Enter the pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition 
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
 
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif SelectOptions == "4":
        print("Options 4 is selected")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")

        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu or exit ...")

    elif SelectOptions == "5":
        print("Options 5 is selected")
        print("Thank you for using our AI banking system!")
        print("\n")
        print("wisit again")
        print("Have a nice day")
        
        break
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
       
        mainMenu = input("Please press enter key to go back to main menu or exit ...")
