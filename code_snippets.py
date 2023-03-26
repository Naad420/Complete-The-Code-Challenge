#-------------data--------------
import random

class Snippets():
    
    def fetch_random_snippet(self):
        code_snippets = {
            "snippet2": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK];\n ptr = #\n\n printf('The value of num is: %d', *ptr);\n\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet3": {
                "code": "#include <stdio.h>\n\nint main() {\n int i = 0;\n [BLANK] (i < 5) {\n printf(''%d '', i);\n i++;\n }\n\n return 0;\n}",
                "answer": "while"
            },
            "snippet4": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int [BLANK] = #\n\n printf('The address of num is: %p', ptr);\n\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet5": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int sum = 0;\n for (int i = 0; i < n; i++) {\n sum += arr[i];\n }\n printf('The sum of the array is: %d', sum);\n return 0;\n}",
                "answer": "sum"
            },
            "snippet6": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int [BLANK] = &num1;\n *ptr = 15;\n\n printf('The value of num1 is: %d', num1);\n\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet7": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int [BLANK];\n for (int i = 0; i < n; i++) {\n rev_arr[i] = arr[n - i - 1];\n }\n return 0;\n}",
                "answer": "rev_arr"
            },
            "snippet8": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr = #\n printf('The value of num is: %d', [BLANK]);\n return 0;\n}",
                "answer": "*ptr"
            }
        }
        snippet = random.choice(list(code_snippets.values()))
        code = snippet["code"]
        key = snippet["answer"]
        
        return str(code), str(key)
        
