from abjad.tools.instrumenttools._Instrument import _Instrument


class Performer(object):
    r'''.. versionadded:: 2.5

    Abjad model of performer::

        abjad> instrumenttools.Performer('Flutist')
        Performer('Flutist')

    The purpose of the class is to model things like
    Flute I doubling piccolo and alto flute.

    At present the class is a list of instruments.
    '''

    def __init__(self, name=None, instruments=None):
        self.name = name
        self.instruments = instruments

    ### OVERLOADS ###

    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.name == other.name:
                if sorted(self.instruments) == sorted(other.instruments):
                    return True
        return False

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return self._repr_helper(include_tools_package=False)

    ### PRIVATE ATTRIBUTES ###

    @property
    def _repr_with_tools_package(self):
        return self._repr_helper(include_tools_package=True)

    ### PRIVATE METHODS ####

    def _repr_helper(self, include_tools_package=False):
        values = []
        if self.name is not None:
            values.append(repr(self.name))
        if self.instruments:
            if include_tools_package:
                instruments = ', '.join([x._repr_with_tools_package for x in self.instruments])
                instruments = '[{}]'.format(instruments)
            else:
                instruments = str(self.instruments[:])
            values.append(instruments)
        values = ', '.join(values)
        if include_tools_package:
            tools_package = self.__module__.split('.')[-3]
            return '{}.{}({})'.format(tools_package, type(self).__name__, values)
        else:
            return '{}({})'.format(type(self).__name__, values)

    ### PUBLIC ATTRIBUTES ###

    @apply
    def instruments():
        def fget(self):
            r'''List of instruments to be played by performer::

                abjad> performer = instrumenttools.Performer('Flutist')

            ::

                abjad> performer.instruments.append(instrumenttools.Flute())
                abjad> performer.instruments.append(instrumenttools.Piccolo())

            ::

                abjad> performer.instruments
                [Flute('Flute', 'Fl.'), Piccolo('Piccolo', 'Picc.')]

            Return list.
            '''
            return self._instruments
        def fset(self, instruments):
            if instruments is None:
                self._instruments = []
            elif isinstance(instruments, list):
                assert all([isinstance(x, _Instrument) for x in instruments])
                self._instruments = instruments[:]
            else:
                raise TypeError('instruments %r must be list or none.' % instruments)
        return property(**locals())

    @property
    def instrument_count(self):
        r'''Read-only number of instruments to be played by performer::

            abjad> performer = instrumenttools.Performer('Flutist')

        ::

            abjad> performer.instruments.append(instrumenttools.Flute())
            abjad> performer.instruments.append(instrumenttools.Piccolo())

        ::

            abjad> performer.instrument_count
            2

        Return nonnegative integer
        '''
        return len(self.instruments)

    @property
    def is_doubling(self):
        r'''Is performer to play more than one instrument? ::

            abjad> performer = instrumenttools.Performer('Flutist')

        ::

            abjad> performer.instruments.append(instrumenttools.Flute())
            abjad> performer.instruments.append(instrumenttools.Piccolo())

        ::

            abjad> performer.is_doubling
            True

        Return boolean.
        '''
        return 1 < self.instrument_count

    @apply
    def name():
        def fget(self):
            r'''Score name of performer::

                abjad> performer = instrumenttools.Performer('Flutist')

            ::

                abjad> performer.name
                'Flutist'

            Return string.
            '''
            return self._name
        def fset(self, name):
            assert isinstance(name, (str, type(None)))
            self._name = name
        return property(**locals())
