import subprocess


# Construct the nmap command with the provided options
subdomain_command = f"python subdomain.py"

# Run the nmap command
result = subprocess.run(subdomain_command, shell=True, text=True)

# Print the output of the nmap command
print(result.stdout)