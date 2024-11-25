a = ["wel", "aba", "madam", "string"]
r = ""
for i in a:
    if i == i[::-1]:  # Check if the string is a palindrome
        r = i
        break
if r != "":
    print(r)
else:
    print("None")
