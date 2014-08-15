# -*- encoding: utf-8 -*-


def selects_first_logical_tie_in_pitched_runs():
    r'''Selects first logical tie in pitched runs.

    ..  container:: example

        ::
        
            >>> selector = selectortools.selects_first_logical_tie_in_pitched_runs()
            >>> print(format(selector))
            selectortools.Selector(
                callbacks=(
                    selectortools.PrototypeSelectorCallback(
                        scoretools.Leaf
                        ),
                    selectortools.RunSelectorCallback(
                        (
                            scoretools.Note,
                            scoretools.Chord,
                            )
                        ),
                    selectortools.LogicalTieSelectorCallback(
                        flatten=False,
                        pitched=False,
                        trivial=True,
                        only_with_head=False,
                        only_with_tail=False,
                        ),
                    selectortools.SliceSelectorCallback(
                        argument=0,
                        apply_to_each=True,
                        ),
                    ),
                )

        ::

            >>> staff = Staff()
            >>> staff.extend(r"c'4. d'8 ~ \times 2/3 { d'4 r4 e'4 ~ } e'8 f'4.")
            >>> print(format(staff))
            \new Staff {
                c'4.
                d'8 ~
                \times 2/3 {
                    d'4
                    r4
                    e'4 ~
                }
                e'8
                f'4.
            }

        ::

            >>> for x in selector(staff):
            ...     x
            ...
            LogicalTie(Note("c'4."),)
            LogicalTie(Note("e'4"), Note("e'8"))

    '''
    from experimental.tools import selectortools
    selector = selectortools.selects_pitched_runs()
    selector = selector.by_logical_tie(flatten=False)
    selector = selector[0]
    return selector