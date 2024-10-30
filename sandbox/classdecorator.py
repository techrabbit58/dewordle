def dto[T](cls: T) -> T:
    args, obj_vars = [], []
    for attr, type_ in cls.__annotations__.items():
        obj_vars.append(f'    self.{attr} = {attr}\n')
        args.append(f'{attr}: {type_.__name__}')

    init_func = f'def __init__(self, {", ".join(args)}) -> None:\n'
    for line in obj_vars:
        init_func += line

    print(init_func, globals(), locals())

    return cls


@dto
class Book:
    author: str = 'Heinrich Hobel'
    title: str
    num_pages: int = '75'


if __name__ == '__main__':
    book = Book()
