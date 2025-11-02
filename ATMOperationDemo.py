from ATMMenu import  menu
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithDrawError,InSuffFundError
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDon't Enter -ve or Zero for Deposit Amount:")
                except ValueError:
                    print("\t Don't Enter ALNUMS/STRS/SPECIAL AYMBOLS FOR DEPOSITE AMOUNT")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T ENTER -VE OR ZERO FOR WITHDRAW AMOUNT")
                except InSuffFundError:
                    print("\tUR ACCOUNT DOES NOT CONTAIN SUFF.FUND")
                except ValueError:
                    print("\t Don't Enter ALNUMS/STRS/SPECIAL AYMBOLS FOR DEPOSITE AMOUNT")
            case 3:
                balenq()
            case 4:
                print("\tThnx for using the ------Bank")
                break
            case _:
                print("\t Ur selection of Operation is wrong--Try Again!!!")
    except ValueError:
        print("\t Don't Enter ALNUMS/STRS/SPECIAL AYMBOLS FOR DEPOSITE AMOUNT")