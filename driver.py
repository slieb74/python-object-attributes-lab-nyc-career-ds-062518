class Driver:

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first_name):
        self._first = first_name
        return self._first

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last_name):
        self._last = last_name
        return self._last

    @last.deleter
    def last(self):
        self._last = None

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating
        return self._rating

    @rating.deleter
    def rating(self):
        self._rating = None

    @property
    def miles_driven(self):
        return self._miles_driven

    @miles_driven.setter
    def miles_driven(self, miles_driven):
        self._miles_driven = miles_driven
        return self._miles_driven

    @miles_driven.deleter
    def miles_driven(self):
        self._miles_driven = None

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def greet_passenger(self):
        return "Hello! I'll be your driver today. My name is {}".format(self.fullname())
