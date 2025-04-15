# sha256 A function that takes a password (string) and converts it into a unique hashed value using the SHA256 algorithm.
from hashlib import sha256

def hash_password(password):

    # password.encode() → password ko bytes mein convert karta hai.
    # hexdigest() → final hashed result (hex string) return karta hai.
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    # """
    # Returns True if the hash of the password we are checking matches the one in stored_logins
    # for a specific email. Otherwise, returns False.
    # """
    if email not in stored_logins:
        return False  # agar email hi nahi mila, to login fail

    if stored_logins[email] == hash_password(password_to_check): #comparing
        return True
    return False

def main():
    # Dictionary of stored emails and their hashed passwords
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # "karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # "123!456?789"
    }

    # Test logins
    # Wo check karta hai ke kya diya gaya email + password sahi hai ya nahi.
    print(login("example@gmail.com", stored_logins, "word"))           
    print(login("example@gmail.com", stored_logins, "password"))      

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))     
    print(login("code_in_placer@cip.org", stored_logins, "karel"))    

    print(login("student@stanford.edu", stored_logins, "password"))    
    print(login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == '__main__':
    main()
