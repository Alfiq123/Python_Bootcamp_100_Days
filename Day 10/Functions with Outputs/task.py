# Pause 1
# def format_name(f_name, l_name):
#     f_name = str(input("Enter your first name: "))
#     l_name = str(input("Enter your last name: "))
#     print(f"{f_name} {l_name}")
# format_name()

# # Pause 2
# def format_name(f_name, l_name):
#     # f_name.title()
#     # l_name.title()
#     # print(f"{f_name} {l_name}")
#     return f"{f_name} {l_name}"

# first = str(input("Enter your first name: ")).title()
# last = str(input("Enter your last name: ")).title()
#
# print(format_name(f_name=first, l_name=last))
# # print(formatted)

def func_one(text):
    return text + " " + text

def func_two(text):
    return text.title()

output = func_two(func_one("hello"))
print(output)
