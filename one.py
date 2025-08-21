from error import inst
def withdral_amount():
     amount = int(input("enter amount"))
     acc_balance = 5000
     if acc_balance<amount:
      raise insuffcientbalerror('go enjoy sat')
     else:
        print('enjoy')
        print("follow rules")
        withdral_amount()
        