import builtins
from . import gizoogle


_print = builtins.print
builtins.print = lambda *args, **kwargs: _print(
    gizoogle.translate(' '.join(args)), **kwargs
)
