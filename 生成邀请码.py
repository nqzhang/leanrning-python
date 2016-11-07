import string
import random
def GenInviteCode():
    i = 0
    InviteCode = ''
    while i <= 10:
        str = random.choice(string.ascii_lowercase)
        InviteCode += str
        i += 1
        if i== 10:
            print(InviteCode)
n=0
while n <= 200:
    GenInviteCode()
    n += 1