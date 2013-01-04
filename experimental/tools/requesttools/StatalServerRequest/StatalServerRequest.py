from experimental.tools import statalservertools
from experimental.tools.requesttools.Request import Request


class StatalServerRequest(Request):
    r'''Statal server request.

    The purpose of a statal server request is to function as the source of a setting.
    '''

    ### INITIALIZER ###
    
    def __init__(self, statal_server, request_modifiers=None):
        assert isinstance(server, statalservertools.StatalServer)
        Request.__init__(self, request_modifiers=request_modifiers)
        self._statal_server = statal_server

    ### SPECIAL METHODS ###

    def __call__(self):
        return self.statal_server(self)

    ### PRIVATE METHODS ###

    def _get_payload(self, score_specification=None, voice_name=None):
        raise NotImplementedError

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def statal_server(self):
        return self._statal_server
