import json
import os
import sys
from classes import Candidate
from colors import bcolors
from typing import Dict, List
from itertools import zip_longest
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
                     change_password(username)
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
        try:
            choice = int(input(bcolors.CYAN + bcolors.UNDERLINE + 'choose an option:' + bcolors.ENDC + bcolors.CYAN + '\n1.' + bcolors.ENDC + 'Log in' + bcolors.CYAN + '\n2.' + bcolors.ENDC + 'Sign up\n'))
            if choice == 1:
                typ, username = log_in()
                if typ is Candidate:
                    return 'Candidate', username
                else:
                    return 'Employer', username

            elif choice == 2:
                typ, username = sign_up()
                return typ, username
            print('Invalid input, Try again')
        except ValueError:
            print('Invalid input, Try again')

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
    jobs_dict =open_jobs_file_to_read()
    if username not in jobs_dict or not jobs_dict[username]:
        print("You dont have jobs at the moment")
        return
    my_jobs = jobs_dict[username]
    while True:
        choice = input('Would you like to sort the jobs by date? (yes/ no/ press enter to skip): ')
        if choice in ['yes', 'no', '']:
            break
        print("Invalid input. Please type 'yes', 'no', or press Enter to skip.")

    if choice == 'yes':
        my_jobs = sorted(my_jobs, key=lambda job: job._date, reverse=True)

    for i, job in enumerate(my_jobs):
        print(f"Job number: {job.job_number}")
        print(f"Profession: {job.name}")
        print(f"City: {job.city}")
        print(f"Salary Range: {job.salary_range}")
        print(f"Job Type: {job.scope_job}")
        print(f"Experience Required: {job.experience}")
        print(f"Description: {job.description}")
        print(f"Date Posted: {job._date}")
        print("-" * 40)

def check_city(city):
    text = "Afula Akko Arad Ariel Ashdod Ashkelon Bnei-Brak Bat-Yam Beersheba Beit-Shean Beit-Shemesh Beitar-Illit Bnei-Ayish Dimona Eilat Elad Givat-Shmuel Giv'atayim Hadera Haifa Harish Herzliya Holon Hoshaya Jerusalem Karmiel Kfar-Saba Kiryat-Ata Kiryat-Bialik Kiryat-Gat Kiryat-Malakhi Kiryat-Motzkin Kiryat-Ono Kiryat-Shmona Kiryat-Yam Lod Ma'alot-Tarshiha Ma'ale-Adumim Migdal-HaEmek Modiin-Illit Modiin-Maccabim-Reut Nahariya Nazareth Nazareth-Illit Ness-Ziona Netanya Netivot Ofakim Or-Akiva Or-Yehuda Petah-Tikva Raanana Ramat-Gan Ramat-Hasharon Ramla Rehovot Rishon-Lezion Rosh-HaAyin Safed Sakhnin Sderot Shoham Tamra Tayibe Tel-Aviv-Jaffa Tiberias Tirat-Carmel Umm-al-Fahm Yavne Yehud-Monosson Yokneam-Illit Zefat"
    cities = text.split()
    if city in cities:
            return True
    return False

def advanced_search(user):
    filters = []
    print(bcolors.UNDERLINE + 'you have entered advanced search\n' + bcolors.ENDC)
    print('choose your filters')

    profession = input('Enter your profession (Press enter to skip): ')
    filters.append(profession if profession != '' else 'skip')
    while True:
        try:
            choose = int(input('1. full time\n2. part time '))
            filters.append('full time' if choose == 1 else 'part time')
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    city = input('Choose your preferred city (Press enter to skip): ')
    if city == '':
        filters.append('skip')
    else:
        filters.append(city)
    exp = 'skip'
    filters.append(exp)
    return search(filters, user)

def search(filters, user_):
    filtered = []
    number = 1
    jobs = open_jobs_file_to_read()

    # Ask the user if they want to sort by date
    while True:
        sort_by_date = input("Would you like to sort the results by date? (yes/no): ").strip().lower()
        if sort_by_date in ['yes', 'no']:
            break
        print('Invalid input. Type yes/no')

    for user in jobs:
        for job in jobs[user]:
            if filters[0].lower() == 'skip' or job.name.lower() == filters[0].lower():
                if job.scope_job.lower() == filters[1].lower():
                    if filters[2].lower() == 'skip' or job.city.lower() == filters[2].lower():
                        if filters[3].lower() == 'skip' or job.experience.lower() == filters[3].lower():
                            filtered.append(job)

    # Sort the filtered jobs by date if the user chose to do so
    if sort_by_date == 'yes':
        filtered.sort(key=lambda job: job._date, reverse=True)

    # Display the results
    if not filtered:
        print('Jobs not found')
        return 1
    print("-" * 40)
    for job in filtered:
        print(bcolors.CYAN + f"{number}: " + bcolors.ENDC)
        job.print_details()
        if sort_by_date == 'yes':  # Display the date if sorted by date
            print(f"Date Posted: {job._date}")
        print("-" * 40)
        number += 1

    return apply_for_job([job.job_number for job in filtered], user_)

