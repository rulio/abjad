from abjad.tools.stafftools.Staff import Staff
from abjad.tools.componenttools.iterate_components_backward_in_expr import iterate_components_backward_in_expr


def iterate_staves_backward_in_expr(expr, start = 0, stop = None):
    r'''.. versionadded:: 2.0

    Iterate staves backward in `expr`::

        >>> score = Score(4 * Staff([]))

    ::

        >>> f(score)
        \new Score <<
            \new Staff {
            }
            \new Staff {
            }
            \new Staff {
            }
            \new Staff {
            }
        >>

    ::

        >>> for staff in stafftools.iterate_staves_backward_in_expr(score):
        ...     staff
        ...
        Staff{}
        Staff{}
        Staff{}
        Staff{}

    Return generator.
    '''

    return iterate_components_backward_in_expr(expr, Staff, start = start, stop = stop)
