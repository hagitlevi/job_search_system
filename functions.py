import json
import os
from classes import Candidate
from colors import bcolors
import pickle
import classes
import random

def open_file_to_write(dictionary):
    try:
        with open("users.txt", "wb") as f:
            pickle.dump(dictionary, f)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error with opening the file {e}')
    return

def open_jobs_file_to_write(dictionary):
    try:
        with open("jobs.txt", "wb") as f:
            pickle.dump(dictionary, f)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error with opening the file {e}')
    return

def open_file_to_read():
    dictionary = {}
    try:
        with open("users.txt", "rb") as f:
            dictionary = pickle.load(f)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error with opening the file {e}')
    return dictionary

def open_jobs_file_to_read():
    dictionary = {}
    try:
        with open("jobs.txt", "rb") as f:
            dictionary = pickle.load(f)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error with opening the file {e}')
    return dictionary

def sign_up():
    dict_ = open_file_to_read()
    full_name = input('Enter your full name: ')
    age = int(input('Enter your age: '))
    while True:
        try:
            username = input('Username: ')
            if username in dict_:
                raise KeyError('try to creat a username that does not exist')
            else:
                password = input('Password: ')
                break
        except KeyError as e:
            print(f'{e}, Try again')
    while True:
        try:
            choice = int(input('Press 1 to Employer profile and 2 to Candidate profile: '))
            if choice == 1:
                employer_user = classes.Employer(username, password, full_name, age)
                dict_[username] = employer_user
                break
            if choice == 2:
                candidate_user = classes.Candidate(username, password, full_name, age)
                dict_[username] = candidate_user
                break
        except ValueError:
            print('Choose again')

    open_file_to_write(dict_)
    print('Welcome! your registration has been successfully received')
    if choice == 1:
        return 'Employer', username
    return 'Candidate' , username

def log_in():
    while True:
        username = input('Username: ')
        dict_ = open_file_to_read()
        if username in dict_:
            password = input('Password: ')
            user = dict_[username]
            if password != user.password:
                print('Wrong password!')
            else:
                return type(dict_[username]), username
        else:
            print('Wrong username! Try again')

def entrance():
    """
    log in or sign up to the system
    :return: type of user
    """
    while True:
        choice = int(input(bcolors.OKBLUE + 'choose an option: \n1. Log in \n2. Sign up\n'))
        if choice == 1:
            typ, username = log_in()
            if typ is Candidate:
                return 'Candidate', username
            else:
                return 'Employer', username

        elif choice == 2:
            typ, username = sign_up()
            return typ, username
        print(bcolors.FAIL + 'Invalid input, Try again' + bcolors.ENDC)

def load_used_numbers():
    if os.path.exists('numbers.txt'):
        with open('numbers.txt', 'r') as f:
            return set(json.load(f))
    return set()

def save_used_numbers(numbers):
    with open('numbers.txt', 'w') as f:
        json.dump(list(numbers), f)

def generate_unique_random(min_val=1, max_val=1000000):
    used = load_used_numbers()
    attempts = 0
    while attempts < 1000:
        num = random.randint(min_val, max_val)
        if num not in used:
            used.add(num)
            save_used_numbers(used)
            return num
        attempts += 1
    raise Exception("Can not find a number in this range")

def view_my_jobs(username):
    """
    Candidate views all available jobs in the system
    :param username: candidate's username
    :return: None
    """
    jobs_dict =open_jobs_file_to_read()
    my_jobs = jobs_dict[username]
    if not jobs_dict:
        print("There are no jobs at the moment.")
        return

    found = False
    for i, job in enumerate(my_jobs):
        print(f"Job number: {job.job_number}")
        print(f"Profession: {job.name}")
        print(f"City: {job.city}")
        print(f"Salary Range: {job.salary_range}")
        print(f"Job Type: {job.scope_job}")
        print(f"Experience Required: {job.experience}")
        print(f"Description: {job.description}")
        print("-" * 40)
        found = True

    if not found:
        print("No available jobs were found.")

def check_city(city):
    text = "Afula Akko Arad Ariel Ashdod Ashkelon Bnei-Brak Bat-Yam Beersheba Beit-Shean Beit-Shemesh Beitar-Illit Bnei-Ayish Dimona Eilat Elad Givat-Shmuel Giv'atayim Hadera Haifa Harish Herzliya Holon Hoshaya Jerusalem Karmiel Kfar-Saba Kiryat-Ata Kiryat-Bialik Kiryat-Gat Kiryat-Malakhi Kiryat-Motzkin Kiryat-Ono Kiryat-Shmona Kiryat-Yam Lod Ma'alot-Tarshiha Ma'ale-Adumim Migdal-HaEmek Modiin-Illit Modiin-Maccabim-Reut Nahariya Nazareth Nazareth-Illit Ness-Ziona Netanya Netivot Ofakim Or-Akiva Or-Yehuda Petah-Tikva Raanana Ramat-Gan Ramat-Hasharon Ramla Rehovot Rishon-Lezion Rosh-HaAyin Safed Sakhnin Sderot Shoham Tamra Tayibe Tel-Aviv-Jaffa Tiberias Tirat-Carmel Umm-al-Fahm Yavne Yehud-Monosson Yokneam-Illit Zefat"
    cities = text.split()
    if city in cities:
            return True
    return False

