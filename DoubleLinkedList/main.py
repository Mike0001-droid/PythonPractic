class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev_obj: ObjList = self.tail.get_prev()
            prev_obj.set_next(None)
            self.tail = prev_obj

    def get_data(self):
        data_list = []
        current = self.head
        while current is not None:
            data_list.append(current.get_data())
            current = current.get_next()
        return data_list


lst = LinkedList()

lst.add_obj(ObjList("Data 1"))
lst.add_obj(ObjList("Data 2"))
lst.add_obj(ObjList("Data 3"))

lst.remove_obj()
lst.remove_obj()
lst.remove_obj()