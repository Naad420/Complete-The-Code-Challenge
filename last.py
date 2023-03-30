import streamlit as st
from code_snippets import Snippets

PAGE_TITLE = "</>Complete the Code</>"
PAGE_ICON = ":fire:"
layout = 'centered'
CORRECT_EMOJI = ':sunglasses:'
WRONG_EMOJI = ':joy:'

data = Snippets()
code, key = data.fetch_random_snippet()
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=layout)

col1, col2 = st.columns([1, 4])
with col1:
    st.image("1623940696853.jpeg", width=80)
with col2:
    st.title("MUJ IEEE CS: BATTLESHIP :collision:")
st.title('</>Complete the code</>')

if 'code' not in st.session_state:
    code = code.replace('[BLANK]', key)
    code = code.replace(key, "____", 1)
    st.session_state.code = code
    st.session_state.answer = key


with st.form(key='my_form'):
    col3 = st.code(st.session_state.code, language="c")

    user_text_input = st.text_input(label="Enter Code for Blank", value=' ')
    submit_button = st.form_submit_button(label="Submit", disabled=False)

    if submit_button:
        if user_text_input != st.session_state.answer:
            st.write(f"Wrong {WRONG_EMOJI}: " + str(user_text_input))
            st.write("Expected: " + st.session_state.answer)
        else:
            st.write(f"Correct {CORRECT_EMOJI}: " + str(user_text_input))

col4, col5 = st.columns([1, 8])
with col4:
    st.markdown("<a href='https://www.instagram.com/ieee_csmuj/'>Instagram</a>",unsafe_allow_html=True)
with col5:
    st.markdown("<a href='https://www.linkedin.com/company/ieee-cs-muj/mycompany/'>LinkedIn</a>", unsafe_allow_html=True)


