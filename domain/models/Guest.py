import User
class Guest(User):
    def __init__(self, id, name, last_name, phone, email, password, status,
                 check_in_date, check_out_date, room_number, reservation_id):
        super().__init__(id, name, last_name, phone, email, password, status)
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._room_number = room_number
        self._reservation_id = reservation_id

    @property
    def check_in_date(self):
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date):
        self._check_in_date = check_in_date

    # check_out_date property
    @property
    def check_out_date(self):
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date):
        self._check_out_date = check_out_date

    # room_number property
    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, room_number):
        self._room_number = room_number

    # reservation_id property
    @property
    def reservation_id(self):
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self._reservation_id = reservation_id
