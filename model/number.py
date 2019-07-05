from sys import maxsize


class Number:

    def __init__(self, nickname=None, firstname=None, lastname=None, address2=None, id=None,
                 all_phones_from_home_page=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, company=None, address=None,
                 email=None, email2=None, all_emails=None):
        self.nickname = nickname
        self.firstname = firstname
        self.lastname = lastname
        self.address2 = address2
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.company = company
        self.address = address
        self.email = email
        self.email2 = email2
        self.all_emails = all_emails


# стандартная функция, которая выводит на консоль для элементов id и name. почему она выглядит именно так - непонятно

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    # стандартная функция, которая обеспечивает сравненте не по расположению, а по смыслу
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id), self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
