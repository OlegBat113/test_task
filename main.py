from typing import Dict, Union, Tuple
 
 # id (уникальный идентификатор, генерируется автоматически)
# title (название книги)
# author (автор книги)
# year (год издания)
# status (статус книги: “в наличии”, “выдана”)


books = {}                              # Глобальная библиотека книг

class TBook:
    # базовый класс для всех Книг
    idBook:int = 0                      # Глобальный счётчик
    def __init__(self, title:str, author:str, year:int):
        TBook.idBook += 1            
        self.id = self.idBook           # уникальный идентификатор, генерируется автоматически
        self.title = title              # название книги 
        self.author = author            # автор книги
        self.year = year                # год издания
        self.status = "в наличии"       # статус книги: “в наличии”, “выдана”

    
def add_book(title:Union[str,None]=None, author:Union[str,None]=None, year:Union[str,None]=None) -> Tuple[Union[TBook,None], bool]:
    """Добавление книги: Пользователь вводит title, author и year"""

    print(f"\n-----\nДобавление книги в библиотеку:\n - Название: '{title}'\n - Автор: '{author}'\n - Год издания: {year}")

    bError = False
    if (title is None):
        bError = True
    else:
        title = title.strip()
        if (len(title) == 0):
            bError = True
    if bError:
        print(f"Error: Не могу добавить книгу в библиотеку, т.к. Название книги не определено.")
        return (None, False)

    bError = False
    if (author is None):
        bError = True
    else:
        author = author.strip()
        if (len(author) == 0):
            bError = True
    if bError:
        print(f"Error: Не могу добавить книгу в библиотеку, т.к. Автор книги не определен.")
        return (None, False)

    bError = False
    if (year is None):
        bError = True
    else:
        try:
            year = int(year)
        except Exception as e:
            bError = True
            print(f"Error: Год издания не определён. Исключение: {e}")
    if bError:
        print(f"Error: Не могу добавить книгу в библиотеку, т.к. Год издания книги не определен.")
        return (None, False)

    b = TBook(title, author, year)

    # Добавление книги в библиотеку
    books[b.id] = b
    #print(f"Книга добавлена в библиотеку. Идентификатор id = {b.id}")
    return (b, True)


def del_book(id: Union[int, None]) -> bool:
    """Удаление книги из библиотеки: Пользователь вводит id книги, которую нужно удалить."""

    print(f"\n-----\nУдаление книги с Идентификатором ({id}) из библиотеки ...")

    if (id is None):
        print(f"Error: Не согу удалить книгу - Идентификатор книги не определён.")
        return False

    try:
        id = int(id)
    except Exception as e:
        print(f"Error: Не согу удалить книгу - Идентификатор книги - не определён. Исключение: '{e}'")
        return False


    if id in books:
        # Удаление книги из библиотеки
        # print(f"Книга с Идентификатором (id={id}) удалена из библиотеки.")
        del books[id]
        return True
    else:
        print(f"Error: Не могу найти в библиотеке книгу  с Идентификатором ({id}).")
        return False


def get_book(title:Union[None, str]=None, author:Union[None, str]=None, year:Union[None, int]=None) -> (Union[TBook, None], bool):
    """Поиск книги: Пользователь может искать книги по title, author или year."""

    print(f"\n-----\nПоиск книги по названию, автору или году издания в библиотеке ...")
    print(f" - Название книги: '{title}'")
    print(f" - Автор книги: '{author}'")
    print(f" - Год издания книги: {year}")

    bSearchTitle = False
    bSearchAuthor = False
    bSearchYear = False

    if not(title is None):
        title = str(title).strip()
        if len(title)>0:
            bSearchTitle = True

    if not(author is None):
        author = str(author).strip()
        if len(author)>0:
            bSearchAuthor = True
            
    if not(year is None):
        try:
            year = int(year)
            bSearchYear = True
        except Exception as e:
            print(f"Error: Год издания не определён. Исключение: '{e}'")
            return(None, False)

    if not (bSearchTitle or bSearchAuthor or bSearchYear):     
        print(f"Error: Условия поиска книги в библиотеке не определены.")
        return(None, False)

    for key in books:
        #print(f"key = {key}")
        bFindTitle = False
        bFindAuthor = False
        bFindYear = False

        if bSearchTitle:
            if books[key].title == title:
                # Нашли
                bFindTitle = True
        else:
            bFindTitle = True

        if bSearchAuthor:
            bFind = False
            if books[key].author == author:
                # Нашли
                bFindAuthor = True
        else:
            bFindAuthor = True
            
        if bSearchYear:
            bFind = False
            if books[key].year == year:
                # Нашли
                bFindYear = True
        else:
            bFindYear = True


        if bFindTitle and bFindAuthor and bFindYear:
            bFind = True
            break

    if bFind:
        # Нашли нужную книжку
        #print(f"Книга в библиотеке найдена.")
        b = books[key]
        return (books[key], True)
    else:
        # Не нашли
        print(f"Error: По условиям поиска книга в библиотеке не найдена.")
        return (None, False)


def print_one(book: TBook):
    """Вывод данных книги"""
    print(f"Данные книги:")
    print(f" - Идентификатор книги: {book.id}")
    print(f" - Название книги: '{book.title}'")
    print(f" - Автор книги: '{book.author}'")
    print(f" - Год издания книги: {book.year}")
    print(f" - Статус книги: '{book.status}'")


