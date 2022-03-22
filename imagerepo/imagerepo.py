from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)
DB_conf = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'imagerepo'
}

def styles():
    S  = "<style>\n"  
    S += " body {background-color: #88caf7;}"
    S += " table {border-collapse: collapse;}"
    S += " table, th, td {border: 2px solid black; background-color: white; padding: 15px;}"
    S += " a:link {color: rgb(255, 0, 0); text-decoration: none; border-bottom: 1px solid;}"
    S += " a:visited {color: rgb(255, 0, 255);}"
    S += " a:hover {color: rgb(0, 255, 0); border-bottom: none;}"
    S += " a:active {color: rgb(0, 255, 255);}"
    S += "</style>\n"
    return S

def test_table():
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM birds')
    results = [c for c in cursor]
    cursor.close()
    connection.close()
    return results

def add_item(species, location, genus, diet, imagelink):
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    request = f"INSERT INTO birds (species, location, genus, diet, imagelink) VALUES ('{species}', '{location}', '{genus}', '{diet}', '{imagelink}');"
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()
    return request

def delete_item(species):
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    request = f"DELETE FROM birds WHERE species = '{species}';"
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()
    return request

@app.route('/delete')
def delete():
    species = request.args.get("species", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "   <head>\n"
    S += "      <title>Deleted a bird</title>\n"
    S += styles()
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Deleted a bird</h1>\n"
    if species != "":
        S += delete_item(species)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/add')
def add():
    species = request.args.get("species", "", str)
    location = request.args.get("location", "", str)
    genus = request.args.get("genus", "", str)
    diet = request.args.get("diet", "", str)
    imagelink = request.args.get("imagelink", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "   <head>\n"
    S += "      <title>Added species, location, genus, diet and image</title>\n"
    S += styles()
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Added species, location, genus, diet and image</h1>\n"
    if species != "" and location != "" and genus != "" and diet != "" and imagelink != "":
        S += add_item(species, location, genus, diet, imagelink)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/upload')
def upload():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <a href='/'>Back!</a>\n"
    S += "   <head>\n"
    S += "      <title>Enter the species, location, genus, diet and image to be added!</title>\n"
    S += styles()
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Enter the species, location, genus, diet and image to be added!</h1>\n"
    S += "      <form action='/add'>\n"
    S += "        <label for='species'>Species:</label>\n"
    S += "        <input type='text' name='species' value=''/>\n"
    S += "        <label for='location'>Location:</label>\n"
    S += "        <input type='text' name='location' value=''/>\n"
    S += "        <label for='genus'>Genus:</label>\n"
    S += "        <input type='text' name='genus' value=''/>\n"
    S += "        <label for='diet'>Diet:</label>\n"
    S += "        <input type='text' name='diet' value=''/>\n"
    S += "        <label for='imagelink'>Image:</label>\n"
    S += "        <input type='file' name='imagelink' accept='image/png, image/jpeg, image/jpg'>\n"
    S += "        <input type='submit' value='Add'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/addform')
def addform():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <a href='/'>Back!</a>\n"
    S += "   <head>\n"
    S += "      <title>Enter the species, location, genus, diet and image to be added!</title>\n"
    S += styles()
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Enter the species, location, genus, diet and image to be added!</h1>\n"
    S += "      <form action='/add'>\n"
    S += "        <label for='species'>Species:</label>\n"
    S += "        <input type='text' name='species' value=''/>\n"
    S += "        <label for='location'>Location:</label>\n"
    S += "        <input type='text' name='location' value=''/>\n"
    S += "        <label for='genus'>Genus:</label>\n"
    S += "        <input type='text' name='genus' value=''/>\n"
    S += "        <label for='diet'>Diet:</label>\n"
    S += "        <input type='text' name='diet' value=''/>\n"
    S += "        <label for='imagelink'>Imagelink:</label>\n"
    S += "        <input type='text' name='imagelink' value=''>\n"
    S += "        <input type='submit' value='Add'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/deleteform')
def deleteform():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <a href='/'>Back!</a>\n"
    S += "   <head>\n"
    S += "      <title>Enter the bird to be deleted</title>\n"
    S += styles()
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Enter the bird to be deleted</h1>\n"
    S += "      <form action='/delete'>\n"
    S += "        <label for='species'>Species:</label>\n"
    S += "        <input type='text' name='species' value=''/>\n"
    S += "        <input type='submit' value='Delete'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/')
def index():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <a href='/addform'>Add!</a> <a href='/deleteform'>Delete!</a> <a href='/upload'>Upload!</a>\n"
    S += "   <head>\n"
    S += "      <title>Simple bird list</title>\n"
    S += styles()
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Birds</h1>\n"
    S += "      <table>\n"
    S += "          <form action='/delete'>\n"
    for (species, location, genus, diet, imagelink) in test_table():
      S += f"         <tr><td>{species}</td>\n"
      S += f"             <td>{location}</td>\n"
      S += f"             <td>{genus}</td>\n"
      S += f"             <td>{diet}</td>\n"
      S += f"             <td>{imagelink}</td>\n"
      S += f"             <td><input type='radio' value='{species}' name='species'/></td>\n"
      S += f"         </tr>"
    S += f"           <tr><td><input type='submit' name='action' value='Delete'></td>\n"
    S += f"           </tr>\n"
    S += f"         </form>"
    S += "      </table>\n"
    S += "      <h2>Add another bird!</h2>\n"
    S += "      <form action='/add'>\n"
    S += "        <label for='species'>Species:</label>\n"
    S += "        <input type='text' name='species' value=''/>\n"
    S += "        <label for='location'>Location:</label>\n"
    S += "        <input type='text' name='location' value=''/>\n"
    S += "        <label for='genus'>Genus:</label>\n"
    S += "        <input type='text' name='genus' value=''/>\n"
    S += "        <label for='diet'>Diet:</label>\n"
    S += "        <input type='text' name='diet' value=''/>\n"
    S += "        <label for='imagelink'>Imagelink:</label>\n"
    S += "        <input type='text' name='imagelink' value=''/>\n"
    S += "        <input type='submit' value='Add'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

if __name__ == '__main__':
    app.run(host='0.0.0.0')