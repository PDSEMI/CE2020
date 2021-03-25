from flask import Flask, redirect, url_for, request, render_template
import webview
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()

