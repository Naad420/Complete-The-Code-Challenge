import streamlit as st
from PIL import Image
import random

#-------------data--------------
code_snippets = {
    "snippet1": {
        "code": "#include <stdio.h>\n\nint main() {\n    int n;\n    printf(\"Enter the size of the matrix: \");\n    scanf(\"%d\", &[BLANK]);\n    int matrix[n][n];\n    printf(\"Enter the matrix elements:\\n\");\n    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < n; j++) {\n            scanf(\"%d\", &[BLANK]);\n            matrix[i][j] = [BLANK];\n        }\n    }\n    printf(\"The matrix is:\\n\");\n    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < n; j++) {\n            printf(\"%d \", matrix[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}",
        "answer": ["n", "num"]
    },
    "snippet2": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK];\n ptr = #\n\n printf('The value of num is: %d', *ptr);\n\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet3": {
        "code": "#include <stdio.h>\n\nint main() {\n int i = 0;\n [BLANK] (i < 5) {\n printf(''%d '', i);\n i++;\n }\n\n return 0;\n}",
        "answer": ["while"]
    },
    "snippet4": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK] = #\n\n printf('The address of num is: %p', ptr);\n\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet5": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int sum = 0;\n for (int i = 0; i < n; i++) {\n sum += arr[i];\n }\n printf('The sum of the array is: %d', sum);\n return 0;\n}",
        "answer": ["sum"]
    },
    "snippet6": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int [BLANK] = &num1;\n *ptr = 15;\n\n printf('The value of num1 is: %d', num1);\n\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet7": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int [BLANK];\n for (int i = 0; i < n; i++) {\n rev_arr[i] = arr[n - i - 1];\n }\n return 0;\n}",
        "answer": ["rev_arr"]
    },
    "snippet8": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr = #\n printf('The value of num is: %d', [BLANK]);\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet9": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int [BLANK];\n if (num1 > num2) {\n max = num1;\n } else {\n max = num2;\n }\n printf('The maximum number is: %d', max);\n return 0;\n}",
        "answer": ["max"]
    },
    "snippet10": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int [BLANK];\n for (int i = 0; i < n; i++) {\n new_arr[i] = arr[i] * 2;\n }\n return 0;\n}",
        "answer": ["new_arr"]
    },
    "snippet11": {
        "code": "#include <stdio.h>\n\nint main() {\n int i = 0;\n [BLANK] (i <= 10) {\n printf('%d ', i);\n i += 2;\n }\n\n return 0;\n}",
        "answer": ["while"]
    },
    "snippet12": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK] = #\n *ptr += 5;\n\n printf('The value of num is: %d', num);\n\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet13": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int max = arr[0];\n for (int i = 1; i < n; i++) {\n if (arr[i] > max) {\n max = arr[i];\n }\n }\n printf('The maximum element in the array is: %d', max);\n return 0;\n}",
        "answer": ["max"]
    },
    "snippet14": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK] = #\n *ptr -= 3;\n\n printf('The value of num is: %d', num);\n\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet15": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr = #\n printf('The address of num is: %p', [BLANK]);\n return 0;\n}",
        "answer": ["ptr"]
    },
    "snippet16": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int [BLANK];\n for (int i = 0; i < n; i++) {\n even_arr[i] = arr[i] % 2 == 0 ? arr[i] : 0;\n }\n return 0;\n}",
        "answer": ["even_arr"]
    },
    "snippet17": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 5;\n int [BLANK] = num;\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet18": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int sum = 0;\n for (int i = 0; i < n; i++) {\n sum += arr[i];\n }\n int [BLANK] = sum / n;\n printf('The average of the elements in the array is: %d', average);\n return 0;\n}",
    "answer": ["average"]
    },
    "snippet19": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 10, num2 = 5;\n int [BLANK] = num1 - num2;\n printf('The result is: %d', result);\n return 0;\n}",
        "answer": ["result"]
    },
    "snippet20": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int [BLANK];\n for (int i = 0; i < n; i++) {\n reverse_arr[i] = arr[n - i - 1];\n }\n return 0;\n}",
        "answer": ["reverse_arr"]
    },
    "snippet21": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK] = #\n printf('The address of num is: %p', address);\n return 0;\n}",
        "answer": ["address"]
    },
    "snippet22": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int max = arr[0];\n int [BLANK] = arr[0];\n for (int i = 1; i < n; i++) {\n if (arr[i] > max) {\n second_max = max;\n max = arr[i];\n }\n }\n printf('The second maximum element in the array is: %d', second_max);\n return 0;\n}",
        "answer": ["second_max"]
    },
    "snippet23": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int [BLANK] = num1 * num2;\n printf('The product is: %d', product);\n return 0;\n}",
        "answer": ["product"]
    },  
    "snippet24": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int [BLANK];\n for (int i = 0; i < 5; i++) {\n ptr[i] = &arr[i];\n }\n printf('The third element of the array is: %d', *ptr[2]);\n return 0;\n}",
        "answer": ["*ptr[5]"]
    },
    "snippet25": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 10, num2 = 5;\n int [BLANK] = num1 / num2;\n printf('The quotient is: %d', quotient);\n return 0;\n}",
        "answer": ["quotient"]
    },
    "snippet26": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK] = num;\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet27": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int [BLANK];\n for (int i = 0; i < 5; i++) {\n ptr[i] = &arr[i];\n }\n printf('The sum of the elements in the array is: %d', *ptr[0] + *ptr[1] + *ptr[2] + *ptr[3] + *ptr[4]);\n return 0;\n}",
        "answer": ["*ptr[5]"]
    },
    "snippet28": {
        "code": "#include <stdio.h>\n\nint main() {\n int num = 5;\n int [BLANK] = #\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
        "answer": ["*ptr"]
    },
    "snippet29": {
        "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int [BLANK];\n for (int i = 0; i < n; i++) {\n if (arr[i] % 2 == 0) {\n even_count++;\n }\n }\n printf('The number of even elements in the array is: %d', even_count);\n return 0;\n}",
        "answer": ["even_count"]
    },
    "snippet30": {
        "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int [BLANK] = num1 + num2;\n printf('The sum is: %d', sum);\n return 0;\n}",
        "answer": ["sum"]
    }
}
#-----------settings------------
PAGE_TITLE = "Complete the Code"
PAGE_ICON = ":fire:"
layout = 'centered'
#------------config-------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=layout)
st.title("</> Complete_the_code </>")

class Game:
    def __init__(self):
        snippet = random.choice(list(code_snippets.values()))
        self.code: str = snippet["code"]
        self.answers = snippet["answer"]
        
    def display(self):
        for answer in self.answers:
            self.code = self.code.replace("[BLANK]", "____")
        with st.form (key="my_form1", clear_on_submit=True):
            st.code(self.code, language='c')
            text_input = st.text_input(label="Enter Code for Blank")
            submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            return text_input
        
    def play(self):
        answers = self.display()
        
        if answers != None:
            for answer in self.answers:
                self.code = self.code.replace("____", answer, 1)
            with st.form(key="my_form2", clear_on_submit=True):
                if answers == self.answers[0]:
                    st.write("Correct" + str(answers))
                else:
                    st.write("Wrong" + str(answers))
                    st.code(self.code, language='c')
            
                # Restart Button
                replay_button = st.form_submit_button(label="Restart")
                if replay_button:
                    self.play()
            

Game().play()
