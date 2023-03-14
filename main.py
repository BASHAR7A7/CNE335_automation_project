# This is the template code for the CNE335 Final Project
# Bashar
# CNE 335 Winter

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Bashar Abduljaleel")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_ip = "18.217.190.68"
    rsa_ppk = r"C:\Users\basha\Downloads\bush_bush.ppk"
    uname = 'ubuntu'

    my_aws = Server(server_ip, rsa_ppk, uname)
    # TODO - Call Ping method and print the results
    print(my_aws.ping())
    print("Updating server!")
    ssh_result = my_aws
    print(ssh_result)
