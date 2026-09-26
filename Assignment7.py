import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}'
    return re.findall(pattern, text)


text = input("Enter a text containing email addresses: ")

emails = find_emails(text)

if emails:
    print("\nEmail addresses found:")
    for email in emails:
        print(email)
else:
    print("\nNo email addresses found.")
