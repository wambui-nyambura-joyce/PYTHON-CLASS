def hello(*names):
    for name in names:
        print(f"Hello {name}")
def sum (*numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer         
# Write a function that accepts any number of integers and returns the result of multiplying all of them
def multiply (*numbers):
    answer = 1
    for number in numbers:
        answer *= number
    return answer 

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")   

def my_country(country="Buurundi"):
    print(f"hello from {country}")

# Assignment
# A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*words):
    names=(" ")
    for word in words:
        names+=word
    return names
# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**strings):
    str=""
    for key,value in strings.items():
        str +=(f"{key},{value}, ") 
    return str   
        