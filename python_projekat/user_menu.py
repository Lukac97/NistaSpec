import sys

from python_projekat.register_helper import fct_prompt_register
from python_projekat.login_helper import fct_prompt_login


def fct_menu_options(obj_db, int_option):
    if int_option == 1:
        fct_prompt_register(obj_db)
    elif int_option == 2:
        fct_prompt_login(obj_db)



def fct_cl_menu(obj_db):
    int_input = 0
    while int_input != 3:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        str_input = ""
        while not str_input.isdigit():
            str_input = input("Choose option")

        int_input = int(str_input)

        fct_menu_options(obj_db, int_input)
