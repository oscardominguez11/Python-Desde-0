# Vars

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenar de variables en Print
print(my_variable, my_int_variable, my_bool_variable)
print("Este es el vaor de mi variable:", my_bool_variable)

# Funciones del Sistema
print(len(my_int_to_str_variable))

# Variables en una sola línea
name, surname, alias, edad = "Oscar", "Dominguez", "byoscaarr", 22
print("Me llamo:", name, surname,". Mi edad es:", edad,". Mi alias es:", alias)