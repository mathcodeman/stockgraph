from flask import Flask,render_template,request,redirect
from pandas_datareader import data
from datetime import datetime
from bokeh.plotting import figure,show,output_file
from bokeh.embed import components
from bokeh.resources import CDN
from stock import plot
from stock_details import stock_detail



app=Flask(__name__)


@app.route("/stock",methods=["POST", "GET"])
def Stock():
    symbol=request.form.get("symbol")
    date1=request.form.get("Date1")
    date2=request.form.get("Date2")
    try:
        start=datetime(int(date1.split("-")[0]),int(date1.split("-")[1]),int(date1.split("-")[2]))
        end=datetime(int(date2.split("-")[0]),int(date2.split("-")[1]),int(date2.split("-")[2]))
        if start < end:
            try:
                result=plot(symbol,start,end)
                return render_template("home.html",script=result[0],div=result[1])
            except:
                msg="Could not find the symbol"
                return render_template("home.html",msg=msg)
        else:
            msg="Wrong date,please re-enter"
            return render_template("home.html",msg=msg)
    except:
        msg="Dude,seems like you missing some input"
        return render_template("home.html",msg=msg)


@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        return redirect("/stock")
    else:
        return render_template("home.html")

@app.route("/about/")
def About():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)

