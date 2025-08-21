from errors import infbaderr
def withdrawl_amount()
    amount= int(input('enter---'))
    acc_bal=5000
    try:
        if acc_bal<amount:
            raise insuffialbaderror('low bal__')
        
        else:
            print("enjoy")
        except insuffisentbalerror as err:
              p(error.msg)
        print("follow rules")
        withdrawl_amount()