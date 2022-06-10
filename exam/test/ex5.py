def book_in_lib(book, author, lib):
    for author in lib: 
        if book in lib:
            print('Книга есть в библиотеке')

book = 'Гарри Поттер'
lib = {'Д.Остин': ['Гордость и предубеждение', 'Нортенгерское аббатство'],   
       'В.Гюго': ['Отверженные', 'Человек, который смеётся']} 

book_in_lib(book, lib)