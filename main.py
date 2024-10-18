# Система управления учетными записями

class User():
    def __init__(self, id, name, user):
        self.id = id
        self.name = name
        self.user = user
    def add_user(self):
        print(f'добавлен пользователь: {self.name}')
    def remove_user(self):
        print(f'удален пользователь: {self.name}')
    def __info(self):
        print(self.id, self.name, self.user)
    def info(self):
        self.__info()
class Admin(User):
    def __init__(self, id, name, user, admin):
        super().__init__(id, name, user)
        self.admin = admin
    def __add_user(self):
        print(f'добавлен пользователь: {self.name}')
    def __remove_user(self):
        print(f'удален пользователь: {self.name}')
    def __info(self):
        print(self.id, self.name, self.user, self.admin)
    def add_user(self):
        self.__add_user()
    def remove_user(self):
        self.__remove_user()
    def info(self):
        self.__info()

user1 = User('08476', 'Николай', 'B')
user2 = User('97659', 'Максим', 'B')

admin1 = Admin('12345', 'Виктор', 'B', 'A')
admin2 = Admin('56789', 'Степан', 'B', 'A')

user1.add_user()
user1.remove_user()
user1.info()
user2.add_user()
user2.info()

admin1.add_user()
admin1.remove_user()
admin1.info()
admin2.add_user()
admin2.info()


