from exchanges import Exchange

class ExchangeManager:
    def __init__(self, market):
        self.market = market
        self.exchange = Exchange(market)
        self.purchases = []
    
    def get_balances(self):
        self.exchage.get_balances()
    
    def get_price(self):
        self.exchange.get_price("asks")
    
    # def buy_cripto(self):
    #     self.exchange.buy_crypto(10000)
    
    # def sell_crypto(self):
    #     self.exchange.sell_crypto(10000)

        

    
