from model.number import Number
import random
import string


#def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    # return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Number(firstname="", lastname="", address="", company="")] + [
    Number(firstname="firstname1", lastname="lastname1",
           address="sddress1", company="company1")
    for i in range(5)
]
