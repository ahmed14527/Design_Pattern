class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CurrencyConverter(metaclass=Singleton):
    rates = {'USD': {'EGP': 15.69}, 'EGP': {'USD': 0.0637}}

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        else:
            return amount * self.rates[from_currency][to_currency]

if __name__ == "__main__":
    converter = CurrencyConverter()

    amount_in_usd = 100
    amount_in_egp = converter.convert(amount_in_usd, 'USD', 'EGP')
    print(f"{amount_in_usd} USD is equivalent to {amount_in_egp} EGP.")

    amount_in_egp = 1000
    amount_in_usd = converter.convert(amount_in_egp, 'EGP', 'USD')
    print(f"{amount_in_egp} EGP is equivalent to {amount_in_usd} USD.")