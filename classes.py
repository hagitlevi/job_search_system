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

    def __repr__(self):
        return f'Employer(Name: {self._full_name} Age: {self._age})'

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
        dict_[self.user] = self._my_posts
        functions.open_jobs_file_to_write(dict_)

    def delete_job(self):
        dict_ = functions.open_jobs_file_to_read()
        dict_users = functions.open_file_to_read()
        my_jobs = dict_[self.user]
        flag = False
        number = input('Enter the number of that specific job(you can see it by choose "view my jobs" in your menu)\n 🔙Press enter to go back')
        if not number:
            return 1
        for job in my_jobs:
            if job.job_number == number:
                flag = True
                self._my_posts = my_jobs.remove(job)
                break
        if not flag:
            print("Can not find this job")
            return False
        dict_[self.user] = self._my_posts
        dict_users[self.user] = self
        functions.open_file_to_write(dict_users)
        functions.open_jobs_file_to_write(dict_)
        return True

    def edit_job(self):
        jobs = functions.open_jobs_file_to_read()
        my_jobs = jobs[self.user]
        if not my_jobs:
            print("You have no jobs to edit.")
            return

        job_number_ = int(input("Enter the job number of the job you want to edit (you can see it by choose 'view my jobs' in your menu'): "))
        job_to_edit = None

        for job in my_jobs:
            if job.job_number == job_number_:
                job_to_edit = job
                my_jobs.remove(job)
                break

        if not job_to_edit:
            print("Job not found.")
            return

        print("Current name:", job_to_edit.name)
        new_name = input("Enter new name (press Enter to keep current): ")
        if new_name:
            job_to_edit.name = new_name

        print("Current city:", job_to_edit.city)
        new_city = input("Enter new city (press Enter to keep current): ")
        if new_city:
            job_to_edit.city = new_city

        print("Current salary range:", job_to_edit.salary_range)
        new_salary_range = input("Enter new salary range (press Enter to keep current): ")
        if new_salary_range:
            job_to_edit.salary_range = new_salary_range

        print("Current scope (full/part time):", job_to_edit.scope_job)
        new_scope_job = input("Enter new scope (press Enter to keep current): ")
        if new_scope_job:
            job_to_edit.scope_job = new_scope_job

        print("Current experience requirement:", job_to_edit.experience)
        new_experience = input("Enter new experience requirement (press Enter to keep current): ")
        if new_experience:
            job_to_edit.experience = new_experience

        print("Current description:", job_to_edit.description)
        new_description = input("Enter new description (press Enter to keep current): ")
        if new_description:
            job_to_edit.description = new_description

        my_jobs.append(job_to_edit)
        jobs[self.user] = my_jobs
        functions.open_jobs_file_to_write(jobs)
        print("Job updated successfully.")

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
        self.applied_jobs = []

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

    def print_details(self):
        print(f"Manager: {self._manager}")
        print(f"Name: {self._name}")
        print(f"City: {self._city}")
        print(f"Salary Range: {self._salary_range}")
        print(f"Job Type: {self._scope_job}")
        print(f"Experience Required: {self._experience}")
        print(f"Description: {self._description}")

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

print('test2')