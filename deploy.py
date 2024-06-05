from flask import Flask, render_template, request
import pickle
model=pickle.load(open('saved_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    sl = request.form['sl']
    sw = request.form['sw']
    pl = request.form['pl']
    pw = request.form['pw']
    result=model.predict([[sl,sw,pl,pw]])
    return render_template('index.html', result = result)

if __name__ == '__main__':
   app.run(debug = True)
