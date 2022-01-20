import streamlit as st
import pandas as pd

from deep_translator import GoogleTranslator

st.title("To English Translator v1.0")

uploaded_file = st.file_uploader("Choose a csv file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df = df[['item_name']]
  
  def change_to_english(item):
    translated = GoogleTranslator(source='auto', target='en').translate(item)
    return (translated)
  
  df.loc[:,'item_name_eng'] = df['item_name'].apply(change_to_english)
  
  st.write(df)

  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()



  st.markdown('### **⬇️ Download output CSV File **')
  href = f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'
  st.markdown(href, unsafe_allow_html=True)
  
