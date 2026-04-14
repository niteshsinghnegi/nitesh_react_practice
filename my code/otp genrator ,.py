#otp genrator in python

import random

def generate_otp(length=4):
    if length <= 0:
        raise ValueError("OTP length must be positive")

    otp = ''.join([str(random.randint(0, 9)) for i in range(length)])
    return otp

otp = generate_otp()
print("Your OTP is:", otp)


def my_genrator():
    for i in range(6):
        yield i 
gen=my_genrator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)



names = ["Nitesh", "sumit", "daksh","ansh"]
print(len(names))










