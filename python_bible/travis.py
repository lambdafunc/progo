known_users = ["Alice", "Bob", "Ciara"]
print(known_users)

while True:
    print("Hi my name is Tarvis")
    name = raw_input("Whats your name: ").strip().capitalize()

    if name in known_users:
        print("Hey {}!").format(name)
        remove = raw_input("Would you like to remove from list: (y/n)").lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)

    else:
        add = raw_input("I can't find you my list :( Would you like to be added on my list : (y/n)").lower()
        if add == "y":
            known_users.append(name)
            print(known_users)
