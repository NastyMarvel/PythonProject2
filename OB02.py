class User:
    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._access_level = 'user'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def access_level(self):
        return self._access_level

    def __repr__(self):
        return f'<User(id={self.id}, name="{self.name}", access_level="{self.access_level}")>'


class Admin(User):
    def __init__(self, admin_id, name):
        super().__init__(admin_id, name)
        self._access_level = 'admin'

    def add_user(self, users_list, new_user):
        if not isinstance(new_user, User):
            raise TypeError("new_user must be an instance of the User class")

        users_list.append(new_user)

    def remove_user(self, users_list, user_to_remove):
        try:
            users_list.remove(user_to_remove)
        except ValueError as e:
            print(f"User {user_to_remove} is not in the list.")


# Создаем обычного пользователя
user1 = User('U001', 'Иван Иванов')
print(user1)  # Вывод: <User(id=U001, name="Иван Иванов", access_level="user")>

# Создаем администратора
admin1 = Admin('A001', 'Алексей Алексеев')
print(admin1)  # Вывод: <User(id=A001, name="Алексей Алексеев", access_level="admin")>

# Список всех пользователей
users = []

# Добавляем пользователя через админа
admin1.add_user(users, user1)
print(users)  # Вывод: [<User(id='U001', name="Иван Иванов", access_level='user')>]

# Пытаемся удалить несуществующего пользователя
admin1.remove_user(users, User('U002', 'Петр Петров'))
# Вывод: User <User(id='U002', name="Петр Петров", access_level='user')> is not in the list.

# Удаляем существующего пользователя
admin1.remove_user(users, user1)
print(users)  # Вывод: []
