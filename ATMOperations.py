from ATMExcept import  DepositError,WithDrawError,InSuffFundError
bal=500.0
def deposit():
    damt=float(input("Enter Ur Deposit Amount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print(f"\tUR Account xxxxxxx123 Credited With INR:₹{damt}")
        print(f"\tUr Account xxxxxxx123 Bal after Deposit INR:₹{bal} ")
def withdraw():
    global bal
    wamt=float(input("Enter Ur Withdraw Amount:"))
    if(wamt<=0):
        raise WithDrawError
    elif(wamt+500>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print(f"\tUR Account xxxxxxx123 Debited With INR:₹{wamt}")
        print(f"\tUR Account xxxxxxx123 Bal after Wihdraw INR:₹{bal}")
def balenq():
    print(f"\tUR Account xxxxxxx123 Bal INR:₹{bal}")