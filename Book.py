class Book():
    def __init__(self, *args):
        self.ISBN = args[0]
        self.book_name = args[1]
        self.author = args[2]
        self.genre = args[3]
        self.price = int(args[4])
        self.borrowed = False

    def print_to_str(self):
        print(f"ISBN : {self.ISBN}, 제목 : {self.book_name}, 작가 : {self.author}, \
장르 : {self.genre}, 가격 : {self.price}, 현재 대여여부 : {self.borrowed}")
        
    def set_borrow(self, bool):
        self.borrowed = bool