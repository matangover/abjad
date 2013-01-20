from experimental.tools.settingtools.Expression import Expression
from experimental.tools.settingtools.PayloadCallbackMixin import PayloadCallbackMixin


class AbsoluteExpression(Expression, PayloadCallbackMixin):
    r'''Absolute expression.

    ::

        >>> expression = settingtools.AbsoluteExpression([(4, 16), (2, 16)])

    ::

        >>> expression
        AbsoluteExpression(((4, 16), (2, 16)))

    ::

        >>> z(expression)
        settingtools.AbsoluteExpression(
            ((4, 16), (2, 16))
            )

    Expression is assumed to resolve to a list or other iterable.

    Because of this absolute expressions afford payload callbacks.
    '''

    ### INTIAILIZER ###

    def __init__(self, payload, payload_callbacks=None):
        assert isinstance(payload, (str, tuple, list)), repr(payload)
        Expression.__init__(self)
        PayloadCallbackMixin.__init__(self, payload_callbacks=payload_callbacks)
        if isinstance(payload, list):
            payload = tuple(payload)
        self._payload = payload

    ### PRIVATE METHODS ###

    def _evaluate(self, score_specification=None, voice_name=None):
        from experimental.tools import settingtools
        # ignore voice_name input parameter
        voice_name = None
        if isinstance(self.payload, (str, tuple)):
            result = self.payload
        else:
            raise TypeError(self.payload)
        result, dummy = self._apply_payload_callbacks(result, None)
        return result

    ### READ-ONLY PROPERTIES ###

    @property
    def payload(self):
        '''Absolute expression payload:

        ::

            >>> expression.payload
            ((4, 16), (2, 16))

        Return tuple or string.
        '''
        return self._payload

    @property
    def payload_callbacks(self):
        '''Absolute expression callbacks:

        ::

            >>> expression.payload_callbacks
            CallbackInventory([])

        Return callback inventory.
        '''
        return PayloadCallbackMixin.payload_callbacks.fget(self)

    @property
    def storage_format(self):
        '''Absolute expression storage format:

        ::

            >>> z(expression)
            settingtools.AbsoluteExpression(
                ((4, 16), (2, 16))
                )

        Return string.
        '''
        return PayloadCallbackMixin.storage_format.fget(self)
