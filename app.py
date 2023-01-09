from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return "F"

if __name__ == '__main__':
    main.main()