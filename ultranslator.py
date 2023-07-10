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

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]


text = st.text_area("enter text to translate")
style = st.text_area("enter translation directions")
# style2 = st.text_area("enter another set of translation directions")

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

# formatted_text2 = prompt_template.format_messages(
#     style=style2,
#     text=text
# )

if "text" not in st.session_state:
    st.session_state.text = []
if "style" not in st.session_state:
    st.session_state.style = []
if "style2" not in st.session_state:
    st.session_state.style2 = []
if "responses" not in st.session_state:
    st.session_state.responses = []
# if "responses2" not in st.session_state:
#     st.session_state.responses2 = []

if text:
    if style:
        st.session_state.text.append(text)
        st.session_state.style.append(style)
        
        translated_response = chat(formatted_text)
        response = translated_response.content
        st.session_state.responses.append(response)
        # st.markdown(response, help="your translated text")
        
        # if style2:
        #     st.session_state.style2.append(style2)

        #     translated_response2 = chat(formatted_text2)
        #     response2 = translated_response2.content
        #     st.session_state.responses2.append(response2)
        #     st.markdown(response2, help="your translated text")
        
        
        
        with st.sidebar:
            st.subheader("History")
            for i in range(len(st.session_state.responses)):
                st.text(st.session_state.text[i])
                st.text(st.session_state.style[i])
                st.text(st.session_state.responses[i])
                # st.write(st.session_state.style2[i])
                # st.write(st.session_state.responses2[i])
                st.divider()