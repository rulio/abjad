from abjad.tools.pitcharraytools._leaf_iterables_to_pitch_array import _leaf_iterables_to_pitch_array


def make_populated_pitch_array_from_list_of_pitch_lists(leaf_iterables):
    r'''.. versionadded:: 2.0

    Make populated pitch array from `leaf_iterables`::

        >>> from abjad.tools import pitcharraytools

    ::

        >>> score = Score([])
        >>> score.append(Staff("c'8 d'8 e'8 f'8"))
        >>> score.append(Staff("c'4 d'4"))
        >>> score.append(Staff(tuplettools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8") * 2))
        >>> f(score)
        \new Score <<
            \new Staff {
                c'8
                d'8
                e'8
                f'8
            }
            \new Staff {
                c'4
                d'4
            }
            \new Staff {
                \times 2/3 {
                    c'8
                    d'8
                    e'8
                }
                \times 2/3 {
                    c'8
                    d'8
                    e'8
                }
            }
        >>

    ::

        >>> array = pitcharraytools.make_populated_pitch_array_from_list_of_pitch_lists(score)
        >>> print array
        [c'     ] [d'     ] [e'     ] [f'     ]
        [c'                   ] [d'                   ]
        [c'] [d'     ] [e'] [c'] [d'     ] [e']

    Return pitch array.
    '''

    return _leaf_iterables_to_pitch_array(leaf_iterables, populate = True)
