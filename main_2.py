class BankAccount:
    def __init__(self,ac , name, bal):
        self.ac=ac
        self.name=name
        self.bal=bal
    def display_bal(self):
        print(f"{self.name} has {self.bal} in account {self.ac}")
    def deposite(self,amount):
        self.bal+=amount
        print(f"deposited {amount} to {self.name} account")
    def withdraw(self ,amt):
        if(self.bal > amt):
            print(f"withdrawn {amt} from {self.name} account")
            self.bal-=amt
        else:
            print("Insufficient balance")

ac1=BankAccount(1234567890,"Goutham",1000)
ac1.display_bal()
ac1.deposite(500)
ac1.withdraw(200)
ac1.display_bal()