import streamlit as st

import joblib

model_nb = joblib.load('Project')
vect = joblib.load('vector.pkl')

def main():
  st.title('Phishing URL Prediction') #creates a title in web app
  ip = st.text_input('Enter URL:') #creates a text box in web app
  if st.button('Predict'):
    data=[ip]
    cv=vect.transform(data).toarray()
    prediction=model_nb.predict(cv)
    result=prediction[0]
    if result=='Good':
      st.success("GOOD URL")
    else:
      st.error("Phishing URL")
   
main()  