def apply_for_job(filtered, user):
    dict_ = {}
    dict_ = open_applications_file_to_read()
    job_index = 0
    while True:
        job_index_ = input('\nChoose the job index you want to apply for(Press enter to exit): ')
        if not job_index_:
            return False
        elif int(job_index_) > len(filtered) or int(job_index_) < 1:
            print('Invalid job selection. Please choose a valid job index.')
        else:
            job_index = int(job_index_)
            break
    selected_job_number = filtered[job_index - 1]

    jobs = open_jobs_file_to_read()
    users = open_file_to_read()
    manager = job = 0

    for job_owner in jobs:
        for job_ in jobs[job_owner]:
            if job_.job_number == selected_job_number:
                manager = job_owner
                job = job_
                if hasattr(user, 'applied_jobs') and selected_job_number in user.applied_jobs:
                    print('You have already applied for this job')
                    return False
                else:
                    user.applied_jobs.append(selected_job_number)

                    # Attach the resume to the application
                    if user.resume:
                        print(f"Your resume has been attached to the application:\n{user.resume}")
                        arr = [None, job, user]
                        dict_.setdefault(manager, []).append(arr)
                        open_applications_jobs_file_to_write(dict_)

                        return True
                    else:
                        resume = input('Type your resume:\n')
                        user.resume = resume
                    print('You have successfully applied for the job')
                    #open_jobs_file_to_write(jobs)
                    open_file_to_write(users)
                    arr = [None, job, user]
                    dict_.setdefault(manager, []).append(arr)
                    open_applications_jobs_file_to_write(dict_)
                    return True

    print("Job number not found in the system.")
    return False

def contact():
    print('For technical assistance, please fill out the form below or contact us at\n' + bcolors.BG_BRIGHT_MAGENTA + 'hirescopeofficial@gmail.com' + bcolors.ENDC + '\n' + bcolors.BG_BRIGHT_MAGENTA + '+1 (555) 123-4567' + bcolors.ENDC + '\nWe’ll get back to you within 24 hour')

common_issues = {
    "1": ("I forgot my password", "To reset your password, click 'Forgot Password' on the login screen."),
    "2": ("I can't edit my profile", "Go to 'Edit Profile' from the main menu and make sure to save your changes."),
    "3": ("I can't post a job", "Make sure all required fields are filled in the 'Post Job' form, then click for Publish."),
    "4": ("I can't see candidates", "Go to 'My Jobs' and click on 'View Candidates' for the relevant job."),
    "5": (" I want to edit my company details", "Go to 'Edit Profile' from the profile menu and update your details."),
    "6": ("Other issue", "Please contact us at support@hirescope.com and we’ll assist you as soon as possible."),
}

common_issues1 = {
    "1": ("I forgot my password", "To reset your password, click 'Forgot Password' on the login screen."),
    "2": ("I can't edit my profile", "Go to 'Edit Profile' from the main menu and make sure to save your changes."),
    "3": ("I can't apply for a job", "Ensure your resume is uploaded and all required fields are filled in the application form."),
    "4": ("I can't find jobs", "Use the 'Advanced Search' feature to filter jobs by profession, location, and type."),
    "5": ("I want to update my resume", "Go to 'Edit Profile' and update your resume in the designated section."),
    "6": ("Other issue", "Please contact us at support@hirescope.com and we’ll assist you as soon as possible."),
}

def show_menu(typ):
    print(bcolors.CYAN + bcolors.UNDERLINE + "\nWelcome to the Help Bot!" + bcolors.ENDC)
    print("\nHow can we help you? Please choose a number:")
    if typ == 'Employer':
        for key, (title, _) in common_issues.items():
            print(f"{key}. {title}")
    elif typ == 'Candidate':
        for key, (title, _) in common_issues1.items():
            print(f"{key}. {title}")

def chatbot_loop(typ):
    while True:
        show_menu(typ)
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
    print(bcolors.UNDERLINE + "\nHere are some tips for writing your resume:" + bcolors.ENDC)
    for tip in tips:
        print(tip)

