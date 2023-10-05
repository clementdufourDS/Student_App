import pytest
import requests
import pandas as pd

@pytest.fixture
def api_url():
    return 'http://127.0.0.1:5000'

def test_prediction_accept(api_url):
    data = {'data': 'GP'}
    response = requests.post(api_url + '/School', json=data)
    
    # Assurez-vous que la requête a réussi avec un code 200
    assert response.status_code == 200
    
    # Convertissez la réponse JSON en DataFrame pandas
    df = pd.read_json(response.json(), orient='split')
    
    # Assurez-vous que la colonne 'school' contient la valeur 'MS'
    assert (df['school'] == 'GP').all()
    
    # Recherchez l'entrée avec 'FullName' égal à 'Rafael Morais'
    rafael_entry = df[df['FullName'] == 'Rafael Morais']
    
    # Assurez-vous que l'entrée a 'StudentID' égal à 0
    assert rafael_entry['StudentID'].values[0] == 0

