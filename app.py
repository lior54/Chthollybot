from flask import Flask
import main

app = Flask(main.main())
app.run('0.0.0.0')