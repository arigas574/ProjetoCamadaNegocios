from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

#Rotas
@app.route("/")
def homepage():
   return "Meu site no flask"

if __name__ == "__main__":
   app.run()