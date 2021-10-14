class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 10000")

    def withdrawl(self,amount):
        new_amount = 10000 - amount
        print("You have withdrawn  "+str(amount) +". Your remaining balance  "+ str(new_amount))


def main():
    Card_number = input("Insert your cardnumber: ")
    pin_number  = input("Enter your pin number: ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your procedure:- ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("Enter procedure number 1 or 2:- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.withdrawl(amount)
    else:
        print("Enter a vaild number:")


if __name__ == "__main__":
    main()