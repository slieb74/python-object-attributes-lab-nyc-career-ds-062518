class Passenger:
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
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    @email.deleter
    def email(self):
        del self._email

    def yell_name(self):
        return self._first.upper() + ' '  +  self._last.upper()
