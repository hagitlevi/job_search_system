import json
import os
import private
from classes import Candidate
from colors import bcolors
import pickle
import classes
import random
def open_applications_file_to_read():
    dictionary = {}
    if not os.path.exists("applications.txt"):
        with open("applications.txt", "wb") as f:
            return dictionary
    try:
        with open("applications.txt", "rb") as f:
            dictionary = pickle.load(f)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error with opening the file {e}')
    return dictionary

def open_applications_jobs_file_to_write(dictionary):
    try:
        with open("applications.txt", "wb") as f:
            pickle.dump(dictionary, f)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error with opening the file {e}')
    return

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
    if not os.path.exists("users.txt"):
        with open("users.txt", "wb") as f:
            return dictionary
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
    if not os.path.exists("jobs.txt"):
        with open("jobs.txt", "wb") as f:
            pickle.dump(dictionary, f)
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
                password = strong_password()
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
                print('Wrong password! Press Enter to try again')
                num = input('Forgot password? (Press 1): ').strip()
                if num == '1':  # Compare as a string
                    private.change_password(username)
                elif num == '':
                    continue  # Restart the loop to re-enter the password
            else:
                return type(user), username
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
    while True:
        try:
            choose = int(input('1. full time\n2. part time: '))
            filters.append('full time' if choose == 1 else 'part time')
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    city = input('Choose your preferred city (or type "skip"): ')
    if city.lower() == 'skip' or city == '2':
        filters.append('skip')
    else:
        #while not check_city(city):
            #city = input(bcolors.FAIL + 'City not found. Please try again: ' + bcolors.ENDC)
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
        return 1
    return apply_for_job(filtered)

def apply_for_job(filtered):
    job_index = 0
    while True:
        job_index_ = input('Choose the job number you want to apply for(Press enter to exit): ')
        if not job_index_:
            return False
        elif int(job_index_) > len(filtered) or int(job_index_) < 1:
            print('Invalid job selection. Please choose a valid job number.')
        else:
            job_index = int(job_index_)
            break
    selected_job_number = filtered[job_index - 1]

    jobs = open_jobs_file_to_read()
    users = open_file_to_read()
    manager = job = 0


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
                manager = job_owner
                job = job_
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
                        return True
                    else:
                        resume = input('Type your resume:\n')
                        user.resume = resume
                    print('You have successfully applied for the job')
                    #open_jobs_file_to_write(jobs)
                    open_file_to_write(users)
                    dict_ = {}
                    dict_ = open_applications_file_to_read()
                    arr = [None, job, user]
                    dict_.setdefault(manager, []).append(arr)
                    open_applications_jobs_file_to_write(dict_)
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
        if len(password) >=8 and any(c.isupper() or c.lower() for c in password):
            return password
        print('The password is not strong enough(at least 8 characters and one letter)')

def view_submission_history(username):
    """
    Displays the submission history of a candidate.
    :param username: candidate's username
    """
    if not os.path.exists("jobs.pkl"):
        print("No job data found.")
        return

    with open("jobs.pkl", "rb") as f:
        try:
            all_jobs = pickle.load(f)
        except EOFError:
            print("No job data found.")
            return

    submissions = []
    for job in all_jobs:
        for candidate in job.applicants:
            if candidate.username == username:
                submissions.append((job.title, job.company_name))

    if not submissions:
        print("You have not submitted any job applications yet.")
    else:
        print("Your submission history:")
        for i, (title, company) in enumerate(submissions, 1):
            print(f"{i}. {title} at {company}")

def check_candidate_messages():
    forum_file = "forum.pkl"

    if not os.path.exists(forum_file):
        print("No forum messages found.")
        return

    with open(forum_file, "rb") as file:
        try:
            messages = pickle.load(file)
        except EOFError:
            print("Forum is currently empty.")
            return

    if not messages:
        print("Forum is currently empty.")
    else:
        print("Candidate Forum Messages")
        for idx, message in enumerate(messages, start=1):
            print(f"{idx}. {message}")

def get_resume_tips():
    tips = [
        "1. Use clear and concise language to describe your skills and experience.",
        "2. Tailor your resume to the job you're applying for by highlighting relevant skills.",
        "3. Include quantifiable achievements (e.g., 'increased sales by 20%').",
        "4. Keep the layout clean, with a clear hierarchy of information.",
        "5. Proofread your resume to avoid any grammatical or spelling errors."
    ]
    print("\nHere are some tips for writing your resume:")
    for tip in tips:
        print(tip)

def view_salary_table():
    salary_table = {
        "Software Developer": "80,000 - 120,000 USD",
        "Data Scientist": "70,000 - 110,000 USD",
        "Project Manager": "60,000 - 100,000 USD",
        "UX Designer": "50,000 - 85,000 USD"
    }
    print("\nSalary Range for Various Jobs:")
    for job, salary in salary_table.items():
        print(f"{job}: {salary}")

def view_forum():
    print("\nEnter the community forum for job seekers to consult and share tips:")
    print("Forum link: www.jobseekerforum.com")

def candidate_tools():
    while True:
        print("\nCandidate Tools:")
        print("1. Get Tips for Writing Your Resume")
        print("2. View Salary Table")
        print("3. Visit Community Forum")
        print("4. 🔙Back")

        choice = input()
        match choice:
            case "1":
                get_resume_tips()
                input('🔙Press enter to go back \n')
            case "2":
                view_salary_table()
                input('🔙Press enter to go back \n')
            case "3":
                view_forum()
                input('🔙Press enter to go back \n')
            case "4":
                break
            case _:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

def search_jobs():
    # Read jobs from the file
    jobs = open_jobs_file_to_read()
    if not jobs:
        print("No jobs available at the moment.")
        return

    # Ask for job number first
    job_number_filter = input("Enter job number (or press Enter to skip): ").strip()
    if job_number_filter:
        for user_jobs in jobs.values():
            for job in user_jobs:
                if str(job.job_number) == job_number_filter:
                    print("Job found:")
                    job.print_details()
                    print("-" * 40)
                    return
        print("No job found with the given job number.")
        return

    # Proceed to other filters if no job number is provided
    filtered_jobs = []
    profession = input("Enter your profession (or press Enter to skip): ").strip()
    while True:
        scope = input("Enter job type (1 for Full-time, 2 for Part-time, or press Enter to skip): ").strip()
        if scope in ("1", "2", ""):
            break
        print("Invalid input. Please enter 1, 2, or press Enter to skip.")
    city = input("Enter your preferred city (or press Enter to skip): ").strip()

    # Convert inputs to required types
    scope = "full time" if scope == "1" else "part time" if scope == "2" else None

    # Search for jobs matching the criteria
    job_number = 1
    for user_jobs in jobs.values():
        for job in user_jobs:
            if (not profession or job.name == profession) and \
                    (scope is None or job.scope_job == scope) and \
                    (not city or job.city == city):
                filtered_jobs.append(job)
                print(f"Job {job_number}:")
                job.print_details()
                print("-" * 40)
                job_number += 1

    if not filtered_jobs:
        print("No jobs found matching your criteria.")