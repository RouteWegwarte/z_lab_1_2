from peewee import *
import random
import datetime
from sys import argv

from raw import fnames, snames, cities, addresses

db = SqliteDatabase('base.db')

class BaseModel(Model):
    class Meta:
        database = db

class Clients(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

class Orders(BaseModel):
    clients = ForeignKeyField(Clients)
    date = DateField()
    amount = IntegerField()
    description = TextField()

def init():
    if not (Clients.table_exists() and Orders.table_exists()):
        db.create_tables([Clients, Orders])
    else:
        db.drop_tables([Clients, Orders])
        db.create_tables([Clients, Orders])
    db.close()

def fill():
    for i in range(20):
        client = Clients.create(
            name = random.choice(fnames) + " " + random.choice(snames),
            city = random.choice(cities),
            address = random.choice(addresses) + " " + str(random.randint(1, 255))
        )
    for i in range(20):
        order = Orders.create(
            clients = Clients.get_by_id(random.randint(1,10)),
            date = datetime.datetime.now(),
            amount = random.randint(1,10),
            description = "zakaz"
        )

def show(Model):
    data = Model.select()
    for inf in data:
        if (Model is Clients):
            print(*("{:<30}".format(str(i)) for i in [inf.id, inf.name, inf.city, inf.address]))
        else:
            print(*("{:<30}".format(str(i)) for i in [inf.clients, inf.date, inf.amount, inf.description]))


if __name__ == "__main__":

    try:
        arg = argv[1]
        if arg == "init":
            init()
        elif arg == "fill":
            fill()
        elif arg == "show":
            try:
                if argv[2] == "Clients":
                    show(Clients)
                elif argv[2] == "Orders":
                    show(Orders)
                else:
                    print("Incorrect tablename")
            except:
                print("Input table name in args: main.py show Clients | main.py show Orders")
    except IndexError:
        print("Error")

db.close()
