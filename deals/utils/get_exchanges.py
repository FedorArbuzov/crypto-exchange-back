import enum


from pycoingecko import CoinGeckoAPI

coins_persent_buy = {'bitcoin': 0.047, 'usd': 0.045, 'rub': 0.00}
coins_persent_sell = {'bitcoin': 0.03, 'usd': 0.02, 'rub': 0.00}
    

def persent_buy(coin):
    return coins_persent_buy[coin.name]

def persent_sell(coin):
    return coins_persent_sell[coin.name]

class Bitcoin():
    def __call__(self): return 'BITCOIN'
    
    name = 'bitcoin'
    round_ = 8
   
class Usd():
    def __call__(self): return 'USDT'
    
    name = 'usd'
    round_ = 2
    
class Rub():
    def __call__(self): return 'RUB'
    
    name = 'rub'
    round_= 2
    
class Exchange(enum.Enum):
    BIT = Bitcoin()
    RUB = Rub()
    USD = Usd()


OPERATION_BUY = 'buy'
OPERATION_SELL = 'sell'


cg = CoinGeckoAPI()


def bitc_function(from_, to_):
    fr = from_.name
    to = to_.name
    coingecko_price = cg.get_price(ids=to, vs_currencies=fr)
    price = coingecko_price[to][fr]
    return price

def calc_function_buy(rate, amount):
    return round(amount / rate, 8)

def calc_function_sell(rate, amount):
    return round(rate * amount, 8)

def get_rate(from_, to_, operation):
    if operation == OPERATION_BUY:
        return round(bitc_function(from_, to_) * (1 + persent_buy(to_)), to_.round_)
    else:
        return round(bitc_function(from_, to_) * (1 - persent_sell(to_)), to_.round_)
    
    

def get_exchange_rate():
    ans = {'exchange_rates': []}
    for exch in Exchange:
        if exch != Exchange.RUB:
            ex = exch.value
            rub = Exchange.RUB.value
            
            val_buy = get_rate(rub, ex, OPERATION_BUY)
            val_sell = get_rate(rub, ex, OPERATION_SELL)
            ans['exchange_rates'].append({
                'currency_pair': ex(),
                'buy_rate': val_buy,
                'sell_rate': val_sell
            })
    return ans
