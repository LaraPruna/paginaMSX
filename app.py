from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)

@app.route('/')
def base():
	return render_template("inicio.html")



port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)