from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, my student number is l00179000 this is my DevOps Project app!' 

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('hello.html', name=name)
    return render_template('hello_form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
