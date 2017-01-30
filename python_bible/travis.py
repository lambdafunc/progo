known_users = ["Alice", "Bob", "Ciara"]
print(len(known_users))

while True:
    print("Hi my name is Tarvis")
    name = raw_input("Whats your name: ").strip().capitalize()

    if name in known_users:
        print("Name Recognized")
    else:
        print("I dont know you")
