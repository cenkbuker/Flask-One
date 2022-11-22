from flask import Flask, request, render_template, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
app = Flask(__name__)
app.config["SECRET_KEY"]= "super-secret"

c = CurrencyRates()


@app.route("/")
def homepage():
    """Homepage"""
    return render_template("converter.html")
    
@app.route("/process",methods=["POST","GET"])
def process():
    first_currency = request.args["currency1"].upper()
    final_currency = request.args["currency2"].upper()
    try:
        amount = int(request.args["amount"])
        final = round(c.convert(f'{first_currency}',f'{final_currency}',amount),2)
        symbol = CurrencyCodes()
        code = symbol.get_symbol(f'{final_currency}')

        return render_template("/result.html", result = final, symbol=code)
    except:
        None
    try:
        c.get_rates(first_currency)
    except:
        flash('Wrong input on currency1')
        return redirect("/")
    try:
        c.get_rates(final_currency)
    except:
        flash('Wrong input on currency2')
        return redirect("/")
    try:
        amount = int(request.args["amount"])
        return redirect("/convert")
    except:
        flash('Wrong input on amount')
        return redirect("/")

