import functools
import sys

commands = {}


def action(*names: str, helptext: str = 'No help. Sorry!'):

    def decorator(func):
        for name in names:
            commands[name] = (func, '' if helptext is None else helptext)
        return func

    return decorator


@action('quit', 'q', helptext='Quit program')
def quit_gracefully(*_: str) -> bool:
    print('Bye!')
    return True


@action('help', 'h', '?', helptext='Display information about the command')
def show_help(*argv: str) -> bool:
    item = argv[1] if len(argv) > 1 else 'help'
    help_ = commands.get(item)
    print('WHAT?' if help_ is None else help_[1])
    return False


def default_action(prog, *args) -> bool:
    print(f'{prog}: what is "{" ".join(args)}"?')
    return False


def ctrl_c_action() -> None:
    print('\n^C')
    sys.exit()


def run(*, prog: str, prompt: str = '> ') -> None:
    argv = None
    while True:
        try:
            argv = input(prompt).split()
        except KeyboardInterrupt:
            ctrl_c_action()
        cmd = commands.get(argv[0].lower(), (functools.partial(default_action, prog), ))[0]
        if cmd(*argv):
            return


if __name__ == '__main__':
    run(prog='CLI')