def view_forum():
    print("\nEnter the community forum for job seekers to consult and share tips:")
    print("Forum link: www.jobseekerforum.com")

def candidate_tools():
    while True:
        print(bcolors.CYAN + bcolors.UNDERLINE + "\nCandidate Tools:" + bcolors.ENDC)
        print(bcolors.CYAN + '1.' + bcolors.ENDC + "Get Tips for Writing Your Resume")
        print(bcolors.CYAN + '2.' + bcolors.ENDC + "View Salary Table")
        print(bcolors.CYAN + '3.' + bcolors.ENDC + "Visit Community Forum")
        print(bcolors.CYAN +'🔙Press enter to go back \n' + bcolors.ENDC)

        choice = input()
        match choice:
            case "1":
                get_resume_tips()
                input(bcolors.CYAN +'🔙Press enter to go back \n'+ bcolors.ENDC)
            case "2":
                salary_tables()
                input(bcolors.CYAN +'🔙Press enter to go back \n' + bcolors.ENDC)
            case "3":
                view_forum()
                input(bcolors.CYAN +'🔙Press enter to go back\n'+ bcolors.ENDC)
            case "":
                break
            case _:
                print("Invalid choice. Please choose 1, 2, 3, or enter.")

def search_jobs(username):
    # Read jobs from the file
    jobs = open_jobs_file_to_read()
    if not jobs:
        print("No jobs available at the moment.")
        return

    while True:
        print(bcolors.CYAN + bcolors.UNDERLINE + 'Choose an option' + bcolors.ENDC)
        print(bcolors.CYAN + "1." + bcolors.ENDC + 'Search by job number')
        print(bcolors.CYAN + "2." + bcolors.ENDC + 'Search by job characteristics')
        print(bcolors.CYAN + "3." + bcolors.ENDC + 'search by date')
        print(bcolors.CYAN + '4.' + bcolors.ENDC + 'sort by date')
        print(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
        cho = input()
        if not cho:
            return

        if cho == '1':
            job_number_filter = input("Enter job number: ").strip()
            if job_number_filter:
                for user_jobs in jobs.values():
                    for job in user_jobs:
                        if str(job.job_number) == job_number_filter:
                            print("Job found:")
                            job.print_details()
                            print("-" * 40)
                            break
                print("No job found with the given job number.")
                break
        elif cho == '2':  # Handle search by job characteristics
            filtered_jobs = []
            sys.stdin.flush()
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
            break
        elif cho == '3':
            flag = False
            date = input("Enter the date (YYYY-MM-DD): ").strip()
            if date:
                for user_jobs in jobs.values():
                    for job in user_jobs:
                        if str(job._date.date()) == date:
                            flag = True
                            print("Job found:")
                            job.print_details()
                            print("-" * 40)
            if not flag:
                print("No job found with the given date.")
            break
        elif cho == '4':
            if username not in jobs or not jobs[username]:
                print("No jobs found.")
                break
            my_jobs = jobs[username]
            my_jobs = sorted(jobs[username], key=lambda job: job._date, reverse=True)
            flag = False
            for job in my_jobs:
                flag = True
                print(f"Date Posted: {job._date.date()}")
                job.print_details()
                print("-" * 40)
            if not flag:
                print("No job found.")
            break
        print('Invalid input. Please choose 1,2,3,4 or enter.')
    sys.stdin.flush()
    p = input('Press 0 for refreshing all the jobs (enter for skip): ')
    if p == '':
        return
    if int(p) == 0:
        print_user_jobs(username)

def salary_tables():
    class JobSalarySystem:
        def __init__(self):  # Corrected constructor name
            self.salary_data = self._load_salary_data()

        def _load_salary_data(self) -> Dict[str, Dict[str, int]]:
            return {
                "Software Engineer": {"Junior": 85000, "Mid": 115000, "Senior": 145000},
                "Data Scientist": {"Junior": 90000, "Mid": 120000, "Senior": 155000},
                "UX Designer": {"Junior": 60000, "Mid": 85000, "Senior": 105000},
                "Cybersecurity Analyst": {"Junior": 85000, "Mid": 115000, "Senior": 140000},
                "AI Researcher": {"Junior": 100000, "Mid": 135000, "Senior": 170000},
                "Project Manager": {"Junior": 65000, "Mid": 90000, "Senior": 120000},
                "Mechanical Engineer": {"Junior": 60000, "Mid": 80000, "Senior": 100000},
                "Financial Analyst": {"Junior": 70000, "Mid": 90000, "Senior": 115000},
                "Doctor": {"Resident": 90000, "Attending": 140000, "Senior": 200000},
                "Nurse": {"Junior": 55000, "Mid": 70000, "Senior": 85000},
                "Graphic Designer": {"Junior": 50000, "Mid": 70000, "Senior": 90000},
                "HR Specialist": {"Junior": 50000, "Mid": 65000, "Senior": 85000},
                "Marketing Manager": {"Junior": 60000, "Mid": 85000, "Senior": 110000},
                "Legal Advisor": {"Junior": 70000, "Mid": 100000, "Senior": 130000},
                "Civil Engineer": {"Junior": 65000, "Mid": 85000, "Senior": 110000}
            }

        def _format_table(self, title: str, data: Dict[str, int]) -> List[str]:
            lines = [f"{title:<30}", "-" * 30]
            for level, salary in data.items():
                lines.append(f"{level:<18} | {salary:>9,}")
            lines.append("-" * 30)
            return lines

        def display_triple_column_salary_tables(self) -> None:
            print("\n📊 Job Salary Tables (3 per row)")
            print("=" * 105)

            professions = list(self.salary_data.items())
            for i in range(0, len(professions), 3):
                left = professions[i]
                center = professions[i + 1] if i + 1 < len(professions) else None
                right = professions[i + 2] if i + 2 < len(professions) else None

                left_lines = self._format_table(left[0], left[1])
                center_lines = self._format_table(center[0], center[1]) if center else [""] * len(left_lines)
                right_lines = self._format_table(right[0], right[1]) if right else [""] * len(left_lines)

                for l, c, r in zip_longest(left_lines, center_lines, right_lines, fillvalue=""):
                    print(f"{l:<35} {c:<35} {r}")

    system = JobSalarySystem()
    system.display_triple_column_salary_tables()

traits = {
    "analytical": 0,
    "creative": 0,
    "social": 0,
    "technical": 0,
    "practical": 0,
    "empathetic": 0
}

professions = {
    "Software Engineer": ["analytical", "technical"],
    "Graphic Designer": ["creative", "practical"],
    "Psychologist": ["empathetic", "analytical"],
    "Teacher": ["empathetic", "social"],
    "Engineer": ["technical", "practical"],
    "Writer": ["creative", "analytical"],
    "Salesperson": ["social", "practical"]
}

questions = [
    {
        "text": "You enjoy solving puzzles and logical problems.",
        "trait": "analytical"
    },
    {
        "text": "You like creating art, music, or stories.",
        "trait": "creative"
    },
    {
        "text": "You prefer working with others and communicating ideas.",
        "trait": "social"
    },
    {
        "text": "You enjoy working with machines or coding.",
        "trait": "technical"
    },
    {
        "text": "You like building or fixing things with your hands.",
        "trait": "practical"
    },
    {
        "text": "You often empathize deeply with others' emotions.",
        "trait": "empathetic"
    },
    {
        "text": "You enjoy planning and organizing complex tasks.",
        "trait": "analytical"
    },
    {
        "text": "You are energized by thinking outside the box.",
        "trait": "creative"
    },
    {
        "text": "You feel fulfilled when helping people directly.",
        "trait": "empathetic"
    },
    {
        "text": "You are drawn to teaching or explaining ideas to others.",
        "trait": "social"
    }
]

def ask_questions(username):
    print(bcolors.CYAN + bcolors.UNDERLINE + "\nWelcome to the Personal Profession Finder!\n" + bcolors.ENDC)
    while True:
        choose = input('would you like to see the last results? (yes/no): ')
        if choose.lower() in ['yes', 'no']:
            break
        print('Invalid input. Please type "yes" or "no".')
    if choose.lower() == 'yes':
        users = open_file_to_read()
        if username in users and isinstance(users[username], Candidate):
            candidate = users[username]
            if candidate.personality_test_results:
                print("Your last results:")
                for trait, score in candidate.personality_test_results.items():
                    print(f"{trait.capitalize()}: {score}")
            else:
                print("No previous results found.")
        else:
            print("Candidate not found.")
        return 0
    for i, q in enumerate(questions, 1):
        while True:
            try:
                answer = int(input(f"{i}. {q['text']} (1=Strongly Disagree ... 5=Strongly Agree): "))
                if 1 <= answer <= 5:
                    traits[q["trait"]] += answer
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def calculate_best_profession():
    scores = {}
    for job, job_traits in professions.items():
        score = sum([traits[trait] for trait in job_traits])
        scores[job] = score

    best_match = max(scores, key=scores.get)
    return best_match, scores

def show_result(username):
    best, scores = calculate_best_profession()
    print("\n--- Your Recommended Profession ---")
    print(f"🏆 {best}\n")
    print("Other profession scores:")
    for job, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{job}: {score}")
    users = open_file_to_read()
    if username in users and isinstance(users[username], Candidate):
        candidate = users[username]
        candidate.personality_test_results = {"best_profession": best}
        open_file_to_write(users)
    while True:
        choice = input('would you like to take the test again? (yes/no): ')
        if choice.lower() in ['yes', 'no']:
            break
        print('Invalid input. Please type "yes" or "no".')
    if choice.lower() == 'yes':
        ask_questions(username)
        show_result(username)

def change_password(username):
    users = open_file_to_read()
    print(bcolors.UNDERLINE + "\nVerify details:" + bcolors.ENDC)
    username_ = input("Enter your username: ")

    if username_ != username:
        print("Error!\n")
        return
    current_age = users[username].age
    age = input("Enter your age: ")
    if int(age) != current_age:
        print("Error!\n")
        return
    user = users[username]
    while True:
        new_password = input("Enter new password: ")
        if len(new_password) < 8 or not(any(c.isupper() or c.lower() for c in new_password)):
            print('The password is not strong enough(at least 8 characters and one letter)')
        else:
            break
    confirm_password = input("Confirm your new password: ")

    if confirm_password != new_password:
        print('Error! those two passwords are not equal\n')
        return
    user.password = new_password
    users[username] = user
    open_file_to_write(users)

    print("Password changed successfully.")

def edit_employer_profile(username):
    users = open_file_to_read()

    if username not in users or not isinstance(users[username], classes.Employer):
        print("Employer not found.")
        return

    employer = users[username]

    print("Current full name:", employer.full_name)
    new_name = input("Enter new full name (press Enter to keep current): ")
    if new_name:
        employer.full_name = new_name

    print("Current age:", employer.age)
    try:
        new_age = input("Enter new age (press Enter to keep current): ")
        if new_age:
            employer.age = int(new_age)
    except ValueError:
        print("Invalid age input. Keeping current age.")

    company = input('Enter your company details (press Enter to keep current): ')
    if company:
        employer.company_description = company

    print("Current password:", employer.password)
    while True:
        password = input("Enter new password. At least 8 characters and one letter(press Enter to keep current): ")
        if not password:
            break
        if len(password) >=8 and any(c.isalpha() for c in password):
            employer.password = password
            break
    while True:
        save = input('Do you want to save the changes? (yes/no): ')
        if save.lower() in ['yes', 'no']:
            break
        print( 'Invalid input. Please type "yes" or "no".')
    if save.lower() == 'yes':
        users[username] = employer
        open_file_to_write(users)
        print("Employer profile updated successfully.")
    else:
        print("Changes not saved.")

def delete_profile(username):
    users = open_file_to_read()
    jobs = open_jobs_file_to_read()

    if username not in users:
        print("User not found.")
        return False

    confirmation = input(f"Are you sure you want to delete the profile for '{username}'? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Profile deletion cancelled.")
        return False

    del users[username]
    open_file_to_write(users)
    if username in jobs:
        del jobs[username]
        open_jobs_file_to_write(jobs)
    print(f"Profile for '{username}' has been deleted.")
    return exit()

def edit_candidate_profile(username):
    users = open_file_to_read()

    if username not in users or not isinstance(users[username], classes.Candidate):
        print("Candidate not found.")
        return

    candidate = users[username]

    print("Current full name:", candidate.full_name)
    new_name = input("Enter new full name (press Enter to keep current): ")
    if new_name:
        candidate.full_name = new_name

    print("Current age:", candidate.age)
    try:
        new_age = input("Enter new age (press Enter to keep current): ")
        if new_age:
            candidate.age = int(new_age)
    except ValueError:
        print("Invalid age input. Keeping current age.")

    print("Current password:", candidate.password)
    while True:
        password = input("Enter new password. At least 8 characters and one letter(press Enter to keep current): ")
        if not password:
            break
        if len(password) >=8 and any(c.isalpha() for c in password):
            candidate.password = password
            break

    users[username] = candidate
    open_file_to_write(users)
    print("Candidate profile updated successfully.")

def print_user_jobs(username):
    """
    Prints all the jobs available for a specific user.
    :param username: The username of the user whose jobs are to be printed.
    """
    jobs_dict = open_jobs_file_to_read()  # Read the jobs from the file

    if username not in jobs_dict or not jobs_dict[username]:
        print(f"No jobs available for the user '{username}'.")
        return

    print(f"Jobs for user '{username}':")
    print("-" * 40)
    for job in jobs_dict[username]:
        job.print_details()
        print("-" * 40)