print("""
****************
ATM Program
1. Balance Inquiry
2. Deposit
3. Withdrawal
4. Card Return
****************""")

balance = 1000
username = "hasan"
password = 1234
login_attempts = 3

while True:
    sys_username = input("Please enter your username:")
    sys_password = int(input("Please enter your password:"))
    
    if login_attempts == 0:
        break
    elif username != sys_username and password == sys_password:
        print("Incorrect username")
        login_attempts -= 1
        continue
    elif username == sys_username and password != sys_password:
        print("Incorrect password")
        login_attempts -= 1
        continue
    elif username != sys_username and password != sys_password:
        print("Incorrect username and password")
        login_attempts -= 1
        continue
    else:
        while True:
            print("Login successful")
            choice = int(input("Please select the operation you want to perform:"))

            if choice == 1:
                print("Total Balance:", balance)
                continue
            
            elif choice == 2:
                while True:
                    deposit_amount = input("Please enter the amount you want to deposit:")
                    if "q" == deposit_amount:
                        break
                    else:
                        deposit_amount = int(deposit_amount)
                        if deposit_amount > 20000:
                            print("The deposit limit is 20,000 TL")
                            continue
                        elif deposit_amount < 0:
                            continue
                        else:
                            balance += deposit_amount
                            print("Total balance:", balance)
                            break
            
            elif choice == 3:
                while True:
                    withdrawal_amount = input("Please enter the amount you want to withdraw:")
                    if "q" == withdrawal_amount:
                        break
                    else:
                        withdrawal_amount = int(withdrawal_amount)
                        if withdrawal_amount > balance:
                            print("Insufficient funds in your account")
                            continue
                        elif withdrawal_amount > 5000:
                            print("The withdrawal limit is 5,000 TL")
                            continue
                        else:
                            balance -= withdrawal_amount
                            print("Remaining balance in your account:", balance)
                            break
            
            else:
                choice == 4
                break
