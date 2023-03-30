import streamlit as st
from code_snippets import Snippets

PAGE_TITLE = "</>Complete the Code</>"
PAGE_ICON = ":fire:"
layout = 'centered'
CORRECT_EMOJI = ':sunglasses:'
WRONG_EMOJI = ':joy:'

data = Snippets()
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=layout)
st.title("MUJ IEEE CS: BATTLESHIP :collision:")
st.title('Complete the code')

if 'code' not in st.session_state:
    data = Snippets()
    code, key = data.fetch_random_snippet()
    code = code.replace('[BLANK]', key)
    code = code.replace(key, "____", 1)
    st.session_state.code = code
    st.session_state.answer = key

st.code(st.session_state.code, language="c")

user_text_input = st.text_input(label="Enter Code for Blank", key="#t1")
submit_button = st.button("Submit")

if submit_button:
    if user_text_input != st.session_state.answer:
        st.write(f"Wrong {WRONG_EMOJI}: " + str(user_text_input))
        st.write("Expected: " + st.session_state.answer)
        print("Helo")
    else:
        st.write(f"Correct {CORRECT_EMOJI}: " + str(user_text_input))
        print("Helo")

