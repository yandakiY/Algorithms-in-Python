import datetime
from Provider import Provider
from User import User


class Transaction:
    '''
        Exchange between two part which money
    '''
    def __init__(self , exp: User , dest : User , montant: float , provider: Provider , date_transaction: datetime.date):
        self._montant = montant
        self._provider = provider
        self._date_transaction = date_transaction
        self._exp = exp
        self._dest = dest
        self._send = False
    
    def print(self) -> str:
        return f'Montant : {self.get_montant()} FCFA\n, Moyen de paiement : {self.get_provider()},\n Date Transaction : {self.get_date()} '
    
    def get_date(self) -> str:
        return f'{self._date_transaction.day}/{self._date_transaction.month}/{self._date_transaction.year}'
    
    def get_montant(self) -> float:
        return self._montant
    
    def get_provider(self) -> str:
        return self._provider.get_name()
    
    def get_exp(self):
        return self._exp
    
    def get_dest(self):
        return self._dest
    
    def set_send(self, send: bool):
        self._send = send
        
    def get_send(self):
        return self._send
    
    def transfert_argent(self , dest: User , montant: float):
        
        if (self.get_montant() > montant):
            print('Operation impossible !!!')
            return

        # decrement balance exp
        self._exp.add_montant(-montant)
        # increment balance dest
        dest.add_montant(montant)
        
        # add transaction to historic of exp 
        self._exp.add_historic_transaction(self , True)
        # add transaction to dest
        copy_transaction = self
        dest.add_historic_transaction(copy_transaction , False)
        
    
    def montant_apres_deduction(self) -> str:
        montant = self.get_montant() * self._provider.get_per()
        return f'Montant apres deduction : {montant}'
    