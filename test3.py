class List:
    _name = "List"

    def __init__(self):
        self._l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(0, len(self._l)):
            if self._l[i] % 2 == 0:
                self._l[i] = self._l[i]/2
