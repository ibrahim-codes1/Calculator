
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
@app.route('/', methods=["GET", "POST"])
def indexwelcome():
    a=request.form.get("boxname")
    print("the ",a)
    result=""
    return render_template("app.html", result=result)
if __name__ == '__main__':
    app.run(debug=True)

