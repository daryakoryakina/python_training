import random
import string
from model.group import Group

testdata = [
    Group(name="groupname", header="groupheader", footer="groupfooter"),
    Group(name="groupname1", header="groupheader1", footer="groupfooter1")
]

# генератор случайных данных

# def random_string(prefix, maxlen):
# symbols = string.ascii_letters + string.digits + string.punctuation + "" * 10
# return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [Group(name="", header="", footer="")] + [
# Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 20))
# for i in range(5)
# ]
