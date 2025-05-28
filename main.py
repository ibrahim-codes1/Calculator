
# from flask import Flask,jsonify,render_template
# app = Flask(__name__)


# @app.route('/',methods=["GET"])
# def indexwelcome():
#     return render_template("./app.html")

# @app.route('/',methods=["POST"])
# def my_data():
#     request.form.get()

# @app.route('/name',methods=['GET'])
# def indexname():
#     return 'Ibrahim'

# @app.route('/name/age',methods=['GET'])
# def indexage():
#     return '25'

# @app.route('/name/occupation',methods=['GET'])
# def indexoccupation():
#     return 'software'

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/history')
@app.route('/', methods=["GET", "POST"])
def indexwelcome():
    result = ""
    c = ""
    if request.method == "POST":
        c=request.form.get("boxname")

        if c and isinstance(c,str):
            parts = c.split()

            if len(parts) == 3:
                value1,op,value2 = parts 

                if value1.isdigit() and value2.isdigit():
                    a = int(value1)
                    b = int(value2)

                    if op == '+':
                        result = a + b
                    elif op == '-':
                        result = a - b
                    elif op == '*':
                        result = a * b
        else:
            result="Error!"
            with open("history.txt", "a") as f:
                f.write(result)

    return render_template("app.html", result=result)
if __name__ == '__main__':
    app.run(debug=True)

