import re
email_input = str(input("Enter the email id "))
pattern = "(\w+)@(\w+)\.(\w+)"
matched = re.match(pattern,email_input)
if matched:
    print("True")
else:
    print("False")