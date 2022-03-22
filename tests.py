import os
from main import Clients, Orders

DATABASE_NAME = "base.db"

def test_db_exists():
    os.system('python main.py init')
    assert os.path.exists(DATABASE_NAME)

def test_columns_exists():
    if len(Orders.select()) == 0 and len(Clients.select()) == 0:
        os.system('python main.py fill')
    assert Orders.select() and Clients.select()

def test_number_lines():
    assert len(Orders.select()) >= 10 and len(Clients.select()) >= 10
