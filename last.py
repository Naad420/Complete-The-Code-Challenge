import streamlit as st
import random
from code_snippets import Snippets


code, key = Snippets()
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
    if user_text_input == user_text_input:
        st.write(f"Correct {CORRECT_EMOJI}: " + str(user_text_input))
    else:
        st.write(f"Wrong {WRONG_EMOJI}: " + str(user_text_input))
        st.write("Expected: ")
        col2 = st.code(code.replace("____", key), language='c')
