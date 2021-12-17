class MoneyBox:
    def __init__(self, capacity):
        # hucha capacity
        self.capacity = capacity

    def can_add(self, v):
        # True, si podemos a;adir v monedas, False in otro caso
        return True if (self.capacity - v) >= 0 else False

    def add(self, v):
        # meter v monedas en la hucha
        self.capacity -= v

        
hucha = MoneyBox(10)
while True:
    print(f'Hay sitio para {hucha.capacity} monedas en la hucha')
    coins = int(input('Cuanto monedas metemos?'))
    if hucha.can_add(coins):
        hucha.add(coins)
    else:
        print('No cabe tanto')
