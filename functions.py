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
                print('log in succeeded')
                return 'Candidate', username
            else:
                print('log in succeeded')
                return 'Employer', username

        elif choice == 2:
            typ, username = sign_up()
            print('sign up succeeded')
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
    if not jobs_dict:
        print("There are no jobs at the moment.")
        return

    print(bcolors.HEADER + f'\nAvailable jobs for candidate {username}:\n' + bcolors.ENDC)
    found = False
    for manager, job in jobs_dict.items():
        print(bcolors.HEADER + f"Published by: {manager}" + bcolors.ENDC)
        print(f"Profession: {job.name}")
        print(f"City: {job.city}")
        print(f"Salary Range: {job.salary_range}")
        print(f"Job Type: {job.scope_job}")
        print(f"Experience Required: {job.experience}")
        print(f"Description: {job.description}")
        print(f"Job number: {job.job_number}")
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
    choose = input('enter your profession. press 2 to skip this filter: ')
    filters.append(choose)
    choose = int(input('1. full time\n2. part time: '))
    if choose == 1:
        scope = True
    else:
        scope = False
    filters.append(scope)
    choose = input('choose your preferred city. press 2 to skip this filter: ')
    if choose == '2':
        filters.append(choose)
    else:
        while check_city(city) is False:
            city = input(bcolors.FAIL + 'city is not found. please try again: ' + bcolors.ENDC)
        filters.append(city)
    choose = int(input('do you prefer jobs that require experience?\n0 - NO\n1 - YES\n2 - skip: '))
    if choose == 2:
        filters.append('2')
    else:
        filters.append(bool(choose))
    return search(filters)

def search(filters):
    filtered = [] # save all the jobs that match the filters
    number = 1
    jobs = open_jobs_file_to_read()
    for user in jobs:
        for job in jobs[user]:
            if job.name == filters[0] or filters[0] == '2':
                if job.scope_job == filtered[1]:
                    if job.city == filtered[2] or filters[2] == '2':
                        if job.experience == filtered[3] or filters[3] == '2':
                            filtered.append(job.job_number)
                            print({number}, job)
                            number+=1
    return filtered

def contact():
    print('For technical assistance, please fill out the form below or contact us at\n' + bcolors.PINKBG + 'hirescopeofficial@gmail.com\n +1 (555) 123-4567\n' + bcolors.ENDC + '. We’ll get back to you within 24 hour')
    choose = int(input('enter 1 to return to the main menu: '))
    if choose == 1:
        menu()

def menu(): #need to finish
    print('welcome to the main menu')

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







