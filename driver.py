class Driver:

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        self._first = first

    @first.deleter
    def first(self):
        del self._first

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        self._last = last

    @last.deleter
    def last(self):
        del self._last

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    @rating.deleter
    def rating(self):
        del self._rating

    @property
    def miles_driven(self):
        return self._miles_driven

    @miles_driven.setter
    def miles_driven(self, miles_driven):
        self._miles_driven = miles_driven

    @miles_driven.deleter
    def miles_driven(self):
        del self._miles_driven

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def greet_passenger(self):
        return "Hello! I'll be your driver today. My name is {}".format(self.fullname())
