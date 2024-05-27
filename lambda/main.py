# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def lamb_arr(lam_f,str_arr):
    new_list = list(filter(lam_f, str_arr))
    return new_list

ask_spaces = lambda str: (str.find(" ") == -1)

str_arr_test = ["a12 3", "a3 2 1", "222", "a444", "Ilya 2306"]
ask_a = lambda str: (str.startswith("a") == -1)
ask_more_then_five = lambda str: (len(str) > 5)
print(lamb_arr(ask_spaces, str_arr_test))
print(lamb_arr(ask_a, str_arr_test))
print(lamb_arr(ask_more_then_five, str_arr_test))

value = 50

f_string = f"Значение = {value}"
concat_str = "Значение = " + str(value)

cart = {
    "Яблоко": 23,
    "Апельсин": 47,
    "Бана": 10
}

for fruit, price in cart.items():
    print(f'Фрукт {fruit.lower()} стоит = {price}')

