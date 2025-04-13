import collections.abc


class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"

    # Too aggressive.
    BLUE = "\033[34m"

    LIGHT_BLUE = "\033[1;34m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREEN_CYAN = "\033[38;5;77m"
    TEAL = "\033[38;5;80m"

    RESET = "\033[0m"
    colors = tuple(t for t in locals() if t.isupper())


def cformat(s: str) -> str:
    """Format string with colors.

    For strings automatically add `RESET` at the end
    and replace all `{COLOR}` with the color code.

    Use double braces in f-strings to pass colors.
    """
    for c in Color.colors:
        s = s.replace(f"{{{c}}}", getattr(Color, c))
    s = f"{s}{Color.RESET}"
    return s


def cprint(s: object) -> None:
    """Print but with c, where c (hopefully) stands for "clever".

    Same as `print` but is using `cformat` if `s` is a string.
    """
    if type(s) is str:
        s = cformat(s)
        print(s)
    elif isinstance(s, collections.abc.Iterable):
        print(*s)
    else:
        print(s)
