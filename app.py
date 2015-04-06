# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, render_template, jsonify

# create Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_all_pubs", methods=["GET"])
def get_all_pubs():
    #TODO
    return "Not Yet"

@app.route("/get_pubs/<int:pubs_id>", methods=["GET"])
def get_pubs(pubs_id):
    data = {
        "name" : "Super Bar 1",
        "location" : "1 rue toto, 1000 Troyes",
        "tel" : "0102030405",
        "website" : "http://superbar1.fr",
        "img" : "BLOB()"
    }
    return jsonify(data)


@app.route("/get_all_prices", methods=["GET"])
def get_all_prices():
    #TODO:
    #Use DB
    data = {
        "data" : [
            {"date_maj": "14/03/2015", "prix": "2€", "_id": 1, "biere_nom": "Biere 5", "bar_nom": "Bar 8", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "12/03/2015", "prix": "5€", "_id": 2, "biere_nom": "Biere 8", "bar_nom": "Bar 2", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "10/03/2015", "prix": "5€", "_id": 3, "biere_nom": "Biere 0", "bar_nom": "Bar 5", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "07/03/2015", "prix": "3€", "_id": 4, "biere_nom": "Biere 0", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "18/02/2015", "prix": "2€", "_id": 5, "biere_nom": "Biere 4", "bar_nom": "Bar 0", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "22/02/2015", "prix": "3€", "_id": 6, "biere_nom": "Biere 8", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "26/02/2015", "prix": "2€", "_id": 7, "biere_nom": "Biere 3", "bar_nom": "Bar 1", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "26/02/2015", "prix": "5€", "_id": 8, "biere_nom": "Biere 8", "bar_nom": "Bar 7", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "26/02/2015", "prix": "1€", "_id": 9, "biere_nom": "Biere 0", "bar_nom": "Bar 4", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "19/02/2015", "prix": "3€", "_id": 10, "biere_nom": "Biere 4", "bar_nom": "Bar 2", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "18/02/2015", "prix": "1€", "_id": 11, "biere_nom": "Biere 10", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "15/02/2015", "prix": "2€", "_id": 12, "biere_nom": "Biere 8", "bar_nom": "Bar 10", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "15/02/2015", "prix": "3€", "_id": 13, "biere_nom": "Biere 5", "bar_nom": "Bar 4", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "30/01/2015", "prix": "1€", "_id": 14, "biere_nom": "Biere 6", "bar_nom": "Bar 4", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "30/01/2015", "prix": "3€", "_id": 15, "biere_nom": "Biere 3", "bar_nom": "Bar 6", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "30/01/2015", "prix": "2€", "_id": 16, "biere_nom": "Biere 4", "bar_nom": "Bar 4", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "30/01/2015", "prix": "1€", "_id": 17, "biere_nom": "Biere 1", "bar_nom": "Bar 2", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "29/01/2015", "prix": "5€", "_id": 18, "biere_nom": "Biere 7", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "29/01/2015", "prix": "2€", "_id": 19, "biere_nom": "Biere 1", "bar_nom": "Bar 6", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "29/01/2015", "prix": "3€", "_id": 20, "biere_nom": "Biere 3", "bar_nom": "Bar 1", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "12/01/2015", "prix": "2€", "_id": 21, "biere_nom": "Biere 5", "bar_nom": "Bar 0", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "12/01/2015", "prix": "3€", "_id": 22, "biere_nom": "Biere 1", "bar_nom": "Bar 7", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "12/01/2015", "prix": "5€", "_id": 23, "biere_nom": "Biere 5", "bar_nom": "Bar 4", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "12/01/2015", "prix": "4€", "_id": 24, "biere_nom": "Biere 0", "bar_nom": "Bar 2", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "20/12/2014", "prix": "1€", "_id": 25, "biere_nom": "Biere 8", "bar_nom": "Bar 7", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "20/12/2014", "prix": "1€", "_id": 26, "biere_nom": "Biere 10", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "20/12/2014", "prix": "3€", "_id": 27, "biere_nom": "Biere 8", "bar_nom": "Bar 8", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "20/12/2014", "prix": "1€", "_id": 28, "biere_nom": "Biere 8", "bar_nom": "Bar 2", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "20/12/2014", "prix": "4€", "_id": 29, "biere_nom": "Biere 4", "bar_nom": "Bar 10", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "20/12/2014", "prix": "4€", "_id": 30, "biere_nom": "Biere 7", "bar_nom": "Bar 1", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "18/12/2014", "prix": "2€", "_id": 31, "biere_nom": "Biere 8", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "18/12/2014", "prix": "3€", "_id": 32, "biere_nom": "Biere 1", "bar_nom": "Bar 9", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "14/12/2014", "prix": "5€", "_id": 33, "biere_nom": "Biere 1", "bar_nom": "Bar 1", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "14/12/2014", "prix": "5€", "_id": 34, "biere_nom": "Biere 6", "bar_nom": "Bar 8", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "14/12/2014", "prix": "1€", "_id": 35, "biere_nom": "Biere 9", "bar_nom": "Bar 0", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "13/12/2014", "prix": "1€", "_id": 36, "biere_nom": "Biere 10", "bar_nom": "Bar 3", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "12/12/2014", "prix": "3€", "_id": 37, "biere_nom": "Biere 9", "bar_nom": "Bar 8", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "11/12/2014", "prix": "2€", "_id": 38, "biere_nom": "Biere 10", "bar_nom": "Bar 6", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "11/12/2014", "prix": "3€", "_id": 39, "biere_nom": "Biere 2", "bar_nom": "Bar 1", "_id_biere" : 1, "_id_bar" : 1 }, 
            {"date_maj": "09/12/2014", "prix": "1€", "_id": 40, "biere_nom": "Biere 9", "bar_nom": "Bar 8", "_id_biere" : 1, "_id_bar" : 1 }
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.debug = True
    app.run()