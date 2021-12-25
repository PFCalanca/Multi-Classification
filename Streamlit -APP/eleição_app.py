import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import model_from_json
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import utils as np_utils



m_dados = pd.read_csv("Eleicao.csv")
dataf=st.dataframe(m_dados)

#dataframe = pd.DataFrame(st.table(m_dados.head()))
def user_input_features(xCol):
    entrada=m_dados
    entrada.pop('Situacao') 
    colunas=entrada.columns
    df_entrada = pd.DataFrame(xCol, columns=colunas)
    data = {}
    for col in df_entrada.columns.to_list():
        df_entrada[col] = df_entrada[col].astype(float, errors = 'raise')
        data[col] = st.sidebar.slider(col,df_entrada[col].min(),df_entrada[col].max(),df_entrada[col].min())   
    
    return pd.DataFrame(data, index=[0])
@st.cache(allow_output_mutation=True)
#Renomeando as colunas para uma melhor estetica 
def load_data():
    m_dados = pd.read_csv('Eleicao.csv')
    
    #columns = {
       # 'age': 'idade',
       # 'hypertension': 'Hipertensão',
       # 'heart_disease': 'doenca_cardiaca',
       # 'avg_glucose_level': 'nível médio de glicose',
       # 'bmi': 'Massa Corporal',
       # 'stroke': 'AVC',
       # 'gender_Female': 'Mulher',
       # 'gender_Male': 'Homem',
       # 'smoking_status_Unknown':'Status Fumante: Desconhecido',
       # 'smoking_status_never smoked': 'Status Fumante: Nunca fumou',
       # 'smoking_status_smokes': 'Status Fumante: Fuma atualmente',
    #}
    #data = data.rename(columns=columns)
    dados_final = m_dados.values
    X = dados_final[:,0:161].astype('float32')
    Y=dados_final[:,161]
    encoder = LabelEncoder()
    encoder.fit(Y)
    encoded_Y = encoder.transform(Y)
    dummy_y = np_utils.to_categorical(encoded_Y)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_scale = min_max_scaler.fit_transform(X)
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, dummy_y, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    return (X_train, Y_train)

def modelo(X_train, Y_train):
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)

    model.load_weights("model.h5")
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def main():
    X_train, Y_train = load_data()

    st.write("""
    # Info dos Candidatos
    # """)
    st.write('---')

    model = modelo(X_train, Y_train)
    st.sidebar.header('Escolha de paramentros para Predição')

    User_r = user_input_features(X_train)
    pred=np.asarray(User_r)
    st.header('Parametros Selecionados')
    st.write(User_r)
    
    prediction = model.predict(pred)
    st.subheader(' Predição')
    st.write(prediction)
    st.write('---')
    #print(prediction[0,0:1]) # X= eleito
    #print(prediction[0,1:2]) # Y= Não eleito
    #print(prediction[0,2:])  # Z= Suplente
    if prediction[0,2:]> prediction[0,0:1] and prediction[0,2:]> prediction[0,1:2]:
        st.subheader(' Resultado')
        st.write("Não sera eleito mas tem chances de ser suplente")
        st.write('---')
    elif prediction[0,0:1] > prediction[0,2:]  and prediction[0,0:1] > prediction[0,1:2]:
        st.subheader(' Resultado')
        st.write("Candidato sera eleito")
        st.write('---')
    else :
        st.subheader(' Resultado')
        st.write("Provavelmente não sera eleito")
        st.write('---')
    


if __name__=='__main__':
    main()

