import pytest
# from selenium.webdriver.common.by import By
from application import Application
from group import Group
# from pages.group_page import GroupPage


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_type(app):
    app.open_page()
    app.login(username="admin")
    app.password(password="secret")
    app.open_groups()
    app.create_group(Group(group_name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    app.return_to_groups()
    app.logout()
