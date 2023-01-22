from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "super secret key"

currentDirectory = os.getcwd()
# databasePath = os.path.join(currentDirectory, "database.db")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + databasePath
databasePathFile = os.path.join(currentDirectory, "db_path.txt")
databasePath = ""
with open(databasePathFile, 'r') as f:
    databasePath = f.readline().strip()
print(databasePath)
app.config['SQLALCHEMY_DATABASE_URI'] = databasePath
db = SQLAlchemy(app)
import routes, models

