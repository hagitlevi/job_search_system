from colors import bcolors
import functions

#The system output:
print(bcolors.BLUEBG + 'Welcome To Search Job System' + bcolors.ENDC)
typ, username = functions.entrance()
jobs_dict = functions.open_jobs_file_to_read()
users_dict = functions.open_file_to_read()
