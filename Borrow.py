import datetime

class Borrow():
    def __init__(self, *args):
        self.ISBN = args[0]
        self.borrower_name = args[1]
        self.borrower_phone_num = args[2]
        self.borrow_date = args[3]
        self.return_date = self.borrow_date + datetime.timedelta(days=7)
        