from colors import bcolors
import functions
import private

#The system output:
print(bcolors.BLUEBG + 'Welcome To Hire Scope System' + bcolors.ENDC)
while not functions.is_human_check():
    continue
typ, username = functions.entrance()
print(bcolors.ENDC)
jobs_dict = functions.open_jobs_file_to_read()
users_dict = functions.open_file_to_read()
obj = users_dict[username]
if typ == 'Candidate':
    while True:
        print('Choose one of those options:')
        print('1. Enter to profile')
        print('2. View my application history')
        print('3. Advanced search')
        print('4. Get some tools')
        print('5. Try personal test')
        print('6. Help bot')
        print('7. Contact details')
        print('8. Quit')
        choice = input()
        match choice:
            case "1":
                while True:
                    print('Choose one of those options:')
                    print('1. Edit profile')
                    print('2. Delete profile')
                    print('🔙Press enter to go back')
                    num = input()
                    match num:
                        case "1":
                            private.edit_candidate_profile(username)
                            input('🔙Press enter to go back \n')
                        case "2":
                            private.delete_profile(username)
                            input('🔙Press enter to go back \n')
                        case "":
                            break
                        case _:
                            print('Invalid option. Please choose a number between 1 and 3')
            case "2":
                    print("Showing application history...")
                    input('🔙Press enter to go back \n')
            case "3":
                while True:
                    job = functions.advanced_search()
                    if job != 1 and job == True:
                        job.print_deatails()
                    print('Do you want to search job again? (Press 1)')
                    back = input('🔙Press enter to go back \n')
                    if not back:
                        break
            case "4":
                functions.candidate_tools()
            case "5":
                print("Starting personal test...")
                input('🔙Press enter to go back \n')
            case "6":
                print("Launching help bot...")
                input('🔙Press enter to go back \n')
            case "7":
                functions.contact()
                input('🔙Press enter to go back \n')
            case "8":
                print("GOODBYE 😊")
                break
            case _:
                print("Invalid option. Please choose a number between 1 and 8")
elif typ == 'Employer':
    while True:
        print('Choose one of those options:')
        print('1. Enter to profile')
        print('2. Actions in my jobs')
        print('3. Notifications')
        print('4. Contacts details')
        print('5. Quit')
        choice = input()
        match choice:
            case "1":
                while True:
                    print('Choose one of those options:')
                    print('1. Edit profile')
                    print('2. Delete profile')
                    print('🔙Press enter to go back')
                    num = input()
                    match num:
                        case "1":
                            private.edit_employer_profile(username)
                            input('🔙Press enter to go back \n')
                        case "2":
                            exit_p = private.delete_profile(username)
                            input('🔙Press enter to go back \n')
                        case "":
                            break
                        case _:
                            print('Invalid option. Please choose a number between 1 and 3')
            case "2":
                while True:
                    print('Choose one of those options:')
                    print('1. Publish a job')
                    print('2. Delete a job')
                    print('3. Update a job')
                    print('4. View my jobs')
                    print('5. Search job')
                    print('🔙Press enter to go back')
                    num = input()
                    match num:
                        case "1":
                            obj.publish_job()
                            print('The job was successfully posted')
                            input('🔙Press enter to go back \n')
                        case "2":
                            if obj.delete_job() != 1:
                                input('🔙Press enter to go back \n')
                        case "3":
                            obj.edit_job()
                            input('🔙Press enter to go back \n')
                        case "4":
                            functions.view_my_jobs(username)
                            input('🔙Press enter to go back \n')
                        case "5":
                            functions.search_jobs()
                            input('🔙Press enter to go back \n')
                        case "":
                            break
                        case _:
                            print('Invalid option. Please choose a number between 1 and 6')
            case "3":
                print('Notifications...')
                input('🔙Press enter to go back \n')
            case "4":
                functions.contact()
                input('🔙Press enter to go back \n')
            case "5":
                print('GOODBYE 😊')
                break
            case _:
                print('Invalid option. Please choose a number between 1 and 5')



