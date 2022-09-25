#app.py

from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', methods=['POST'])
def addTodo():
    text1 = request.form['text1']
    print(text1)
    return(text1)


if __name__ == "__main__":
    app.run(debug=True)




#All 4 of them pass information through query parameters and path parameters
# Query params. www.google.com?page=3&row=53782&user=joe
# Path parameters www.google.com/someRootURL/3//53782/joe

#POST AND PUT
#Info will be passed in the body -> www.google.com

#GET, PUT, POST, DELETE
#GET and DELETE


#CRUD CREATE, RETRIEVE, UPDATE, DELETE