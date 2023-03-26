import streamlit as st
import random

#-------------data--------------
code_snippets = {
    "snippet1": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr;\n ptr = #\n\n printf('The value of num is: %d', *ptr);\n\n return 0;\n}",
        "answer": "*ptr"
    },
    "snippet2": {
        "code": "#include <stdio.h>\n\nint main() {\n int i = 0;\n while (i < 5) {\n printf(''%d '', i);\n i++;\n }\n\n return 0;\n}",
        "answer": "while"
    },
    "snippet3": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr = #\n\n printf('The address of num is: %p', ptr);\n\n return 0;\n}",
        "answer": "*ptr"
    },
    "snippet4": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int sum = 0;\n for (int i = 0; i < n; i++) {\n sum += arr[i];\n }\n printf('The sum of the array is: %d', sum);\n return 0;\n}",
        "answer": "sum"
    },
    "snippet5": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int *ptr = &num1;\n *ptr = 15;\n\n printf('The value of num1 is: %d', num1);\n\n return 0;\n}",
        "answer": "*ptr"
    },
    "snippet6": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int rev_arr;\n for (int i = 0; i < n; i++) {\n rev_arr[i] = arr[n - i - 1];\n }\n return 0;\n}",
        "answer": "rev_arr"
    },
    "snippet7": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr = #\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
        "answer": "*ptr"
    }
}
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
snippet = random.choice(list(code_snippets.values()))
code = snippet["code"]
key = snippet["answer"]
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
