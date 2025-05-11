from colors import bcolors
import functions
import private

#The system output:
print(bcolors.UNDERLINE + bcolors.BRIGHT_MAGENTA + 'Welcome To Hire Scope System' + bcolors.ENDC)
while not functions.is_human_check():
    continue
typ, username = functions.entrance()
print(bcolors.ENDC)
jobs_dict = functions.open_jobs_file_to_read()
users_dict = functions.open_file_to_read()
obj = users_dict[username]
if typ == 'Candidate':
    while True:
        print(bcolors.CYAN + bcolors.UNDERLINE + 'Choose one of those options:' + bcolors.ENDC)
        print(bcolors.CYAN + '1.' + bcolors.ENDC + 'Enter to profile')
        print(bcolors.CYAN + '2.' + bcolors.ENDC + 'View my application history')
        print(bcolors.CYAN + '3.' + bcolors.ENDC + 'Advanced search')
        print(bcolors.CYAN + '4.' + bcolors.ENDC + 'Get some tools')
        print(bcolors.CYAN + '5.' + bcolors.ENDC + 'Try personal test')
        print(bcolors.CYAN + '6.' + bcolors.ENDC + 'Help bot')
        print(bcolors.CYAN + '7.' + bcolors.ENDC + 'Contact details')
        print(bcolors.CYAN + '8.' + bcolors.ENDC + 'Quit')
        choice = input()
        match choice:
            case "1":
                while True:
                    print(bcolors.CYAN + bcolors.UNDERLINE + 'Choose one of those options:' + bcolors.ENDC)
                    print(bcolors.CYAN + '1.' + bcolors.ENDC + 'Edit profile')
                    print(bcolors.CYAN + '2.' + bcolors.ENDC + 'Delete profile')
                    print(bcolors.CYAN + '🔙Press enter to go back' + bcolors.ENDC)
                    num = input()
                    match num:
                        case "1":
                            private.edit_candidate_profile(username)
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "2":
                            private.delete_profile(username)
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "":
                            break
                        case _:
                            print('Invalid option. Please choose a number between 1 and 3')
            case "2":
                    obj.view_my_jobs()
                    input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
            case "3":
                while True:
                    job = functions.advanced_search(obj)
                    if job != 1 and job == True:
                        job.print_deatails()
                    print('Do you want to search job again? (Press 1)')
                    back = input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                    if not back:
                        break
            case "4":
                functions.candidate_tools()
            case "5":
                print("Starting personal test...")
                input(bcolors.CYAN + '🔙Press enter to go back \n'+ bcolors.ENDC)
            case "6":
                functions.chatbot_loop()
                input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
            case "7":
                functions.contact()
                input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
            case "8":
                print(bcolors.BG_CYAN + "GOODBYE 😊" + bcolors.ENDC)
                break
            case _:
                print("Invalid option. Please choose a number between 1 and 8")
elif typ == 'Employer':
    while True:
        print(bcolors.CYAN + bcolors.UNDERLINE + 'Choose one of those options:' + bcolors.ENDC)
        print(bcolors.CYAN + '1.' + bcolors.ENDC + 'Enter to profile')
        print(bcolors.CYAN + '2.' + bcolors.ENDC + 'Actions in my jobs')
        print(bcolors.CYAN + '3.' + bcolors.ENDC + 'Notifications')
        print(bcolors.CYAN + '4.' + bcolors.ENDC + 'Contacts details')
        print(bcolors.CYAN + '5.' + bcolors.ENDC + 'Quit')
        choice = input()
        match choice:
            case "1":
                while True:
                    print(bcolors.CYAN + bcolors.UNDERLINE + 'Choose one of those options:' + bcolors.ENDC)
                    print(bcolors.CYAN + '1.' + bcolors.ENDC + 'Edit profile')
                    print(bcolors.CYAN + '2.' + bcolors.ENDC + 'Delete profile')
                    print(bcolors.CYAN + '🔙Press enter to go back' + bcolors.ENDC)
                    num = input()
                    match num:
                        case "1":
                            private.edit_employer_profile(username)
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "2":
                            exit_p = private.delete_profile(username)
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "":
                            break
                        case _:
                            print('Invalid option. Please choose a number between 1 and 3')
            case "2":
                while True:
                    print(bcolors.CYAN + bcolors.UNDERLINE + 'Choose one of those options:' + bcolors.ENDC)
                    print(bcolors.CYAN + '1.' + bcolors.ENDC + 'Publish a job')
                    print(bcolors.CYAN + '2.' + bcolors.ENDC + 'Delete a job')
                    print(bcolors.CYAN + '3.' + bcolors.ENDC + 'Update a job')
                    print(bcolors.CYAN + '4.' + bcolors.ENDC + 'View my jobs')
                    print(bcolors.CYAN + '5.' + bcolors.ENDC + 'Search job')
                    print(bcolors.CYAN +'🔙Press enter to go back' + bcolors.ENDC)
                    num = input()
                    match num:
                        case "1":
                            obj.publish_job()
                            print('The job was successfully posted')
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "2":
                            if obj.delete_job() != 1:
                                input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "3":
                            obj.edit_job()
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "4":
                            functions.view_my_jobs(username)
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "5":
                            functions.search_jobs()
                            input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
                        case "":
                            break
                        case _:
                            print('Invalid option. Please choose a number between 1 and 5')
            case "3":
                obj.messages()
                input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
            case "4":
                functions.contact()
                input(bcolors.CYAN + '🔙Press enter to go back \n' + bcolors.ENDC)
            case "5":
                print(bcolors.BG_CYAN + 'GOODBYE 😊' + bcolors.ENDC)
                break
            case _:
                print('Invalid option. Please choose a number between 1 and 5')



