# importing library
import requests
import subprocess

# function for scanning subdomains
def domain_scanner(domain_name, sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')

    valid_urls = []

    # loop for getting URL's
    for subdomain in sub_domnames:

        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"

        # using try catch block to avoid crash of the program
        try:
            # sending get request to the url
            requests.get(url)

            # if after putting subdomain one by one url is valid then append it to valid_urls list
            valid_urls.append(url)

        except requests.ConnectionError:
            pass

    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')

    return valid_urls

# main function
if __name__ == '__main__':
    # inputting the domain name
    dom_name = input("Enter the Domain Name:")
    print('\n')

    # opening the subdomain text file
    with open('subdomain_wordlist.txt', 'r') as file:
        # reading the file
        name = file.read()

        # using splitlines() function storing the list of splitted strings
        sub_dom = name.splitlines()

    # calling the function for scanning the subdomains and getting the urls
    valid_urls = domain_scanner(dom_name, sub_dom)

    # writing the valid urls to a file
    with open('output.txt', 'w') as output_file:
        for url in valid_urls:
            output_file.write(f'{url}\n')

    print("successfully bruted domain with python")


#----------------------------------------------------------------------------------------------------------------------
import subprocess


# Construct the nmap command with the provided options
subdomain_command = f"python pysubrute.py"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)

#----------------------------------------------------------------------------------------------------------------------

# Construct the nmap command with the provided options
subdomain_command = f"pip install -r requirements.txt"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# Construct the nmap command with the provided options
subdomain_command = f"python3 setup.py install"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)

#----------------------------------------------------------------------------------------------------------------------

# Construct the nmap command with the provided options
subdomain_command = f"python sublist3r.py -v -d wscubetech.com -b -o output_sublister.txt"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)

#----------------------------------------------------------------------------------------------------------------------

# Construct the nmap command with the provided options
subdomain_command = f"apt-get install subfinder"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)

#----------------------------------------------------------------------------------------------------------------------

# Construct the nmap command with the provided options
subdomain_command = f"subfinder -d wscubetech.com -v -o output_subfinder.txt"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)

#----------------------------------------------------------------------------------------------------------------------




