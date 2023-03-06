from func import *
menu = [add_book, borrow_book, return_book, select_all, select_by_name, select_by_author,\
            select_by_genre, select_return_book, select_over_return_date, quit]

def main():
    while True:
        select = ui()
        if 0 >= select or select > 10:
            print("잘못입력되었습니다.\n입력은 1~10까지만 기능이있습니다.")
            continue
        else:
            menu[select - 1]()

if __name__ == "__main__":
    main()