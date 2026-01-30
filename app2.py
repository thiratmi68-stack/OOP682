from models.bankaccount import Bankaccount

myaccount = Bankaccount(1000)
youraccount = Bankaccount(2000)

our_acc = myaccount + youraccount
print(our_acc)