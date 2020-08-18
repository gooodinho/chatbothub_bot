from utils.db_api.sqllite import Database

db = Database()


def test():
    db.create_table_users()
    users = db.select_all_users()
    print(f"DO DOBAVLENIE: {users}")
    db.add_user(1, "One", "email", "123123123")
    db.add_user(2, "agtter", "email", "656565")
    db.add_user(3, "Ossds", "", "223")
    db.add_user(4, "fsfs", "email")
    db.add_user(5, "One", "email", "5555")
    db.add_user(6, "safsafe", "email")

    users = db.select_all_users()
    print(f"POSLE DOBAVLENIE: {users}")
    user = db.select_user(Name="Ossds", id=3)
    print(user)
    print(db.count_users())
    db.update_email("new_email", 3)
    print(db.select_user(id=3))

test()