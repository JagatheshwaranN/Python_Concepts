class YoungException(Exception):
    def __init__(self, msg):
        self.msg = msg


class OldException(Exception):
    def __init__(self, msg):
        self.msg = msg


age = int(input("Enter your age : "))
if age > 60:
    raise OldException("You have crossed the marriage age")
elif age < 18:
    raise YoungException("You have not reached the marriage age")
else:
    print("You are eligible for marriage")
