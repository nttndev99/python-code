username = input('What is yourname? ')
password = input('What is password? ')

password_length = len(password)
hidden_password = '*' * password_length

print(f"Hello {username}\n Your password is {hidden_password} with {password_length} letters")