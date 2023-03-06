from Book import Book
from Borrow import Borrow
import pickle
import re
import datetime


def ui():
    select = input(
"""#### 도서 관리 프로그램 ####
1. 책 추가
2. 책 대여
3. 책 반납
4. 전체 도서 조회
5. 도서 이름으로 도서 조회
6. 작가 이름으로 도서
7. 장르로 도서 조회
8. 전체 대여 도서 조회
9. 연체 도서 및 연체자 조회
10. 종료
입력 : """)
    return int(select)


def select_all():
    print("=====전체 도서 조회 목록=====")
    for i in book_list:
        i.print_to_str()
        print("=============================")
    print("========= 출력 종료 =========")


def select_by_name():
    string = input("검색 조건 입력 : ")
    rule = re.compile(string)
    print("=====이름 조건 조회 목록=====")
    for i in book_list:
        if rule.search(i.book_name):
            i.print_to_str()
            print("=============================")
    print("========= 출력 종료 =========")


def select_by_author():
    string = input("검색 조건 입력 : ")
    rule = re.compile(string)
    print("=====작가 조건 조회 목록=====")
    for i in book_list:
        if rule.search(i.author):
            i.print_to_str()
            print("=============================")
    print("========= 출력 종료 =========")


def select_by_genre():
    string = input("검색 조건 입력 : ")
    rule = re.compile(string)
    print("=====작가 조건 조회 목록=====")
    for i in book_list:
        if rule.search(i.genre):
            i.print_to_str()
            print("=============================")
    print("========= 출력 종료 =========")


def select_over_return_date():
    print("=====반납 지연 조회 목록=====")
    for i in borrow_list:
        if i.return_date < datetime.date.today():
            for j in book_list:
                if i.ISBN == j.ISBN:
                    print(f"ISBN : {j.ISBN}, 제목 : {j.book_name}, 연체자 : {i.borrower_name}, 연체일 : {(datetime.date.today() - i.return_date).days}일")
                    print("=============================")
    print("========= 출력 종료 =========")


def add_book():
    lst = ["ISBN", "제목", "작가", "장르", "가격"]
    temp = []
    for i in lst:
        temp += (input(f"{i} : "),)
    book_list.append(Book(temp[0], temp[1], temp[2], temp[3], temp[4]))


def borrow_book():
    lst = ["ISBN", "이용자 이름", "전화번호"]
    temp = ()
    for i in lst:
        temp += (input(f"{i} : "),)
    for i in book_list:
        if i.ISBN == temp[0] and i.borrowed == False:
            temp += (datetime.date.today(),)
            borrow_list.append(Borrow(temp[0], temp[1], temp[2], temp[3]))
            i.set_borrow(True)
            break
    else:
        print("요청하신 책이 존재하지 않거나 대출 중입니다.")
            

def return_book():
    borrower_name = input("이름을 입력해주세요 : ")
    for i in range(len(borrow_list)):
        if borrow_list[i].borrower_name == borrower_name:
            for j in book_list:
                if j.ISBN == borrow_list[i].ISBN:
                    borrow_list.pop(i)
                    j.set_borrow(False)

def select_return_book():
    print("=====전체 대여 도서 목록=====")
    for i in borrow_list:
        for j in book_list:
            if i.ISBN == j.ISBN:
                print(f"ISBN : {j.ISBN}, 제목 : {j.book_name}, 대여자 : {i.borrower_name}, 반납예정일 : {i.return_date}")
                print("=============================")
    print("========= 출력 종료 =========")

def quit():
    print("프로그램이 종료 됩니다.")
    pickle.dump(book_list, open('book_list.p','wb'))
    pickle.dump(borrow_list, open('borrow_list.p','wb'))
    exit()

try:
    book_list = pickle.load(open("book_list.p","rb"))
except:
    book_list = []
try:
    borrow_list = pickle.load(open("borrow_list.p","rb"))
except:
    borrow_list = []