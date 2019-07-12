from model.number import Number
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Number(firstname="", lastname="", address="", company="")] + [
    Number(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
           address=random_string("sddress", 20), company=random_string("company", 15))
    for i in range(5)
]
