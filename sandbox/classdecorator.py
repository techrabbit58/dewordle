def classdecorator[T](cls: T) -> T:
    cls.num_pages = 175
    for item, value in vars(cls).items():
        print(item, '=', repr(value))
    return cls


@classdecorator
class Book:
    author: str = 'Herbert Hobel'
    title: str = 'Holzhandwerk im Wandel der Zeit'
    num_pages: int

    def get_author(self) -> str:
        return self.author


if __name__ == '__main__':
    book = Book()
    book.get_author()
