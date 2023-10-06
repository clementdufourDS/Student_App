# Tableau de bord d'aide à la priorisation des élèves

Ce projet vise à aider les conseillers pédagogiques des établissements scolaires à prioriser les élèves qui ont le plus besoin d'un soutien personnalisé pour améliorer leur niveau scolaire. L'outil se base sur un score calculé en fonction de la complexité de l'accompagnement nécessaire et de la valeur potentielle de cet accompagnement.

### Score

    Pour créer un score pertinent destiné à aider les conseillers pédagogiques, j'ai suivi une démarche méthodique. J'ai commencé par identifier des indicateurs pertinents, qui serviraient de base pour évaluer la nécessité d'un soutien personnalisé aux élèves. Il serait judicieux de discuter de ces indicateurs avec les conseillers pédagogiques pour éventuellement les ajuster en fonction de leur expertise et de leurs besoins. Les indicateurs que j'ai sélectionnés comprennent :

    - La consommation d'alcool les jours travaillés.
    - La consommation d'alcool le week-end.
    - Le nombre de sorties entre amis.
    - Le temps consacré aux études.
    - Le nombre d'absences en classe.

    Chacun de ces indicateurs a été soigneusement standardisé, ce qui signifie que je les ai mis à l'échelle de manière à ce qu'ils aient une signification uniforme dans le calcul du score. En outre, j'ai pris en compte l'impact positif ou négatif de chaque indicateur et les ai ajoutés ou soustraits en conséquence. Par exemple, le temps consacré aux études a été soustrait, car davantage de temps d'étude est généralement associé à de meilleures performances scolaires.

    Ensuite, pour garantir que les scores sont comparables et compris dans une plage de 0 à 1, j'ai appliqué une fonction de mise à l'échelle appelée "Min-Max" aux scores pour chaque école.

    Cette approche a permis de créer des scores qui tiennent compte de divers facteurs pertinents et qui peuvent être utilisés par les conseillers pédagogiques pour prioriser les élèves en fonction de leurs besoins en matière de soutien scolaire.

### Fonctionnalités principales

    - Visualisation sous forme de scatterplot des scores des élèves en fonction de leurs notes actuelles.
    - Priorisation des élèves en fonction de leur score.
    - Informations détaillées sur chaque élève.
    - Visualisation de données supplémentaires, y compris des indicateurs actionnables tels que l'absentéisme, la consommation d'alcool, etc.

### Technologies utilisées

    - Python
    - Streamlit
    - Flask
    - sickit-learn
    - Pandas
    - matplotlib, seaborn, plotly

### Installation

    Clonez ce dépôt sur votre machine locale :

    git clone https://github.com/clementdufourDS/Student_App.git

### Installez les dépendances Python requises :

    pip install -r requirements.txt


### Utilisation

    Exécutez l'API en utilisant la commande suivante :
       
        flask run

    Exécutez l'application Streamlit en utilisant la commande suivante :

        streamlit run app.py

    Ouvrez votre navigateur web et accédez à l'URL indiquée par Streamlit.

    Explorez le tableau de bord pour visualiser les scores des élèves, prioriser les élèves à accompagner et obtenir des informations détaillées sur chaque élève.

### Tests unitaires

    Nous avons inclus des tests unitaires pour vérifier le bon fonctionnement de l'API. Vous pouvez exécuter ces tests en utilisant pytest :

    pytest tests.py

### Déploiement

    L'application peut être déployée sur les serveurs de l'établissement en suivant les procédures standards de déploiement pour les applications Python.
