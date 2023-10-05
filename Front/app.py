import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import requests

# Chargement des données depuis l'API Flask locale
predict_url = 'http://127.0.0.1:5000'

# Fonction pour récupérer les données correspondant à l'école sélectionnée
def get_school_data(school):
    data = {'data': school}
    response = requests.post(predict_url + '/School', json=data)
    df = pd.read_json(response.json(), orient='split')
    return df   

# Fonction pour récupérer le nom des élèves pour l'école sélectionnée
def get_student_name(school):
    data = {'data': school}
    r  = requests.post(predict_url + '/Name',json=data)
    return r.json().values()

# Fonction pour afficher la visualisation de la corrélation entre l'Improvable score et la note finale
def display_IS_FG(df):
    fig = px.scatter(df, x="FinalGrade", y="ImprovableScore", hover_data='FullName',
                     title='Correlation between Improvable Score and Final Grade',
                     color='Priority', color_discrete_map={'Yes': 'red', 'No': 'blue'})
    fig.update_xaxes(autorange="reversed")
    return fig 

# Configuration de l'app Streamlit
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"]{
        min-width: 200px;
        max-width: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.write("")

with col2:
    st.image("ministerio-da-educacao.jpg")

with col3:
    st.write("")

# Sélection de l'école
selected_school = st.selectbox("Select your school", ["Gabriel Pereira", "Mousinho da Silveira"])

if selected_school == "Gabriel Pereira":
    school = 'GP'
    df = get_school_data(school).drop(columns='Unnamed: 0')
    st.plotly_chart(display_IS_FG(df), use_container_width=True)
elif selected_school == "Mousinho da Silveira":
    school = 'MS'
    df = get_school_data(school).drop(columns='Unnamed: 0')
    st.plotly_chart(display_IS_FG(df), use_container_width=True)

# Barre latérale pour les options
with st.sidebar:
    data = st.checkbox('Data')
    final_grade = st.checkbox('Final Grade')
    student = st.selectbox("Select a student", get_student_name(school))

# Affichage des données brutes
if data:
    st.write(df)

# Affichage de l'histogramme des notes finales
if final_grade:
    plot = sns.histplot(df['FinalGrade'], bins=20, kde=True)
    plt.xlabel('Final Grade')
    plt.ylabel('Count')
    plt.title('Distribution of Final Grades')
    st.pyplot(plot.get_figure())

# Affichage des données correspondant à l'étudiant séléctionné
st.write(df.loc[df['FullName'] == student])

# Sélection des caractéristiques pour l'affichage
features_list = ['studytime', 'goout', 'Dalc', 'Walc', 'absences']
selected_features = st.multiselect('Select features to visualize', features_list)

# Affichage des graphiques de distribution pour les caractéristiques sélectionnées
if selected_features:
    for feature in selected_features:
        fig, ax = plt.subplots()
        sns.histplot(data=df, x=feature, kde=True)
        st.pyplot(fig)

        stud = float(df.loc[df['FullName'] == student][feature])

        # Affichage du boxplot avec la valeur de l'étudiant marquée en rouge
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x=feature)
        sns.scatterplot(x=[student], y=[0], color='red', marker='X', s=100)
        st.pyplot(fig)

# Affichage du graphique bi-varié si deux caractéristiques sont sélectionnées
if len(selected_features) == 2:
    stud_value1 = float(df.loc[df['FullName'] == student][selected_features[0]])
    stud_value2 = float(df.loc[df['FullName'] == student][selected_features[1]])
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=selected_features[0], y=selected_features[1], s=10)
    sns.scatterplot(x=[stud_value1], y=[stud_value2], color='red', marker='X', s=100)
    st.pyplot(fig)