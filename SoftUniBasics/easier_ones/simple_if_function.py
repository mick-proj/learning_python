def request_user_id():
    while True:
        user_id = input("Enter your user id: ")
        if user_id == "12345":
            print("Welcome, Miro!")
            break
        else:
            print("Incorrect ID!\nTry again.")
request_user_id()