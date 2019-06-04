from flask import Flask
from flask import render_template
import requests



app = Flask(__name__)


@app.route('/')
def startpage():    
    return render_template('startpage.html', title='Startpage')


@app.route('/profile')
def auth():
    result = requests.get('https://testtaskdeliveryweb.appspot.com/')
    print(result.url)     
    return render_template('profile.html', title='Profile')


if __name__ == '__main__':
    app.run(debug=True)