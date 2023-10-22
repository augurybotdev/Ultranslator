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
Jules: They don't call it a Quarter Pounder with Cheese?
Vincent: No, they got the metric system there, they wouldn't know what the heck a Quarter Pounder is.
Jules: What do they call it?
Vincent: They call it a “Royale with Cheese."""

history = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure"""

roosevelt = """It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming.."""""

breakfast = """Grid-like breakfast slabs... seared strips of swine flesh and flattened chicken embryos. I will enjoy it."""

madison = """Mr.Madison, what you've just said is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points, and may God have mercy on your soul."""


with st.expander("Instructions"):
    st.markdown(
        """
        Title: Instructional Guide and About Message for ULTRANSLATOR

        ---

        ## About ULTRANSLATOR:

        I've crafted an app, a tool to relate,
        That translates any tone, from any style to any given trait.
        You can reach across eras, lands, cultures and countries and states
        Even across realities piercing both time dimensions and space
        To communicate with any person, that's ever been or would be a person belonged to the human race

        Have you ever felt lost, misunderstood, with your words falling flat on your face?
        Or even worse, your tongue and cheek chats, perceived in bad taste?
        My app's your savior then friend , it clarifies your true phrase,
        Ensuring your wit, and rightful respect in places completely foreign, you'll soon be embraced
        As your gab and your chatter are heeded as candor and grace

        So when humor fades and expressions go cold,
        This tool finds the words, turns your stories to gold.
        It's not just the content, but the tone that's key,
        With this app, you'll connect, just try it you'll see.

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
        style_examples = ["Yoda", "French", "Cockney", "Cajun", "Italian", "Baby Talk", "Beldar Conehead", "Hawaiian Pidgin", "90's 'Fly' sounding White Boy", "Overly Apologetic", "Pauley Shore from Encinoman", "Obama", "Alliterative Mandarin Poetry",  "15th Century English Nobleman", "Pig Latin"]
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

template_string = """\
**TASK**

1. Translate the original text so that is matches the, language, cultural slang, accent lingo, jargon, lexicon, vernacular, dialect, tone, vibe and lexicon of the given style and or character.
Take creative liberty to re-interpret and re-phrase the provided text so that it most convincingly fits within all aspects.
When translating, place yourself in both time and space as well as character and mood to capture realistically how the given text could be expressed as faithfully as possible.
For example, if a character is from another time, prior to when certain technologies did not yet exist, take this into account. 
Or if a character is from a known fictional universe, or has a particular accent or pattern in their speech, take this into account as well.
Lastly, attempt to communicate regional dialects, slangs, vernaculars and turns of phrase to communicate across regions, cultures and ideas.

Here are some *examples* of some original texts and their translations:

[BEGIN EXAMPLES]

Original: "She's very smart and does well in school."
British (Cockney): "She's proper clever, does top in school."

Original: "Did I like the food? I sure did!"
New Yorker: "Facts, the food was lit fam."

Original: "My car's GPS took me the wrong way!"
15th Century Nobleman: "Mine carriage's compass led me astray!"

Original: "I'm heading to the beach this afternoon. Want to join me? It's a beautiful day!"
Hawaiian Pidgin:
"Eh, I going beach side dis aftahnoon, brah. You like come? Da day stay lookin' cherry!"

Original: "We'll need more chips for the party tonight."
Beldar Conehead: "We require additional fried consumables for this evening's communal gathering."

Original: "You did a great job."
Yoda: "A great job, you did."

Original: "This is a really impressive building."
Trump-esque: "This building, it's truly tremendous. Everyone knows it's probably the best in maybe the whole world. Everyone says so."

Original: "Education is the key to a better future."
Obama-esque: "If you look at the arc of history, education stands out as the gateway to a brighter tomorrow."

Original: "This car is quite old and might break down, but it's still reliable most of the time."
Australian (Extreme):
"Oi, this ute's a bit of a clunker and might chuck a wobbly, but she's right as rain most days, mate!"

Original: "Hey man! We should chill at my place! My mom's gonna be gone all weekend!"
90's White Boy Gangsta: "Yo peep this dawg! Le casa is officially O.P.P. vacant! ya feel me? Word to my mother! know what I'm saying boyyyy??"

Original: "Hello there! How have you been? We should get together for a coffee and chat soon."
Cajun:
"Hey cher! Comment ça va? We oughta meet up for some café au lait and pass a good time, yeah."

[END EXAMPLES]

!! IMPORTANT. DO NOT APPLY OLD ENGLISH STYLE INAPPROPRIATELY. for example: do NOT apply old english style to style of 'Beldar Conehead'! He doesn't speak in old english style. !!

Here is the original text you need to translate:
```{text}```

And here is the style or character you need to translate it to:

```{style}```
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