import functions

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
        self._my_posts = []

    def publish_job(self):
        dict_ = functions.open_jobs_file_to_read()
        name = input('Profession name: ')
        city = input('City: ')
        salary_range = input('Salary range: ')
        scope_job = input('Full/part time job: ')
        experience = input('Requirement experience: ')
        description = input('Job description: ')
        job = Job(self.user, name, city, salary_range, scope_job, experience, description)
        if not isinstance(self._my_posts, list):
            self._my_posts = []
        self._my_posts.append(job)
        dict_[self.user] = job
        functions.open_jobs_file_to_write(dict_)

    def __repr__(self):
        return f'Employer(Name: {self._full_name} Age: {self._age})'

    @property
    def my_posts(self):
        return self._my_posts

    @my_posts.setter
    def my_posts(self, my_posts):
        if not isinstance(my_posts, list):
            raise ValueError("my_posts must be a list")
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

class Job:
    def __init__(self, manager, name, city, salary_range, scope_job, experience, description):
        self._manager = manager
        self._name = name
        self._city = city
        self._salary_range = salary_range
        self._scope_job = scope_job
        self._experience = experience
        self._description = description
        self._job_number = functions.generate_unique_random()

    def __repr__(self):
        return (f"Job(manager={self._manager}, name={self._name}, city={self._city}, "
                f"salary_range={self._salary_range}, scope_job={self._scope_job}, "
                f"experience={self._experience}, description={self._description})")
    @property
    def name(self):
        return self._name

    @property
    def city(self):
        return self._city

    @property
    def manager(self):
        return self._manager

    @property
    def salary_range(self):
        return self._salary_range

    @property
    def scope_job(self):
        return self._scope_job

    @property
    def experience(self):
        return self._experience

    @property
    def description(self):
        return self._description

    @property
    def job_number(self):
        return self._job_number

    @description.setter
    def description(self, description):
        self._description = description

    @experience.setter
    def experience(self, experience):
        self._experience = experience

    @scope_job.setter
    def scope_job(self, scope_job):
        self._scope_job = scope_job

    @salary_range.setter
    def salary_range(self, salary_range):
        self._salary_range = salary_range

    @manager.setter
    def manager(self, manager):
        self._manager = manager

    @city.setter
    def city(self, city):
        self._city = city
