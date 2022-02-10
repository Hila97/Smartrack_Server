from flask import Flask, render_template,request
from sqlalchemy import sql
app = Flask(__name__)
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sql(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        rating = request.form['rathing']
        print(customer,rating)
        return render_template('result.html')

if __name__ == '__main__':
    app.run()
