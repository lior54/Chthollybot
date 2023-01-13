from flask import Flask
from threading import Thread
import main

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return "F"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t= Thread(target=run)
    t.start()


if __name__=='__main__':
    main.main()
