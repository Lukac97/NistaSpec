from python_projekat.database_model import Database
from python_projekat.register_helper import fct_prompt_register


if __name__ == "__main__":
    obj_db = Database()

    while True:
        fct_prompt_register(obj_db)
