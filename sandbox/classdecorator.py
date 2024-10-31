from typing import Any


class DefaultSentinel:
    pass


class Field:
    def __init__(self, name: str, type_: type, default: Any = DefaultSentinel()) -> None:
        self.name = name
        self.type_ = type_
        self.default = default


def dto[T](cls: T) -> T:
    args, obj_vars, fields = [], [], {}
    for name, type_ in cls.__annotations__.items():
        if name in cls.__dict__:
            fields[name] = Field(name, type_, cls.__dict__[name])
        else:
            fields[name] = Field(name, type_)

    setattr(cls, '_FIELDS', fields)

    for field in fields.values():
        if isinstance(field.default, DefaultSentinel):
            obj_vars.append(f'    self.{field.name} = {field.name}')
            args.append(f'{field.name}: {field.type_.__name__}')

    for field in fields.values():
        if not isinstance(field.default, DefaultSentinel):
            obj_vars.append(f'    self.{field.name} = {field.name}')
            args.append(f'{field.name}: {field.type_.__name__} = {repr(field.default)}')

    new_init = f"""
def __init__(self{", " + ", ".join(args) if len(args) else ""}) -> None:
{"\n".join(obj_vars) if len(obj_vars) else "    pass"}
    """

    exec(new_init, globals(), locals())

    new_init_func = locals()['__init__']
    new_init_func.__name__ = '__init__'
    new_init_func.__qualname__ = f'{cls.__name__}.__init__'

    cls.__init__ = new_init_func

    return cls


@dto
class Book:
    author: str = 'Heinrich Hobel'
    title: str
    num_pages: int = 75


if __name__ == '__main__':
    book = Book('Holzbearbetung im Wandel der Zeit')
    print(book.__dict__)
