
class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

# стандартная функция, которая выводит на консоль для элементов id и name. почему она выглядит именно так - непонятно
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

# стандартная функция, которая обеспечивает сравненте не по расположению, а по смыслу
    def __eq__(self, other):
        return self.id == other.id, self.name == other.name











