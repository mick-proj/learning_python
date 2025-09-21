def guess_the_password():
    while True:
        password = str(input("Enter your password: "))
        correct_password = "s3cr3t!P@ssw0rd"
        if password == correct_password:
            print("Welcome, Miro.")
            break;
        else:
            print("Try again")
guess_the_password()