import streamlit as st

import joblib

model_nb = joblib.load('Project')
vect = joblib.load('vect.pkl')

def main():
  st.title('Heart_Attack_Risk_Predictor ') #creates a title in web app
  ip = st.text_input('Enter INPUT:') #creates a text box in web app
  if st.button('Predict'):
    data=[ip]
    cv=vect.transform(data).toarray()
    prediction=model_nb.predict(cv)
    result=prediction[0]
    if result=='1':
      st.success("TRUE")
    else:
      st.error("FALSE")
   
main()  
