from sys import maxsize


class Number:

    def __init__(self, nickname=None, firstname=None, lastname=None, address2=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None):
        self.nickname = nickname
        self.firstname = firstname
        self.lastname = lastname
        self.address2 = address2
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
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
