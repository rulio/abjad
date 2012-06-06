from abjad.tools.spannertools.Spanner import Spanner


# TODO: remove and just use Spanner instead with overrides
class TextScriptSpanner(Spanner):
    r'''.. versionadded:: 2.0

    Abjad text script spanner::

        >>> staff = Staff("c'8 d'8 e'8 f'8")

    ::

        >>> spanner = spannertools.TextScriptSpanner(staff[:])
        >>> spanner.override.text_script.color = 'red'
        >>> markuptools.Markup(r'\italic { espressivo }', 'up')(staff[1])
        Markup(('\\italic { espressivo }',), direction='^')(d'8)

    ::

        >>> f(staff)
        \new Staff {
            \override TextScript #'color = #red
            c'8
            d'8 ^ \markup { \italic { espressivo } }
            e'8
            f'8
            \revert TextScript #'color
        }

    Override LilyPond TextScript grob.

    Return text script spanner.
    '''

    ### INITIALIZER ###

    def __init__(self, components=None):
        Spanner.__init__(self, components)
