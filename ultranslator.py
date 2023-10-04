import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

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

if "text" not in st.session_state:
    st.session_state.text = ""
movie_scene = """
    Vincent: You know what they call a Quarter Pounder with Cheese in Paris?
    Jules: They don’t call it a Quarter Pounder with Cheese?
    Vincent: No, they got the metric system there, they wouldn’t know what the heck a Quarter Pounder is.
    Jules: What do they call it?
    Vincent: They call it a “Royale with Cheese."""

with st.expander("Instructions"):
    st.markdown(
        """
        Title: Instructional Guide and About Message for ULTRANSLATOR

        ---

        ## About ULTRANSLATOR:

        ULTRANSLATOR is a fun tool designed to translate text input into a specified language, style, or character directive. Utilizing the prowess of OpenAI's GPT-4, it smartly adapts the text to mirror the nuances of the chosen directive. Whether it's translating modern text into Shakespearean prose or a casual chat into formal language, ULTRANSLATOR stands ready to assist.

        ---

        ## How to Use:

        1. **Enter Text:**
            - Locate the text input box titled "enter text to translate".
            - You can type in or paste the text you wish to translate here.

        2. **Specify Directive:**
            - In the sidebar, you'll find a section titled "Saved Styles" where you can select a previously used style or enter a new one in the text area below titled "enter language or character or style to translate to".

        3. **Translation:**
            - Click on the "Translate" button.
            - The translated text will appear below, formatted according to the specified directive. You can view the original text, directive, and the translated text all in one place for easy comparison.

        4. **Save Styles (Optional):**
            - If you find a particular style useful, the application will save it for easier selection in future sessions.
        """
    )


# Display styles in a dropdown
with st.sidebar:
    st.markdown("### Saved Styles")
    selected_style = st.selectbox("your styles", [''] + st.session_state.saved_styles)

example_button = st.button('Show Example')
if example_button:
    st.session_state.text = movie_scene
    selected_style = "Overly excited 15th century English Peasant"

text = st.text_area("enter text to translate", value = st.session_state.text, label_visibility="collapsed")
    
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
