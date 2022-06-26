from python_projekat.database_model import Database
from python_projekat.user_menu import fct_cl_menu

if __name__ == "__main__":
    obj_db = Database()

    fct_cl_menu(obj_db)
