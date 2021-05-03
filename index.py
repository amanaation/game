from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")


@app.route('/<code>')
def hello_world(code):

    return render_template("index.html")
    # return 'Hello, World! : '


@app.route('/mydata', methods=['GET', 'POST'])
def navigate():
    print(" -----  ", request.args.items())
    for r in request.args.items():
        print(" -----  ", r)
    return str(request.form.get("name"))
    # return "Redirecting...."


if __name__ == "__main__":
    app.run(debug=True)
