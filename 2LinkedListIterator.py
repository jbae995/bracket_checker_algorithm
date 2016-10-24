from NodeDLL import NodeDLL


class LinkedListIterator:
    def __init__(self, head):
        self.__current = head

    def __next__(self):
        if self.__current.get_data() == None:
            raise StopIteration
        else:
            item = self.__current.get_data()
            self.__current = self.__current.get_next()
            return item
