from abjad.tools import componenttools


def label_leaves_in_expr_with_melodic_chromatic_intervals(expr, markup_direction='up'):
    r""".. versionadded:: 2.0

    Label leaves in `expr` with melodic chromatic intervals::

        >>> staff = Staff(notetools.make_notes([0, 25, 11, -4, -14, -13, 9, 10, 6, 5], [Duration(1, 8)]))
        >>> leaftools.label_leaves_in_expr_with_melodic_chromatic_intervals(staff)
        >>> f(staff)
        \new Staff {
            c'8 ^ \markup { +25 }
            cs'''8 ^ \markup { -14 }
            b'8 ^ \markup { -15 }
            af8 ^ \markup { -10 }
            bf,8 ^ \markup { +1 }
            b,8 ^ \markup { +22 }
            a'8 ^ \markup { +1 }
            bf'8 ^ \markup { -4 }
            fs'8 ^ \markup { -1 }
            f'8
        }

    Return none.
    """
    from abjad.tools import leaftools
    from abjad.tools import markuptools
    from abjad.tools import notetools
    from abjad.tools import pitchtools

    for note in componenttools.iterate_components_forward_in_expr(expr, notetools.Note):
        thread_iterator = componenttools.iterate_thread_forward_from_component(note, leaftools.Leaf)
        try:
            thread_iterator.next()
            next_leaf = thread_iterator.next()
            if isinstance(next_leaf, notetools.Note):
                mci = pitchtools.calculate_melodic_chromatic_interval_from_pitch_carrier_to_pitch_carrier(
                    note, next_leaf)
                markuptools.Markup(mci, markup_direction)(note)
        except StopIteration:
            pass
