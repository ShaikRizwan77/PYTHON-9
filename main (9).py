char = input("Enter any character: ")
if char.isupper():
    print(f"'{char}' is an Uppercase letter.")
elif char.islower():
    print(f"'{char}' is an lowercase letter.")
elif char.isdigit():
    print(f"'{char}' is an number.")
else: 
    print(f"'{char}' is an Special character or space.")