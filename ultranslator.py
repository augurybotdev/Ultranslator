import openai
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


st.title("ULTRANSLATOR")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_completion(prompt, model="gpt-4-0613"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]
text = st.text_area("enter text to translate")

if "saved_styles" not in st.session_state:
    st.session_state.saved_styles = []

# Display styles in a dropdown
selected_style = st.selectbox('Your saved languages and style directions', [''] + st.session_state.saved_styles)
style = st.text_area("enter translation directions", value=selected_style)

if style and style not in st.session_state.saved_styles:
    st.session_state.saved_styles.append(style)
    
st.divider()

template_string = """Translate the text \
that is delimited by triple backticks \
into a style or language that is {style}. \
When appropriate, alter the nouns and verbs to fit the context of the desired style \
For example, if the style is from 1600's and the text contains a reference to an automobile, \
translate that reference to "horse and carriage". \
text: ```{text}```
"""



chat = ChatOpenAI(temperature=0.0)
prompt_template = ChatPromptTemplate.from_template(template_string)

formatted_text = prompt_template.format_messages(
    style=style,
    text=text
)

if "text" not in st.session_state:
    st.session_state.text = []
if "style" not in st.session_state:
    st.session_state.style = []
if "responses" not in st.session_state:
    st.session_state.responses = []


if text:
    if style:     
        st.session_state.text.append(text)
        st.session_state.style.append(style)
        
        translated_response = chat(formatted_text)
        response = translated_response.content
        st.session_state.responses.append(response)

        for i in range(len(st.session_state.responses)):
            with st.expander(f'{st.session_state.style[i]}', expanded=False):
                st.text('FROM:')
                st.write(st.session_state.text[i])
                st.text('TO:')
                st.write(st.session_state.style[i])
                st.text('TRANSLATION:')
                response_text = st.session_state.responses[i].replace('```', '')
                st.write(response_text)  
