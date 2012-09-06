import copy
from abjad.tools import sequencetools   
from abjad.tools import voicetools
from experimental.quantizationtools.QTarget import QTarget


class BeatwiseQTarget(QTarget): 
    '''A beat-wise quantization target.

    Not composer-safe.

    Used internally by ``Quantizer``.

    Return ``BeatwiseQTarget`` instance.
    '''

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def beats(self):
        return tuple(self.items)
    
    @property
    def item_klass(self):
        from experimental import quantizationtools
        return quantizationtools.QTargetBeat

    ### PRIVATE METHODS ###

    def _notate(self, grace_handler, attack_point_optimizer):
        voice = voicetools.Voice()

        # generate the first
        beat = self.items[0]
        components = beat.q_grid(beat.beatspan)
        copy.copy(beat.tempo)(components[0])
        voice.extend(components)

        # generate the rest pairwise, comparing tempi
        for beat_one, beat_two in sequencetools.iterate_sequence_pairwise_strict(self.items):
            components = beat_two.q_grid(beat_two.beatspan)
            if beat_two.tempo != beat_one.tempo:
                copy.copy(beat_two.tempo)(components[0])
            voice.extend(components)

        # apply tie chains, pitches, grace containers
        self._notate_leaves_pairwise(voice, grace_handler)

        # partition tie chains in voice
        attack_point_optimizer(voice)

        return voice
