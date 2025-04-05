class User:
    def __init__(self, id, name, last_name, phone, email, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        self._password = password
        self._status = status

    # id property
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # last_name property
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    # phone property
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    # email property
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    # password property
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    # status property
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


