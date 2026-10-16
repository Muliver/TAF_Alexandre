pi = 3.141592
my_fstring = f"pi = {pi}"
print(my_fstring)
my_string_with_4decimals = f"pi = {pi:.4f}"
print(my_string_with_4decimals)
l = [i for i in range(10)]
print(l)
salesman = {"name": "Dwight", "age": 30}  # dictionnaires python
print(salesman["name"])
salesman["rank"] = "Assistant (to the) regional manager"
print(salesman)
salesman["rank"] = "Regional manager"
print(salesman)
key_value_pairs_items = salesman.items()  # .items permet de boucler sur les dictionnaires!
print(salesman.items())
names = ["Michael", "Jim", "Dwight"]  # list python
print("--------ITERATES--------------")
for name in names:
    print(f"Element: {name}")
print("----------------------")
for iname, name in enumerate(names):  # enumerate permet de récupérer l'indice !!!!!
    print(f"Index {iname}: {name}")
print("----------------------")
for key, value in salesman.items():
    print(f"key: {key}, value: {value}")
print("----------------------")
names_men = ["Michael", "Jim", "Dwight"]
names_women = ["Holly", "Pam", "Angela"]
for name_man, name_woman in zip(
    names_men, names_women
):  # zip permet de mélanger et d'utiliser en même temps 2 listes !!!
    print(f"{name_man} and {name_woman} form a couple")
print("----------------------")
for icouple, (name_man, name_woman) in enumerate(zip(names_men, names_women)):
    print(f"Couple {icouple}: {name_man} and {name_woman}")
