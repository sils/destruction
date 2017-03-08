import sys

if sys.version_info >= (3,):
    import builtins
else:
    import __builtin__ as builtins


from destruction.FakeFloat import FakeFloat
builtins.float = FakeFloat


from destruction.FakeMath import FakeMath
sys.modules['math'] = FakeMath()


from destruction.Sorting import fake_shuffle, fake_sorted
import random
builtins.sorted = fake_sorted
random.shuffle = fake_shuffle
