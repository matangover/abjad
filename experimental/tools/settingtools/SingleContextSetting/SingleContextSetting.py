import copy
from experimental.tools import helpertools
from experimental.tools.settingtools.Setting import Setting


class SingleContextSetting(Setting):
    r'''

    ::

        >>> from experimental.tools import *

    Single-context setting.

    Set `attribute` to `request` for single-context `anchor`::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecification(score_template)
        >>> red_segment = score_specification.append_segment(name='red')

    ::

        >>> multiple_context_setting = red_segment.set_time_signatures([(4, 8), (3, 8)])

    ::

        >>> contexts = ['Voice 1', 'Voice 3']
        >>> multiple_context_setting = red_segment.set_divisions([(3, 16)], contexts=contexts)

    ::

        >>> score = score_specification.interpret()

    ::

        >>> single_context_setting = score_specification.single_context_settings[1]

    ::

        >>> z(single_context_setting)
        settingtools.SingleContextSetting(
            attribute='divisions',
            request=requesttools.AbsoluteRequest(
                [(3, 16)]
                ),
            anchor='red',
            context_name='Voice 1',
            fresh=True,
            persist=True
            )

    Composers do not create single-context settings.

    Single-context settings are a byproduct of interpretation.

    Multiple-context settings unpack to produce single-context settings.
    '''

    ### INITIALIZER ###

    def __init__(self, attribute=None, request=None, anchor=None, context_name=None, 
        fresh=True, persist=True, truncate=None):
        Setting.__init__(self, attribute=attribute, request=request, anchor=anchor, 
            fresh=fresh, persist=persist, truncate=truncate)
        assert isinstance(context_name, (str, type(None)))
        self._context_name = context_name

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def context_name(self):
        '''Single-context setting context name.

        Return string or none.
        '''
        return self._context_name

    @property
    def storage_format(self):
        '''Single-context setting storage format::

            >>> z(single_context_setting)
            settingtools.SingleContextSetting(
                attribute='divisions',
                request=requesttools.AbsoluteRequest(
                    [(3, 16)]
                    ),
                anchor='red',
                context_name='Voice 1',
                fresh=True,
                persist=True
                )

        Return string.
        '''
        return Setting.storage_format.fget(self)

    ### PUBLIC METHODS ###

    def copy_setting_to_segment_name(self, segment_name):
        '''Create new setting. 

        Set new setting start segment identifier to `segment_name`.

        Set new setting `fresh` to false.

        Return new setting.
        '''
        assert isinstance(segment_name, str)
        new_setting = copy.deepcopy(self)
        new_setting._set_start_segment_identifier(segment_name)
        new_setting._fresh = False
        return new_setting