def advanced_search():
    filters = []
    print(bcolors.OKGREEN + 'you have entered advanced search\n' + bcolors.ENDC)
    print(bcolors.OKBLUE + 'choose your filters\n')

    profession = input('Enter your profession (or type "skip"): ')
    filters.append(profession if profession != '2' else 'skip')

    choose = int(input('1. full time\n2. part time: '))
    filters.append('full time' if choose == 1 else 'part time')

    city = input('Choose your preferred city (or type "skip"): ')
    if city.lower() == 'skip' or city == '2':
        filters.append('skip')
    else:
        while not check_city(city):
            city = input(bcolors.FAIL + 'City not found. Please try again: ' + bcolors.ENDC)
        filters.append(city)

    exp = input('Do you prefer jobs that require experience? (yes/no/skip): ').lower()
    if exp not in ['yes', 'no']:
        exp = 'skip'
    filters.append(exp)

    return search(filters)


def search(filters):
    filtered = []
    number = 1
    jobs = open_jobs_file_to_read()

    for user in jobs:
        for job in jobs[user]:
            if filters[0].lower() == 'skip' or job.name.lower() == filters[0].lower():
                if job.scope_job.lower() == filters[1].lower():
                    if filters[2].lower() == 'skip' or job.city.lower() == filters[2].lower():
                        if filters[3].lower() == 'skip' or job.experience.lower() == filters[3].lower():
                            filtered.append(job.job_number)
                            print(f"{number}: ")
                            job.print_details()
                            number += 1

    if number == 1:
        print('jobs not found')
    return apply_for_job(filtered)


def apply_for_job(filtered):
    job_index = int(input('Choose the job number you want to apply for: '))
    if job_index > len(filtered) or job_index < 1:
        print('Invalid job selection. Please choose a valid job number.')
        return False

    selected_job_number = filtered[job_index - 1]

    jobs = open_jobs_file_to_read()
    users = open_file_to_read()

    current_user = input("Enter your username: ")  # Ensure the correct user is identified
    if current_user not in users:
        print("User not found in the system.")
        return False

    user = users[current_user]
    if not isinstance(user, Candidate):
        print("Only candidates can apply for jobs.")
        return False

    for job_owner in jobs:
        for job_ in jobs[job_owner]:
            if job_.job_number == selected_job_number:
                if hasattr(user, 'applied_jobs') and selected_job_number in user.applied_jobs:
                    print('You have already applied for this job')
                    return False
                else:
                    if not hasattr(user, 'applied_jobs'):
                        user.applied_jobs = []  # Initialize if not present
                    user.applied_jobs.append(selected_job_number)

                    # Attach the resume to the application
                    if user.resume:
                        print(f"Your resume has been attached to the application:\n{user.resume}")
                    else:
                        print("No resume found in your profile. Application submitted without a resume.")

                    print('You have successfully applied for the job')
                    open_jobs_file_to_write(jobs)
                    open_file_to_write(users)
                    return True

    print("Job number not found in the system.")
    return False



def contact():
    print('For technical assistance, please fill out the form below or contact us at\n' + bcolors.PINKBG + 'hirescopeofficial@gmail.com\n +1 (555) 123-4567\n' + bcolors.ENDC + '. We’ll get back to you within 24 hour')

common_issues = {
    "1": ("I forgot my password", "To reset your password, click 'Forgot Password' on the login screen."),
    "2": ("I can't edit my profile", "Go to 'Edit Profile' from the main menu and make sure to save your changes."),
    "3": ("I can't post a job", "Make sure all required fields are filled in the 'Post Job' form, then click for Publish."),
    "4": ("I can't see candidates", "Go to 'My Jobs' and click on 'View Candidates' for the relevant job."),
    "5": ("Other issue", "Please contact us at support@hirescope.com and we’ll assist you as soon as possible."),
}

def show_menu():
    print("\nHow can we help you? Please choose a number:")
    for key, (title, _) in common_issues.items():
        print(f"{key}. {title}")

def chatbot_loop():
    while True:
        show_menu()
        choice = input(">> ").strip()

        if choice in common_issues:
            print("\n📌 Solution:")
            print(common_issues[choice][1])

            follow_up = input("\nWould you like help with another issue? (yes/no): ").strip().lower()
            if follow_up != "yes":
                print("Returning to the main menu. Thank you!")
                break
        else:
            print("❗ Invalid choice. Please enter a number from the list.")

def is_human_check():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2

    print("\n🔒 Human verification:")
    print(f"What is {num1} {operator} {num2}?")

    try:
        user_input = int(input("Your answer: "))
        if user_input == answer:
            print("✅ Verified as human.\n")
            return True
        else:
            print("❌ Incorrect. Try again.")
            return False
    except ValueError:
        print("❌ Invalid input. Try again.")
        return False

def human_check():
    print("Before continuing, we need to make sure you're not a robot.")
    print("Please answer the following question creatively:")

    print("\n🌵 What would you do if you were a cactus in the desert?")
    answer = input("> ")

    if len(answer.strip().split()) < 5:
        print("\n🤖 Hmm... that answer is a bit too short. Are you really human?")
        return False

    print("\n✅ That was weird enough to sound human. Welcome!")
    return True

def strong_password():
    while True:
        password = input('Password: ')
        if len(password) >=8 and any(c.isupper() for c in password):
            return True
        print('The password is not strong enough, Try  again')




print('test')

