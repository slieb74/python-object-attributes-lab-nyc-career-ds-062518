class Passenger:

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first_name):
        self._first = first_name
        return self._first

    @first.deleter
    def first(self):
        self._first = None

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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        return self._email

    @email.deleter
    def email(self):
        self._email = None

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def yell_name(self):
        return "{}".format(self.fullname().upper())
