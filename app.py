from flask import Flask 
app = Flask(__name__)
@app.route("/")#it means home page
def hellow_word():
    return "hellow world "

if __name__ ==  "__main__":
    app.run()
    
