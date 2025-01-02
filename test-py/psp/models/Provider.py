
class Provider():
    
    def __init__(self , name : str, per : float):
        self._name = name
        self._per = per
        
    def get_name(self) -> str:
        return self._name
    
    def get_per(self) -> float:
        return self._per