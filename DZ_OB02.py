# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и
# уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный
# атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также
# содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей
# из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Геттеры
    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттеры
    def set_name(self, name):
        self.__name = name

    def set_access_level(self, level):
        if level in ['user', 'admin']:
            self.__access_level = level
        else:
            raise ValueError("Недопустимый уровень доступа")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.set_access_level('admin')
        self.__managed_users = []

    def add_user(self, user):
        self.__managed_users.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_id):
        for user in self.__managed_users:
            if user.get_id() == user_id:
                self.__managed_users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self):
        print("Список пользователей:")
        for user in self.__managed_users:
            print(f"ID: {user.get_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Получить список пользователей
    def get_managed_users(self):
        return self.__managed_users.copy()

#Пример использования

# Создание админа
admin = Admin(1, "Иван")

# Создание пользователей
user1 = User(2, "Алексей")
user2 = User(3, "Мария")

# Добавление пользователей
admin.add_user(user1)
admin.add_user(user2)

# Просмотр списка пользователей
admin.list_users()

# Удаление пользователя
admin.remove_user(2)
admin.list_users()



