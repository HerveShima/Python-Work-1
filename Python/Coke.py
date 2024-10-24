def coke_machine():
    price = 50
    inserted = 0
    
    while inserted < price:
        coin = int(input("Insert a coin (5, 10, or 25): "))
        
        if coin not in (5, 10, 25):
            print("Invalid coin. Please insert a coin of 5, 20, or 25.")
            continue
        
        inserted += coin
        amount_due = price - inserted
        
        if inserted < price:
            print("Amount due: ",amount_due," units.")
        elif inserted > price:
            change = inserted - price
            print("Thank you, Here is your coke. Amount owed: ",change," units.")
            break
        else:
            print("Thank you! Here is your Coke.")

coke_machine()
