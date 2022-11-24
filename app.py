from flask import Flask, request, render_template, flash, redirect
from converter_service import convert
app = Flask(__name__)
app.config["SECRET_KEY"]= "super-secret"


@app.route("/")
def homepage():
    """Homepage"""
    return render_template("converter.html")
    
@app.route("/process",methods=["GET"])
def process():
    unit_input = request.args["currency1"].upper()
    unit_output = request.args["currency2"].upper()
    amount=request.args["amount"]

    result = convert(unit_input,unit_output,amount)
    
    if result["outcome"]=="failed":
        flash(result["reason"])
        return redirect("/")

    return render_template("/result.html", result = result["value"], symbol=result["symbol"])


