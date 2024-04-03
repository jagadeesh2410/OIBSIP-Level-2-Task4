import bcrypt

class Style:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def user_registration():
    print(Style.BOLD + "\n=== Register ===" + Style.RESET)
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = hash_password(password)

def user_login():
    print(Style.BOLD + "\n=== Login ===" + Style.RESET)
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
        print(Style.GREEN + "Login successful!" + Style.RESET)
        return True
    else:
        print(Style.RED + "Incorrect username or password." + Style.RESET)
        return False

def secured_page():
    if user_authenticated:
        print(Style.BOLD + "\nWelcome to the secured page!" + Style.RESET)
    else:
        print(Style.RED + "\nAccess denied. Please login." + Style.RESET)

if __name__ == "__main__":
    users = {}
    user_registration()
    user_authenticated = user_login()
    secured_page()
