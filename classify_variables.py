#Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

#solution 

variables = {
    "index": "idiomatic",
    "CatName": "Non-idiomatic",
    "lazy_dog": "idiomatic",
    "quick_fox": "Non-idiomatic",
    "1stCharacter": "Illegal",
    "operand2": "idiomatic",
    "BIG_NUMBER": "Non-idiomatic",
    "π": "idiomatic",
}    

for name, classification in variables.items():
    print(f"{name}: {classification}")
    