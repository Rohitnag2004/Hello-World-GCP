from flask import Flask
app2 = Flask(__name__)
@app2.route('/')
def hello():
 return 'Hello World from GitHub!
