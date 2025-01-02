from Transaction import Transaction

class User:
    '''
        user of the system
    '''
    def __init__(self , name: str ,balance: float, historic_transaction: list[Transaction] = None):
        self._name = name
        self._balance = balance
        self._transactions = historic_transaction
        
    def get_name(self):
        return self._name
    
    def get_balance(self) -> str:
        return self._balance
    
    def print_balance(self):
        print(f'Balance : {self.get_balance()} FCFA')
        
    def add_montant(self , montant : float):
        self._balance = self._balance + montant
        
    def add_historic_transaction(self , transaction: Transaction, send: bool):
        transaction.set_send(send)
        self._transactions.append(transaction)
        
    def print_historic_transaction(self) -> str:
        libelle = 'Transaction de ' + self.get_name()
        for transaction in self._transactions:
            t = f'\nTransaction de {transaction.get_montant()} FCFA par {transaction.get_provider()} du {transaction.get_date()}. {"Sending" if transaction.get_send() else "Receiver"}'
            libelle += t
        return libelle
        