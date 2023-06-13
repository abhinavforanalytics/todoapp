password = input("Enter the password: ")

result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
# to check if there's atleast 1 digit
result['digits'] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result['uppercase'] = upper
print(result)
if all(result):     # returns true even if one condition is true under result list
    print("Strong Password")
else:
    print("Weak Password")
