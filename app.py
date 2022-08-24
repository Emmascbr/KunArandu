from flask import Flask, render_template, request
import pyrebase
from flask_sqlalchemy import SQLAlchemy
from firebase_admin import firestore, auth
firebaseConfig = {
  "apiKey": "AIzaSyBU3KdmlMusWkFeBIvT5FMncBmIDu0LP7U",
  "authDomain": "auth-anonimo.firebaseapp.com",
  "projectId": "auth-anonimo",
  "storageBucket": "auth-anonimo.appspot.com",
  "messagingSenderId": "881555772121",
  "appId": "1:881555772121:web:2967c5e95110794f0564c8",
  "databaseURL":"https://console.firebase.google.com/project/auth-anonimo/authentication/users?hl=es-419",
  "measurementId": "G-30JX2XK5SK"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = auth.sign_in_anonymous()
app = Flask(__name__)

db = firebase.database()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sign_in_as_guest")
def guest_user():
    return render_template("bienvenida.html")

@app.route("/arte") 
def artesania(): 
    return render_template("artesania.html")  

@app.route("/cocina") 
def cocina(): 
    return render_template("cocina.html")  


@app.route("/pelo") 
def peluqueria(): 
    return render_template("peluqueria.html")