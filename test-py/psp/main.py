from models.User import User
from models.Transaction import Transaction
from models.Provider import Provider
import datetime

def main():
    '''
        Process of Payment Processing
    '''
    user1 = User("Michel", 0)
    user2 = User("Yves", 5000)
    
    # provider
    orange = Provider("Orange", 0.01)
    mtn = Provider("MTN CI", 0.01)
    
    print("Historic of transaction of user1 \n" , user1.print_historic_transaction())
    print("Historic of transaction of user2 \n" , user2.print_historic_transaction())
    
    # make transactions
    now = '02/02/2025'
    t1 = Transaction(user1 , user2, 500, orange, date_transaction=now)
    t2 = Transaction(user1 , user2, 1500, mtn, date_transaction=now)
    
    t1.transfert_argent()
    t2.transfert_argent()
    
    print(t1.montant_apres_deduction())
    print(t2.montant_apres_deduction())
    
    print("Historic of transaction of user1 \n" , user1.print_historic_transaction())
    print("Historic of transaction of user2 \n" , user2.print_historic_transaction())




main()