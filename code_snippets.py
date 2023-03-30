#-------------data--------------
import random

class Snippets():
    
    def fetch_random_snippet(self):
        code_snippets = {
            "snippet1": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int sum = 0;\n for (int i = 0; i < n; i++) {\n sum += arr[i];\n }\n printf('The sum of the array is: %d', sum);\n return 0;\n}",
                "answer": "sum"
            },
            "snippet2": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int *ptr = &num1;\n *ptr = 15;\n\n printf('The value of num1 is: %d', num1);\n\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet3": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int rev_arr;\n for (int i = 0; i < n; i++) {\n rev_arr[i] = arr[n - i - 1];\n }\n return 0;\n}",
                "answer": "rev_arr"
            },
            "snippet4": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int max;\n if (num1 > num2) {\n max = num1;\n } else {\n max = num2;\n }\n printf('The maximum number is: %d', max);\n return 0;\n}",
                "answer": "max"
            },
            "snippet5": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int new_arr;\n for (int i = 0; i < n; i++) {\n new_arr[i] = arr[i] * 2;\n }\n return 0;\n}",
                "answer": "new_arr"
            },
            "snippet6": {
                "code": "#include <stdio.h>\n\nint main() {\n int i = 0;\n while(i <= 10) {\n printf('%d ', i);\n i += 2;\n }\n\n return 0;\n}",
                "answer": "while"
            },
            "snippet7": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int max = arr[0];\n for (int i = 1; i < n; i++) {\n if (arr[i] > max) {\n max = arr[i];\n }\n }\n printf('The maximum element in the array is: %d', max);\n return 0;\n}",
                "answer": "max"
            },
            "snippet8": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int even_arr;\n for (int i = 0; i < n; i++) {\n even_arr[i] = arr[i] % 2 == 0 ? arr[i] : 0;\n }\n return 0;\n}",
                "answer": "even_arr"
            },
            "snippet9": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 5;\n int *ptr = num;\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet10": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int sum = 0;\n for (int i = 0; i < n; i++) {\n sum += arr[i];\n }\n int average = sum / n;\n printf('The average of the elements in the array is: %d', average);\n return 0;\n}",
                "answer": "average"
            },
            "snippet11": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 10, num2 = 5;\n int result = num1 - num2;\n printf('The result is: %d', result);\n return 0;\n}",
                "answer": "result"
            },
            "snippet12": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int reverse_arr;\n for (int i = 0; i < n; i++) {\n reverse_arr[i] = arr[n - i - 1];\n }\n return 0;\n}",
                "answer": "reverse_arr"
            },
            "snippet13": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int address = #\n printf('The address of num is: %p', address);\n return 0;\n}",
                "answer": "address"
            },
            "snippet14": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int max = arr[0];\n int second_max = arr[0];\n for (int i = 1; i < n; i++) {\n if (arr[i] > max) {\n second_max = max;\n max = arr[i];\n }\n }\n printf('The second maximum element in the array is: %d', second_max);\n return 0;\n}",
                "answer": "second_max"
            },
            "snippet15": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int product = num1 * num2;\n printf('The product is: %d', product);\n return 0;\n}",
                "answer": "product"
            },
            "snippet16": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int *ptr[5];\n for (int i = 0; i < 5; i++) {\n ptr[i] = &arr[i];\n }\n printf('The third element of the array is: %d', *ptr[2]);\n return 0;\n}",
                "answer": "*ptr[5]"
            },
            "snippet17": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 10, num2 = 5;\n int quotient = num1 / num2;\n printf('The quotient is: %d', quotient);\n return 0;\n}",
                "answer": "quotient"
            },
            "snippet18": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 10;\n int *ptr = num;\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet19": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int *ptr[5];\n for (int i = 0; i < 5; i++) {\n ptr[i] = &arr[i];\n }\n printf('The sum of the elements in the array is: %d', *ptr[0] + *ptr[1] + *ptr[2] + *ptr[3] + *ptr[4]);\n return 0;\n}",
                "answer": "*ptr[5]"
            },
            "snippet20": {
                "code": "#include <stdio.h>\n\nint main() {\n int num = 5;\n int *ptr = #\n printf('The value of num is: %d', *ptr);\n return 0;\n}",
                "answer": "*ptr"
            },
            "snippet21": {
                "code": "#include <stdio.h>\n\nint main() {\n int arr[] = {1, 2, 3, 4, 5};\n int n = sizeof(arr) / sizeof(arr[0]);\n int even_count;\n for (int i = 0; i < n; i++) {\n if (arr[i] % 2 == 0) {\n even_count++;\n }\n }\n printf('The number of even elements in the array is: %d', even_count);\n return 0;\n}",
                "answer": "even_count"
            },
            "snippet22": {
                "code": "#include <stdio.h>\n\nint main() {\n int num1 = 5, num2 = 10;\n int sum = num1 + num2;\n printf('The sum is: %d', sum);\n return 0;\n}",
                "answer": "sum"
            },
            "snippet23": {
                'code': '''
                    #include <stdio.h> 
                main() {
                int n, i, c = 0;
                printf("Enter any number n:");
                scanf("%d", &n);


                for (i = 1; i <= n; i++) {
                    if (n%i==0) {
                        c++;
                    }
                }

                if (c == 2) {
                        printf("n is a Prime number");
                }
                else {
                        printf("n is not a Prime number");
                }
                return 0;    
                }
            ''',
                'answer': 'n%i==0'
            },
            "snippet24": {
                'code': '''#include <stdio.h>
        int main() {
          int n, reversed = 0, remainder, original;
            printf("Enter an integer: ");
            scanf("%d", &n);
            original = n;

            // reversed integer is stored in reversed variable
            while (n != 0) {
                remainder =n%10;
                reversed = reversed * 10 + remainder;
                n /= 10;
            }

            // palindrome if orignal and reversed are equal
            if (original == reversed)
                printf("%d is a palindrome.", original);
            else
                printf("%d is not a palindrome.", original);
            return 0;
        }''',
                'answer': 'n%10'
            },
            "snippet25": {
                'code': '''
        #include <stdio.h>
        int main() {
          int n=9;

          for (int i = 1; i <= 10; ++i) {
            printf("%d * %d = %d", n, i, n*i);
          }
          return 0;
        }''',
                'answer': 'n*i'
            },
            "snippet26": {
                'code': '''
        #include <stdio.h>
        int main() {    

            int number1, number2, sum;

            printf("Enter two integers: ");
            scanf("%d %d", &number1, &number2);

            // calculate the sum
            sum = number1 + number2;      

            printf("%d + %d = %d", number1, number2, sum);
            return 0;
        }
                ''',
                'answer': 'int'
            },
            "snippet27": {
                'code': '''
        #include<stdio.h>
        int main() {
          double first, second, temp;
          printf("Enter first number: ");
          scanf("%lf", &first);
          printf("Enter second number: ");
          scanf("%lf", &second);

          // value of first is assigned to temp
          temp = first;

          first = second;

          second = temp;

          printf("After swapping, first number = %.2lf", first);
          printf("After swapping, second number = %.2lf", second);
          return 0;
        }
                ''',
                'answer': 'temp'
            },
            "snippet28": {
                'code': '''
        #include <stdio.h>
        void main()
        {
            // fact to store factorial of number N
            int fact = 1, n;
            // Take input
            printf("Enter the number: ");
            scanf("%d", &n);
            // Check validity of N
            if (n <= 0)
            fact = 1;
            // Loop N times and multiply all positive numbers
            else
            {
                for (int i = 1; i <= n; i++)
                {
                    fact = fact * i;
                }
            }
            // Print the fact.
            printf("Factorial of %d = %5d", n, fact);
        }

                ''',
                'answer': 'i++'
            },

            "snippet29": {
                'code': '''
        #include <stdio.h>
            void main()
            {
                int array[10];
                int i;
                printf("enter the element of an array \n");
                for (i = 0; i < 10; i++){
                    scanf("%d", &array[i]);
                    }
                printf("Alternate elements of a given array \n");
                for (i = 0; i < 10; i += 2)
                    printf( "%d", array[i]) ;
            }
        ''',
                'answer': 'array'
            },

            "snippet30": {
                'code': '''
        #include<stdio.h>

        int main()
        {
            printf("Studytonight - Best place to learn");

            // Local Variable Definition
            char grade;
            printf("Enter your grade:\n");
            scanf("%c", &grade);

            switch(grade)
            {
                case 'A':
                    printf("Excellent");
                    break;
                case 'B':
                    printf("Keep it up!");
                    break;
                case 'C':
                    printf("Well done");
                    break;
                case 'D':
                    printf("You passed");
                    break;
                case 'F':
                    printf("Better luck next time");
                    break;
                default:
                    printf("Invalid grade");
            }
            printf("Your grade is %c",grade);
            printf("Coding is Fun !");
            return 0;
        }
                ''',
                'answer': 'default'
            },

            "snippet31": {
                'code': '''
        #include<stdio.h>

        int main(){
        float fahrenheit, celsius;
        printf(“Enter temperature in Celsius:”);
        scanf(“%d”,&celsius
        fahrenheit =((celsius*9)/5)+32;
        printf(" Temperature in fahrenheit is: %f",fahrenheit);
        return(0);
        }
        ''',
                'answer': 'celsius'
            },

            "snippet32": {
                'code': '''
        #include <stdio.h>

        int main()
        {
            // Initializing variable.
            char str[100];  
            int i, vowels = 0;

            // Accepting input.
            printf("Enter the string: ");

            gets(str);

            //Initializing for loop. 
            for(i = 0; str[i]; i++)  
            {
                //Counting the vowels.
                if(str[i]=='a'|| str[i]=='e'||str[i]=='i'||
                   str[i]=='o'|| str[i]=='u'||str[i]=='A'||
                   str[i]=='E'||str[i]=='I'||str[i]=='O' ||str[i]=='U')
                {
                    vowels++;
                }
            }

            //Printing the count of vowels.
            printf("Total number of vowels: = %d",vowels);

            return 0;
        }
                ''',
                'answer': 'str'
            },
            "snippet33": {
                'code': '''
            #include <stdio.h>
            void main()
            {
                int array[10];
                int i;
                printf("enter the element of an array ");
                for (i = 0; i < 10; i++){
                    scanf("%d", &array[i]);
                    printf("Alternate elements of a given array ");
                }
                for (i = 0; i < 10; i += 2){
                    printf( "%d", array[i]) ;
                }
            }

                ''',
                'answer': 'array'
            },
            "snippet34": {
                'code': '''
        #include <stdio.h>
        int main()
        {
          float Pi=3.14, area, circumference, radius;

          printf("Enter radius of circle: ");

          scanf("%f",&radius);

          area = Pi * radius * radius;
          printf("Area of circle is: %f",area);

          circumference = 2 * Pi * radius;
          printf("Circumference of circle is: %f",circumference);

          return 0;
            }
                ''',
                'answer': '&radius'
            },
            "snippet35": {
                'code': '''
        #include <stdio.h>
        #include <math.h> //to use sqrt() function
        int main(){

          float side, area, temp;

          printf("Enter the Side of the triangle: ");
          scanf("%f",&side);

          //Calculate and print the area of Equilateral Triangle
          temp = sqrt(3) / 4 ;
          area = temp * side * side ;
          printf("Area of Equilateral Triangle is: %f",area);

          return 0;
            }
                ''',
                'answer': 'area'
            },
            "snippet36": {
                'code': '''
        #include <stdio.h>

        int main() {

          int n, reverse = 0, remainder;

          printf("Enter an integer: ");
          scanf("%d", &n);

          while (n != 0) {
            remainder = n % 10;
            reverse = reverse * 10 + remainder;
            n /= 10;
          }

          printf("Reversed number = %d", reverse);

          return 0;
        }
                ''',
                'answer': 'reverse'
            },
            "snippet37": {
                'code': '''
        #include <stdio.h>

        int main() {

          int n, reverse = 0, remainder;

          printf("Enter an integer: ");
          scanf("%d", &n);

          while (n != 0) {
            remainder = n % 10;
            reverse = reverse * 10 + remainder;
            n /= 10;
          }

          printf("Reversed number = %d", reverse);

          return 0;
        }
                ''',
                'answer': 'remainder'
            },
            "snippet38": {
                'code': '''
        #include <stdio.h>
        void main()
        {
            float base,height;
            printf("Enter Base and Height: ");
            scanf("%f %f",&base,&height);
            float area = (base * height) / 2;
        
            //Area with precision of 2 decimal places
            printf("Area of Triangle is %0.2f",area);
        }
                ''',
                'answer': 'base * height'
            }
        }
        snippet = random.choice(list(code_snippets.values()))
        code = snippet["code"]
        key = snippet["answer"]
        
        return str(code), str(key)
        
