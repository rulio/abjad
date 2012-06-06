def interpolate_linear(y1, y2, mu):
    '''Linear interpolate `y1` and `y2` with `mu` normalized ``[0, 1]``::

        >>> from abjad.tools import mathtools

    ::

        >>> mathtools.interpolate_linear(0, 1, 0.5)
        0.5

    Return float.

    .. versionchanged:: 2.0
        renamed ``interpolate.linear()`` to
        ``mathtools.interpolate_linear()``.
    '''

    return (y1 * (1 - mu) + y2 * mu)
