
def test_delete_first_group(app):
    app.open_page()
    app.group.click_to_first_group()
    app.group.delete_first_group()
    app.group.return_to_groups()


