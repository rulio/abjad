from abjad.tools.leaftools._label_leaves_in_expr_with_leaf_durations import _label_leaves_in_expr_with_leaf_durations


def label_leaves_in_expr_with_prolated_leaf_duration(expr, markup_direction = 'down'):
    r'''.. versionadded:: 1.1

    Label leaves in `expr` with prolated leaf duration::

        >>> tuplet = tuplettools.FixedDurationTuplet(Duration(1, 4), "c'8 d'8 e'8")
        >>> leaftools.label_leaves_in_expr_with_prolated_leaf_duration(tuplet)
        >>> f(tuplet)
        \times 2/3 {
            c'8 _ \markup { \small 1/12 }
            d'8 _ \markup { \small 1/12 }
            e'8 _ \markup { \small 1/12 }
        }

    Return none.
    '''

    show = ['prolated']
    return _label_leaves_in_expr_with_leaf_durations(
        expr, markup_direction = markup_direction, show = show)
