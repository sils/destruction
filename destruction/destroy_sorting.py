import random

from .utils import builtins


_shuffle = random.shuffle
_sorted = builtins.sorted


def fake_shuffle(a: list, *args, **kwargs):
    a.sort()  # Shuffle returns None and shuffles in place


def fake_sorted(a, *args, **kwargs):
    shuffled = list(a)
    _shuffle(shuffled)
    return shuffled


builtins.sorted = fake_sorted
random.shuffle = fake_shuffle
