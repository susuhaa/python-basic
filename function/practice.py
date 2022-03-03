def open_account(): 
    print("새로운 계좌가 생성되었습니다.")

open_account()


#값을 전달하고 반환받는 경우가 있다.
def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

balance = 0 #잔액 
balance = deposit(balance, 1000)
print(balance)



