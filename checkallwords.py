import string
import keyword

def is_valid_variable_name(name):
    return (
        name not in keyword.kwlist and
        name[0].isalpha() or name[0] == '_' and
        all(c.islower() or c.isdigit() or c == '_' for c in name) and
        name.count('_') <= 1
    )

# Пример
variable_names = [
    "_", "__", "___", "x", "get_value", "get value",
    "get!value", "some_super_puper_value", "Get_value",
    "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"
]

for name in variable_names:
    print(f"{name} => {is_valid_variable_name(name)}")
