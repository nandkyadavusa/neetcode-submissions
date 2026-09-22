class StoreItem:
    def __init__(self,names:str, price:float):
        self.name = names
        self.price = price


chips = StoreItem("Chips", 1.99) # Don't modify this line
print(chips.name, chips.price,sep="\n")
# TODO: Access the attributes of the chips object and display them


