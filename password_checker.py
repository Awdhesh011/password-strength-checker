from getpass import getpass
password = getpass("Enter your password: ")
if len(password) >= 8:
    print("Password length is good.")

else:
     print("Password is too  short.")

has_number = False

for char in password:
        if char.isdigit():
            has_number = True
            break

        if has_number:
            print("number found")
        else:
                print("no number found")
                special_characters = "!@#$%^&*"
                has_special = False
                for char in password:
                    if char in special_characters:
                        has_special = True
                        break
                if has_special:
                    print("Special character found")
                else:
                    print("No special character found")
                has_upper = False
                has_lower = False
                for char in password:
                    if char.isupper():
                        has_upper = True
                    elif char.islower():
                        has_lower = True
                if has_upper:
                    print("Uppercase found")
                else:
                    print("No uppercase found")
                if has_lower:
                    print("Lowercase found")
                else:
                    print("No lowercase found")
if len(password) >= 8 and  has_number and has_upper and   has_lower:
     print("Password strength: STRONG.")
else:
     print("Password strength: WEAK.")