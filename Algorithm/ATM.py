# ATM Question (Code Chef)

# Summary
# If Withdraw Amount not divisible by 5 --> return bank balance
# If Withdraw Amount > Bank Balance - Charge --> return bank balance
# If Withdraw Amount < Bank Balance - Charge --> return new bank balance

# Example:
# Withdraw Amount: 30, Bank Balance: 120.00
# Answer: 89.50

# ==============================================================

# O(1) Time | O(1) Space

def atm(withdraw, totalBalance):
    if withdraw % 5 == 0:
        CHARGE = 0.50
        if withdraw > totalBalance - CHARGE:
            return "{0:.2f}".format(totalBalance)
        else:
            remainingBalance = totalBalance - withdraw - CHARGE
            return "{0:.2f}".format(remainingBalance)
    return "{0:.2f}".format(totalBalance)

if __name__ == '__main__':
    withdraw, totalBalance = map(float, input().split())
    print(atm(withdraw, totalBalance))
