class Account:
    def __init__(self,name:str, balance:int):
        self._name=name
        self._balance = balance

    def get_names(self) ->str:
        return self._name
        
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
