from sys import maxsize


class Number:

    def __init__(self, second_name=None, nickname=None, first_name=None, middle_name=None, address2=None, id=None):
        self.second_name = second_name
        self.nickname = nickname
        self.first_name = first_name
        self.middle_name = middle_name
        self.address2 = address2
        self.id = id

# стандартная функция, которая выводит на консоль для элементов id и name. почему она выглядит именно так - непонятно
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.second_name)

# стандартная функция, которая обеспечивает сравненте не по расположению, а по смыслу
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id), self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize