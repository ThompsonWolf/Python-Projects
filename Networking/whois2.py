import whois


domain = whois.whois('example.com')

# Extract and print specific details
print(f"Domain Name: {domain.domain_name}")
print(f"Registrar: {domain.registrar}")
print(f"Creation Date: {domain.creation_date}")
print(f"Expiration Date: {domain.expiration_date}")
print(f"Name Servers: {domain.name_servers}")
