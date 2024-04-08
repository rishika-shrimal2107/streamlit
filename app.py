from transformers import pipeline
import streamlit as st
from PIL import Image

#tab name and favicon
st.set_page_config(page_title='Pegasus Samsum',
                   page_icon='📖',
                   layout='centered')

#import pipeline
summarizer = pipeline("text2text-generation",
                      model="rishitau/pegasus-samsum-model")

#image=Image.open('image.png')
st.image('bot.gif', use_column_width=True)

st.write("""
# Pegasus Samsum 🎨 
Using Rishita's and Rishika's Transformers 🤗
""")

with st.form(key='my_form'):

  input = st.text_area('Enter your Text', height=300)

  summarize = st.form_submit_button('Summarize!')

if summarize:
  summary = summarizer(input, do_sample=False)
  st.subheader('Result 🎉')
  st.info(summary[0]['generated_text'])
  st.write('**Length:** ' + str(len(summary[0]['generated_text'].split(' '))) +
           ' words')
