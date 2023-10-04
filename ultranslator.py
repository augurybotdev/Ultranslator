import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from st_custom_components import st_audiorec
import os
from speechrecognition import transcribe_audio

st.title("ULTRANSLATOR")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "saved_styles" not in st.session_state:
    st.session_state.saved_styles   = []
if "text" not in st.session_state:
    st.session_state.text           = []
if "style" not in st.session_state:
    st.session_state.style          = []
if "responses" not in st.session_state:
    st.session_state.responses      = []
if "recorded_audio" not in st.session_state:
    st.session_state.recorded_audio = False

def get_completion(prompt, model="gpt-4-0613"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]

# st.markdown("#### Text to Translate")

# audio_in = st.checkbox('transcribe audio', key='audio_in' )

# if audio_in:
    
#     wav_audio_data = st_audiorec()
    
#     if wav_audio_data is not None:
#         filename = "recorded_speech.wav"
        
#         if os.path.exists(filename):
#             os.remove(filename)
            
#         with open(filename, 'wb') as f:
#             f.write(wav_audio_data)
            
#         print(f"Filename: {filename}")  # Print the filename
#         print(f"File exists: {os.path.exists(filename)}")  # Check if the file exists
        
#         text = transcribe_audio(filename)
        
#         st.session_state.text.append(text)
#         st.session_state.recorded_audio = True

# if st.session_state.recorded_audio == True:
#     value = st.session_state.text[0]
# else:
#     value =''
            
# text = st.text_area("enter text to translate", value=value, label_visibility="collapsed")

text = st.text_area("enter text to translate", label_visibility="collapsed")

# Display styles in a dropdown
with st.sidebar:
    st.markdown("### Saved Styles")
    selected_style = st.selectbox("your styles", [''] + st.session_state.saved_styles)
    
st.markdown("#### Language or Style Directions")
style = st.text_area("enter language or character or style to translate to", value=selected_style, label_visibility="collapsed")

if style and style not in st.session_state.saved_styles:
    st.session_state.saved_styles.append(style)
    
col1, col2, col3 = st.columns([3,3,1])

with col3:
    translate_button = st.button("Translate")
    
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

if translate_button:
    if text:
        if style:     
            st.session_state.text.append(text)
            st.session_state.style.append(style)

            translated_response = chat(formatted_text)
            response            = translated_response.content
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
        else:
            st.info("please select or enter a directive to translate to")
    else:
        st.info("please enter text to be translated") 
