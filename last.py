import streamlit as st
import random
from code_snippets import Snippets


data = Snippets()
code, key = data.fetch_random_snippet()
#-----------settings------------
PAGE_TITLE = "</>Complete the Code</>"
PAGE_ICON = ":fire:"
layout = 'centered'
CORRECT_EMOJI = ':sunglasses:'
WRONG_EMOJI = ':joy:'
#------------config-------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=layout)
st.title("MUJ IEEE CS: BATTLESHIP :collision:")
st.title("</> Complete_the_code </>")
#-------------------------------
#-------------------------------
code.replace(key, "____", 1) # only replacing first occurance
#-------------------------------
col1 = st.code(code, language='c')
user_text_input = st.text_input(label="Enter Code for Blank", key="#t1")
submit_button = st.button("Submit")
#-------------------------------
if submit_button:
    if user_text_input == key:
        st.write(f"Correct {CORRECT_EMOJI}: " + str(user_text_input))
        user_text_input = ""  # reset input
    else:
        st.write(f"Wrong {WRONG_EMOJI}: " + str(user_text_input))
        st.write(f"Expected: {key}")

restart_button = st.button("Restart")
if restart_button:
    code, key = data.fetch_random_snippet()
    code.replace(key, "____", 1)
    col1.code(code, language='c')
    user_text_input = ""  # reset input
