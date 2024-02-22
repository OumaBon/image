from flask import Flask


app =Flask(__name__)


@app.route("/",methods=["GET"])
def root ():
    return "<h1>Welcome to Our Page<\h1>"



if __name__=="__main__":
    app.run(debug=True)