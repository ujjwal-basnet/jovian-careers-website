from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
    { 'id' : "1"  ,
     'title' : "Data Analytics"  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    }, 
    { 'id' : "2"  ,
     'title' : "Machiene Learning "  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    },
    { 'id' : "3"  ,
     'title' : "MERN "  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    },
    { 'id' : "4"  ,
     'title' : "Full stack "  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    },
    { 'id' : "5"  ,
     'title' : "Backend "  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    },
    { 'id' : "6"  ,
     'title' : "App developer "  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    },
    { 'id' : "7"  ,
     'title' : "Block Chain "  , 
     "location" : "kathmandu nepal " , 
     "salary" : "Rs 100000" 
     
    },
    ]




@app.route("/")
def hello_world():
    return render_template("home.html" , jobs  = JOBS )

if __name__ == '__main__':
    app.run(debug=True)
    

