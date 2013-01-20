from experimental.tools.settingtools.Expression import Expression
from experimental.tools.settingtools.PayloadCallbackMixin import PayloadCallbackMixin


class StatalServerRequest(Expression, PayloadCallbackMixin):
    r'''Statal server request.

    The purpose of a statal server request is to function as the source of a setting.
    '''

    ### INITIALIZER ###
    
    def __init__(self, statal_server=None, payload_callbacks=None):
        assert isinstance(statal_server, settingtools.StatalServer), repr(statal_server)
        Expression.__init__(self)
        PayloadCallbackMixin.__init__(self, payload_callbacks=payload_callbacks)
        self._statal_server = statal_server

    ### SPECIAL METHODS ###

    def __call__(self):
        return self.statal_server(self)

    ### PRIVATE METHODS ###

    def _evaluate(self, score_specification=None, voice_name=None):
        # ignore voice_name input parameter
        voice_name = None
        raise NotImplementedError

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def statal_server(self):
        return self._statal_server
