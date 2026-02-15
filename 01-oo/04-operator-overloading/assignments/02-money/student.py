class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount + other.amount, self.currency)
            raise RuntimeError("Mismatched currencies!")
    
    def __sub__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount - other.amount, self.currency)
            raise RuntimeError("Mismatched currencies!")
        
    def __mul__(self, value):
        return Money(self.amount * value, self.currency)
        
    def __str__(self):
        return f"Money({self.amount}, {self.currency})"



money = Money(10, "EUR")
print(money.amount)
print(money.currency)
print("-------")
print(Money(10, "EUR") + Money(20, "EUR"))
#print(Money(10, "EUR") + Money(20, "USD"))
print(Money(30, "EUR") - Money(10, "EUR"))
#print(Money(30, "EUR") - Money(10, "USD"))
print("-------")
print(Money(20, "EUR") * 5)