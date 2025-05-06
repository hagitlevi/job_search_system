class Person:
    def __init__(self, user, password, full_name, age):
        self._user = user
        self._password = password
        self._full_name = full_name
        self._age = age

    def __str__(self):
        return f'Name: {self._full_name}\nAge: {self._age}'

    def __repr__(self):
        return f'Person(Name: {self._full_name} Age: {self._age})'

    def __eq__(self, other):
        return self.user == other.user

    @property
    def full_name(self):
        return self._full_name

    @property
    def age(self):
        return self._age

    @property
    def password(self):
        return self._password

    @property
    def user(self):
        return self._user

    @password.setter
    def password(self, password):
        self._password = password


class Employer(Person):
    def __init__(self, user, password, full_name, age):
        super().__init__(user, password, full_name, age)
        self._my_posts = None

    def __repr__(self):
        return f'Employer(Name: {self._full_name} Age: {self._age})'

    @property
    def my_posts(self):
        return self._my_posts

    @my_posts.setter
    def my_posts(self, my_posts):
        self._my_posts = my_posts


class Candidate(Person):
    def __init__(self, user, password, full_name, age):
        super().__init__(user, password, full_name, age)
        self._resume = None
        self._my_sub = None

    def __repr__(self):
        return f'Candidate(Name: {self._full_name} Age: {self._age})'

    @property
    def resume(self):
        return self._resume

    @property
    def my_sub(self):
        return self._my_sub

    @my_sub.setter
    def my_sub(self, my_sub):
        self._my_sub = my_sub