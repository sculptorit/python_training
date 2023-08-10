import random
import string
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
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