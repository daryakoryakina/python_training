import time

from model.number import Number
from random import randrange
import re


def test_get_and_assert_random_number(app, json_numbers):
    if app.number.count() == 0:
        number = json_numbers # Number(firstname="name1", lastname="name2", nickname="name3", address2="address2",
                        # company="mycompany", address="address1", email="mail@mail", email2="mail@mail2",
                        # homephone="+123", mobilephone="234", workphone="567", secondaryphone="3456")
        app.number.create_number(number)
    old = app.number.get_number_list()
    index = randrange(len(old))
    contact_info_from_home_page = app.number.get_number_list()[index]
    contact_info_from_edit_page = app.number.get_contact_info_from_edit_page(index)
    assert contact_info_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_info_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert contact_info_from_home_page.address == contact_info_from_edit_page.address
    assert contact_info_from_home_page.all_emails == merge_emails(contact_info_from_edit_page)
    assert contact_info_from_home_page.all_phones_from_home_page == merge_phones_on_home_page(contact_info_from_edit_page)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_on_home_page(number):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [number.homephone, number.mobilephone, number.workphone,
                                        number.secondaryphone]))))


def merge_emails(number):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [number.email, number.email2]))))
