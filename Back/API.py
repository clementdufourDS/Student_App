# Importation des bibliothèques nécessaires
import pandas as pd
from flask import Flask, jsonify, request


# Initialisation de l'application Flask
app = Flask(__name__)

# Charger les données à partir du fichier CSV 'student_data.csv'
data = pd.read_csv('student_data_with_score.csv')

# Route pour récupérer les données complètes au format JSON
@app.route('/')
def get_data():
    return jsonify(data.to_json(orient='split'))

# Route pour obtenir les noms complets des éléves
@app.route('/Name',methods = ['POST'])
def get_student_name():
    school = request.json['data']
    return jsonify(data[data['school'] == school]['FullName'].to_dict())

# Route pour récupérer uniquement les données correspondant à une Université
@app.route('/School',methods=['POST'])
def get_school():
    school = request.json['data']
    return jsonify(data[data['school'] == school].to_json(orient='split'))

# Démarrer l'application Flask si le script est exécuté directement
if __name__ == '__main__':
    app.run()
