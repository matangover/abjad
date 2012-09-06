import abc
from abjad.tools.abctools import AbjadObject


class AttackPointOptimizer(AbjadObject):
    '''Abstract attack-point optimizer class from which concrete attack-point
    optimizer classes inherit.

    Attack-point optimizers may alter the number, order, and individual durations
    of leaves in a tie chain, but may not alter the overall duration of that
    tie chain.

    They effectively "clean up" notation, post-quantization.
    '''

    ### INITIALIZER ###

    def __init__(self):
        pass

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(self, expr):
        raise NotImplemented
