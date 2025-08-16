s = input()
a = s[-3 : :]
if a.lower() == ".py":
    print("yes")
else:
    print("no")