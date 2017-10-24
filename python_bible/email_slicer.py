#Ask for email address
email = raw_input("Enter email-id: ").strip()
#Slice out username
username = email[:email.index("@")]
#Slice out domain name
domainname = email[email.index("@")+1:]
#format message
output = "Username: {} \nDomain name: {}".format(username, domainname)
#display output message
print(output)
