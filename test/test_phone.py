from model.number import Number
import re


def test_phone_on_home_page(app):
    contact_from_home_page = app.number.get_number_list()[0]
    contact_from_edit_page = app.number.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)


def test_phone_on_contact_view_page(app):
    contact_from_view_page = app.number.get_number_from_view_page(0)
    contact_from_edit_page = app.number.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone

def clear(s):
    return re.sub("[() -]", "", s)





