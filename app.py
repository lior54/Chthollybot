from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return "F"

if __name__ == '__main__':
    os.system("python main.py &")