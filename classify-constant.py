#Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

#solution 

constant = { 
    "index": "Non-idiomatic",
    "CatName": "Non-idiomatic",
    "snake_case": "Non-idiomatic",
    "LAZY_DOG3": "idiomatic",
    "1st": "Illegal",
    "operand2": "Non-idiomatic",
    "BIG_NUMBER": "idiomatic",
}
for name, classification in constant. items():
    print(f"{name}: {classification}")   
   