def print_all():
    """Отображение всех книг в библиотеке: Приложение выводит список всех книг с их id, title, author, year и status."""
    
    print(f"\n-----\nКоличество книг в библиотеке - {len(books)}.\n\nСписок всех книг в библиотеке:")
    print("-------------")
    for key in books:
        b = books[key]
        print_one(book=b)
        print("-------------")


def change_status(id:Union[int, None], status:Union[str, None]) -> (Union[TBook, None], bool):
    """Изменение статуса книги в библиотеке: Пользователь вводит id книги и новый статус ('в наличии' или 'выдана')"""
    
    print(f"\n-----\nИзменение статуса книг с Идентификатором ({id}) в библиотеке. Новый Статус - '{status}'")

    if id is None:
        print("Error: Идентификатор книги не определён.")
        return None, False
    else:
        try:
            id = int(id)
        except Exception as e:
            print(f"Error: Идентификатор книги не определён. Исключение: '{e}'")
            return None, False

    if status is None:
        print("Error: Название Статуса не определено.")
        return None, False
    else:
        status = str(status).strip()
        if len(status) == 0:
            print("Error: Название Статуса не определено.")
            return None, False
        else:
            if (status != "в наличии") and (status != "выдана"):
                print("Error: Имя Статуса для изменения - не верно.")
                return None, False

    if id in books:
        books[id].status = status
        # print(f"Книга с Идентификатором ({id}) найдена. Новый статус книги - '{status}'")
        return books[id], True
    else:
        print(f"Error: Не могу найти книгу в библиотеке с Идентификатором id = {id} для смены статуса.")
        return False


def main():
    """Консольное приложение для управления библиотекой книг"""
    
    print(f"Консольное Приложение для рабты с библиотекой книг, которое позволяет добавлять, удалять, искать и отображать книги.")

    while True:
        print("\n------------------")
        print("1 - Добавить книгу в библиотеку.")
        print("2 - Удалить книгу из библиотеки.")
        print("3 - Поиск книги в библиотеке.")
        print("4 - Отобразить все книги в библиотеке.")
        print("5 - Изменить статус книги в библиотеке.")
        print("0 - Выйти из Приложения.")
        action = input(f"Выберите действие: ")

        match action:
            case "0":
                print("Выход из Приложения ...\n")
                break
            case "1":
                """Добавление книги в библиотеку"""
                
                title = input(f" Ввнедите название книги (0 - отменить): ")
                if title == "0":
                    continue
                
                author = input(f" Ввнедите автора книги (0 - отменить): ")
                if author == "0":
                    continue

                bYearInput = False
                while True:
                    year = input(f" Ввнедите год издания книги (число, 0 - отменить): ")
                    if len(year.strip()) == 0:
                        continue
                    try:
                        year = int(year)
                    except Exception as e:
                        print("Error: Ошибка ввода года издания книги. Исключение: {e}")
                    if year == 0:
                        break
                    if year < 0:
                        print("Error: Год издания не может быть отрицательным.")
                    else:
                        bYearInput = True
                        break

                if bYearInput:
                    book, bAdd = add_book(title=title, author=author, year=year)  
                    if bAdd:
                        print(f"Книга добавлена в библиотеку.")
                        print_one(book=book)
            
            case "2":
                """Удаление книги из библиотеки"""
                id = input(f" Введите Идентификатор книги. (число, 0 - отменить): ")
                id = id.strip()
                if id == '0':
                    continue
                try:
                    id = int(id)
                    bDelInput = True
                except Exception as e:
                    print(f"Error: ошибка ввода Идентификатора книги. Исключение: {e}")
                    continue

                bDel = del_book(id)
                if bDel:
                    print(f"Книга с Идентификатором ({id}) удалена из библиотеки.")
            
            case "3":
                """Поиск книги в библиотеке"""

                title = input(f" Введите название книги (0 - отменить): ")
                title = title.strip()
                if title == "0":
                    continue

                author = input(f" Введите автора книги (0 - отменить): ")
                author = author.strip()
                if author == "0":
                    continue

                year = input(f" Введите год издания книги (число, 0 - отменить): ")
                year = year.strip()
                if year == "0":
                    continue
                if len(year) == 0:
                    year = None
                else:
                    try:
                        year = int(year)
                    except Exception as e:
                        print(f"Error: не верный год издания книги. Исключение: {e}")
                        continue
                    if year<0:
                        print(f"Error: Год издания не может быть отрицательным.")
                        continue

                (book, bFind) = get_book(title=title, author=author, year=year)
                if bFind:
                    print(f"Книга по условиям поиска в библиотеке найдена.")
                    print_one(book=book)

            case "4":
                """Отображение всех книг в библиотеке."""
                print_all()

            case "5":
                """Изменение статуса книги: (“в наличии” или “выдана”)"""

                id = input(f" Введите Идентификатор книги. (число, 0 - отменить): ")
                id = id.strip()
                if id == "0":
                    continue

                try:
                    id = int(id)
                except Exception as e:
                    print(f"Error: ошибка ввода Идентификатора книги. Исключение: {e}")

                aStatus = ("в наличии", "выдана")
                status = None
                c = input(f" Введите новый статус книги (1 - 'в наличии', 2 - 'выдана',  0 - отменить): ")
                c = c.strip()
                if c == "0":
                    continue
                elif c == "1":
                    status = aStatus[0]
                elif c == "2":
                    status = aStatus[1]
                
                if not(status is None):
                    book, bStatus = change_status(id, status)
                    if bStatus:
                        print(f"Статус книги с Идентификатором ({id}) - изменён.")
                        print_one(book=book)


if __name__ == '__main__':
    main()
