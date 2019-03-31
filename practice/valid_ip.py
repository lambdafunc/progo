# # Purpose: Check if provided IP address is valid
# # Additional Installation requirement : No

ip_address = input("Please enter IP Address:")
ip = ip_address.strip()
ip_valid = True

if (not (ip.count(".") == 3)):
    ip_valid = False

else:
    octet_value = ip.split(".")
    for value in octet_value:
        value = int(value)
        if (not (0 <= value <= 255)):
            ip_valid = False

if (ip_valid):
    print("IP is Valid: {}".format(ip))
else:
    print("Invalid")

# ip_address=input("Enter IP address: ")
# #remove any extra characters
# ip_address=ip_address.strip()

# #initialize a flag to point to true for an ip address
# ip_address_flag=True

# #validate if there are only 3 dots (.) in ip address
# if (not(ip_address.count('.') == 3)):
#     ip_address_flag=False
# else:
#     #Validate if each of the octet is in range 0 - 255
#     ip_address=ip_address.split(".")
#     for val in ip_address:
#         val=int(val)
#         if (not(0 <= val <=255)):
#             ip_address_flag=False

# #based upon the flag value display the relevant message
# if (ip_address_flag):
#     print ("Given IP is correct")
# else:
#     print ("Given IP is not correct")
