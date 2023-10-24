import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from streamlit_extras.stylable_container import stylable_container 
import os
import time

st.markdown("# :violet[ULTRANSLATOR]")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "saved_styles" not in st.session_state:
    st.session_state.saved_styles = []
if "text" not in st.session_state:
    st.session_state.text = ""
if "style" not in st.session_state:
    st.session_state.style = ""
if "responses" not in st.session_state:
    st.session_state.responses = []
    
def special_button(button_text):
    with stylable_container(key="translate_button", 
                            css_styles="""
                                button { 
                                    background-color: #2986cc; 
                                    color: white; 
                                    border-radius: 10px;
                                    }
                                font-weight: bold;"""):
        st.button(button_text, key = "a_button")
    
def container_with_border(current_response):
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 3px solid rgba(149, 151, 163, 0.2);
                border-radius: 0.5rem;
                background-color: rgba(245, 245, 245, 0.7);
            }
            p {   
                padding-top: 0em;
                padding-bottom: 1em;
                padding-left: 1.5em;
                padding-right: 1.5em;
                word-wrap: break-word;
                word-break: break-all;
                white-space: pre-line:
                overflow-wrap: break-word;
            }
            """,
    ):
        st.markdown(current_response)


def get_completion(prompt, model="gpt-4"):
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

about_sample="""\
    To capture the essence of ULTRANSLATOR, think of it as your ultimate communication tool. 
    It translates not just words, but also tone and style, bridging gaps across time, space, and culture. 
    Ever felt misunderstood or had your humor fall flat? This app ensures your message hits the mark, gaining you respect and understanding wherever you go. 
    It's not just about what you say, but how you say it. 
    Give it a try and see how it transforms your conversations into something golden."""

about_extended_with_alliteration="""\
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
        """


with st.expander("Documentation"):
    
    title_with_header = st.markdown("""\
        ### **About** Ultranslator:\
        """)
        
    about_text = st.markdown(f"{about_sample}")
    
    how_to_use_text = st.markdown("""
                
        ---

        ### How to Use:

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
        "
    """)


# Display styles in a dropdown
with st.sidebar:
    st.markdown("### Session History")
    style_selection_placeholder = st.empty()

example_options = st.container()

    
example_button = st.button('Place Example')
example_style = st.session_state.style

with example_options:
    toggle = st.toggle("use preset ideas", help="""\
                       1. toggle the switch to use preset examples. 
                       
                       2. Select a quote along with a pre-set style, 
                       
                       3. click the 'Place Example' button to confirm choices. 
                       
                       4. Click 'Translate' to receive translation.\
                       """)
    
    if toggle:
        example_options.expander("example ideas")
        text_input_examples = [fiction, history, roosevelt, breakfast, madison]
        style_examples = ["French", "Cockney", "Yoda", "Mario from Super Mario Bros", "Cajun", "Italian", "Bostonian", "Baby Talk", "Hawaiian Pidgin", "90's 'Fly' sounding White Boy", "Overly Apologetic", "Pauley Shore from Encinoman", "Obama", "Alliterative Mandarin Poetry",  "15th Century English Nobleman", "Pig Latin", "East Harlem native, 1985", "Southern Baptist Preacher", "Pirate"]
        selected_text = st.selectbox("text examples", text_input_examples)
        selected_style = st.selectbox("style examples", style_examples)
        example_text = selected_text
        example_style = selected_style


if example_button:
    st.session_state.text = example_text
    st.session_state.style = example_style

text = st.text_area("enter the text that you'd like the ai to translate in the space below", value=st.session_state.text, label_visibility="hidden", placeholder="enter some text")
style = st.text_area("Here you can specify what you'd like to translate your text to such as another language, or a unique dialect, vernacular, accent or slang.", value=st.session_state.style, label_visibility="hidden", placeholder="enter a language accent character or something else here")

    
col1, col2, col3 = st.columns([3,3,1])

with col1:
    st.divider()
    
    # translate_button = special_button("TRANSLATE")
    translate_button  = st.button('Translate')
    
st.divider()

template_string = """\
To capture the essence of a character or style in your translation, immerse yourself in their specific language, culture, and mannerisms. 
Consider the time period and technology available to them, as well as their unique way of speaking. 
For someone like Donald Trump, remember that he rarely admits fault and often distorts facts. Make sure your translation aligns with his typical way of communicating. 
Also, try to incorporate regional dialects and slang to make the translation culturally nuanced and authentic.

Here are some examples for inspiration:

Original: "Did I like the food? I sure did!"
New Yorker: "Facts, the food was lit fam."

Original: "My car's GPS took me the wrong way!"
15th Century Nobleman: "Mine carriage's compass led me astray!"

Original: "We'll need more chips for the party tonight."
Beldar Conehead: "We require additional fried consumables for this evening's communal gathering."

Original: "This building is very large and seems to be built out of a lot of cement and steel."
Trump: "This building, it's truly tremendous isn't it folks? The fake news media won't show you how amazing, just incredible this building truly is but those who are here will tell you, it's much more incredible than it seems on tv. One of the best in the world, maybe of all time, best buildings ever made. A lot of people, very smart people say so, and tell me all the time, they say, "Sir, How did you make this building so incredible? It's the most amazing and incredible building I've ever seen!"

Here is the original text you need to translate:
```{text}```

And here is the style or character you need to translate it to:
```{style}```
"""

# Original: "This car is quite old and might break down, but it's still reliable most of the time."
# Australian (Queensland):"Oi, this ute's a bit of a clunker and might chuck a wobbly, but she's right as rain most days, mate!"

# Original: "Wind energy can be harvested with turbines that spin from the force of wind."
# Trump: "Wind energy is terrible, it's completely unreliable, I mean what happens if the wind stops blowing, what happens when we have a windless day, you ever hear of that, no wind, a day with no wind. I don't want that I want wind, I like wind, but if there's no wind then what, what happens then, it's terrible. You need oil for that, you know that right? You can't just make wind. Wind doesn't just come out of nowhere, it needs oil to make it. It's true. And the birds, all the dead birds they're dying by the millions from these things, gives them cancer. It's true, terrible, so sad all the dead birds and cancer from these things... that's what they are all saying, believe me."

# Original: "I lied. I'm sorry."
# Trump: "They lied. They're very, very bad people. They hate you and they want to destroy this beautiful country. It's awful and it's very sad. Some people don't know, they don't know that they are lying about me. But that's what they do in the swamp, it's all fake, that's why I call them the 'Fake' 'News' 'Media' because that's what they are folks. 'F A K E'. They lie and they lie and they try to blame it all on me. And it's very sad, because some people, some people used to be smart but now they don't know about the lies and it's tearing us apart, because they hate us because we love America. They say it's my fault and I'm sorry they lied about me to you. They're liars, they can't even help themselves anymore I guess. And so, I'm sorry, but I'm not sorry. They're sorry. I'm not sorry."



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
        
        st.markdown(" :violet[your translation:]")
        
        container_with_border(current_response)
                
        history = st.sidebar.expander("text translations")
        with history:
            for i in range(len(st.session_state.responses)):
                response_text = st.session_state.responses[i].replace('```', '')
                st.write(response_text)
style_selection_placeholder.selectbox("previously entered styles", ['styles used'] + st.session_state.saved_styles)