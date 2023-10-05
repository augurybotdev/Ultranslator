import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
import time

st.title("ULTRANSLATOR")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "saved_styles" not in st.session_state:
    st.session_state.saved_styles = []
if "text" not in st.session_state:
    st.session_state.text = ""
if "style" not in st.session_state:
    st.session_state.style = ""
if "responses" not in st.session_state:
    st.session_state.responses = []

def get_completion(prompt, model="gpt-4-0613"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

fiction = """Vincent: You know what they call a Quarter Pounder with Cheese in Paris?
Jules: They don’t call it a Quarter Pounder with Cheese?
Vincent: No, they got the metric system there, they wouldn’t know what the heck a Quarter Pounder is.
Jules: What do they call it?
Vincent: They call it a “Royale with Cheese."""

history = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure"""

roosevelt = """It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming.."""""

breakfast = """Grid-like breakfast slabs... seared strips of swine flesh and flattened chicken embryos. I will enjoy it."""

madison = """Mr.Madison, what you’ve just said is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points, and may God have mercy on your soul."""


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
    style_selection_placeholder = st.empty()

example_options = st.container()

    
example_button = st.button('Place Example')
example_style = st.session_state.style

with example_options:
    toggle = st.toggle("use preset ideas")
    
    if toggle:
        example_options.expander("example ideas")
        text_input_examples = [fiction, history, roosevelt, breakfast, madison]
        style_examples = ["Yoda", "French", "Cockney", "Cajun", "1920's Gangster", "Beldar Conehead", "Liam Neeson", "Groovy Cat, 1970, Hip To It", "Overly Apologetic, Stammering and Polite", "Baby Talk", "Stoney from Encinoman", "Exaggerate Everything", "alliteration-sounding Mandarin-poem",  "15th Century English Nobleman", "90's rapper", "Pig Latin"]
        selected_text = st.selectbox("text examples", text_input_examples)
        selected_style = st.selectbox("style examples", style_examples)
        example_text = selected_text
        example_style = selected_style


if example_button:
    st.session_state.text = example_text
    st.session_state.style = example_style

text = st.text_area("enter text to translate", value=st.session_state.text, label_visibility="collapsed")
style = st.text_area("enter language or character or style to translate to", value=st.session_state.style, label_visibility="collapsed")

st.markdown("#### Language or Style Directions")
    
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
    
Remember to stay in character! Don't start applying old english accents if it isn't appropriate for the given style.
 
text: ```{text}```
"""

chat = ChatOpenAI(temperature=0.0)
prompt_template = ChatPromptTemplate.from_template(template_string)

if translate_button:
    with st.spinner('Translating...'):
        if style and style not in st.session_state.saved_styles:
            st.session_state.saved_styles.append(style)
        formatted_text = prompt_template.format_messages(style=style,text=text)
        translated_response = chat(formatted_text)
        response = translated_response.content
        st.session_state.responses.append(response)
        current_response = response.replace('```', '')
        st.write(current_response)
                
        history = st.expander("response history")
        with history:
            for i in range(len(st.session_state.responses)):
                response_text = st.session_state.responses[i].replace('```', '')
                st.write(response_text)
style_selection_placeholder.selectbox("your styles", [''] + st.session_state.saved_styles)