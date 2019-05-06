# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.newnum import NewNum


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.number.type_firstname(NewNum(first_name="dfggtxf", middle_name="edszertgderxde", nickname="fgxhgcfj", address2="sdfzdfgxdhgcfj"))
    app.number.click_save()
    app.session.logout()


