import copy
from experimental.tools.settingtools.Setting import Setting


class MultipleContextSetting(Setting):
    r'''

    Multiple-context setting::
    
        >>> from abjad.tools import *
        >>> from experimental.tools import *

    Set `attribute` to `request` for multiple-context `anchor`:: 

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecification(score_template)
        >>> red_segment = score_specification.append_segment(name='red')

    ::

        >>> multiple_context_setting = red_segment.set_time_signatures([(4, 8), (3, 8)])

    ::

        >>> z(multiple_context_setting)
        settingtools.MultipleContextSetting(
            attribute='time_signatures',
            request=requesttools.AbsoluteRequest(
                ((4, 8), (3, 8))
                ),
            anchor='red',
            persist=True
            )

    Composers create multiple-context settings at specification-time.

    Composers create multiple-context settings with ``SegmentSpecification`` setter methods.

    Multiple-context settings capture composers' musical intent.
    '''

    ### INITIAILIZER ###

    def __init__(self, attribute=None, request=None, anchor=None, context_names=None, 
            persist=True, truncate=None):
        Setting.__init__(self, attribute=attribute, request=request, anchor=anchor, 
            persist=persist, truncate=truncate)
        assert isinstance(context_names, (list, type(None))), repr(context_names)
        self._context_names = context_names

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def context_names(self):
        '''Multiple-context setting context names.
    
        Return list of strings or none.
        '''
        return self._context_names

    ### PUBLIC METHODS ###

    def unpack(self):
        from experimental.tools import settingtools
        single_context_settings = []
        if self.context_names is None:
            anchor = copy.deepcopy(self.anchor)
            single_context_setting = settingtools.SingleContextSetting(
                self.attribute, 
                self.request, 
                anchor,
                context_name=None,
                persist=self.persist, 
                truncate=self.truncate)
            single_context_settings.append(single_context_setting)
        else:
            for context_name in self.context_names:
                anchor = copy.deepcopy(self.anchor)
                single_context_setting = settingtools.SingleContextSetting(
                    self.attribute, 
                    self.request, 
                    anchor,
                    context_name=context_name,
                    persist=self.persist, 
                    truncate=self.truncate)
                single_context_settings.append(single_context_setting)
        return single_context_settings
