import random
import string
import os.path
import getopt
import sys
import jsonpickle
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts",  "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string('firstname', 10),
                    lastname=random_string('lastname', 10),
                    address=random_string('address', 10),
                    email=random_string('email', 10),
                    email2=random_string('email2', 10),
                    email3=random_string('email3', 10),
                    mobilephone=random_digits(10),
                    homephone=random_digits(10),
                    workphone=random_digits(10),
                    secondaryphone=random_digits(10))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
