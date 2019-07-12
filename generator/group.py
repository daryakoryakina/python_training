import json
import os
import random
import string
import getopt
import sys
from model.group import Group


# генератор случайных данных

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
out = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", out)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

#normal_data = [
#  Group(name="groupname", header="groupheader", footer="groupfooter"),
# Group(name="groupname1", header="groupheader1", footer="groupfooter1")
# ]
