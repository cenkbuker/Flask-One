from forex_python.converter import CurrencyRates, CurrencyCodes
currency_rates = CurrencyRates()
symbol = CurrencyCodes()

def convert(unit_input,unit_output,amount):
    try:
        currency_rates.get_rates(unit_input)
    except:
        return {"outcome":"failed","reason":"Wrong input on input currency"}
    try:
        currency_rates.get_rates(unit_output)
    except:
        return {"outcome":"failed","reason":"Wrong input on output currency"}
    try:
        amount = float(amount)
    except:
        return {"outcome":"failed","reason":"Amount should be float"}

    final = round(currency_rates.convert(f'{unit_input}',f'{unit_output}',amount),2)
    code = symbol.get_symbol(f'{unit_output}')
    return {"outcome":"success","value":final, "symbol":code}