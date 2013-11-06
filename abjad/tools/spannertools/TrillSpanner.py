# -*- encoding: utf-8 -*-
from abjad.tools import pitchtools
from abjad.tools.spannertools.Spanner import Spanner


class TrillSpanner(Spanner):
    r'''A trill spanner.

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> trill = spannertools.TrillSpanner()
        >>> attach(trill, staff[:])
        >>> show(staff) # doctest: +SKIP

    ..  doctest::

        >>> f(staff)
        \new Staff {
            c'8 \startTrillSpan
            d'8
            e'8
            f'8 \stopTrillSpan
        }

    Overrides LilyPond TrillSpanner grob.
    '''

    ### INITIALIZER ###

    def __init__(
        self, 
        components=None,
        overrides=None,
        ):
        Spanner.__init__(
            self, 
            components,
            overrides=overrides,
            )
        self._pitch = None

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        new.written_pitch = self.written_pitch

    def _format_before_leaf(self, leaf):
        result = []
        if self.pitch is not None:
            if self._is_my_first_leaf(leaf):
                result.append(r'\pitchedTrill')
        return result

    def _format_right_of_leaf(self, leaf):
        result = []
        if self._is_my_first_leaf(leaf):
            result.append(r'\startTrillSpan')
            if self.pitch is not None:
                result.append(str(self.pitch))
        if self._is_my_last_leaf(leaf):
            result.append(r'\stopTrillSpan')
        return result

    ### PUBLIC PROPERTIES ###

    @apply
    def pitch():
        def fget(self):
            r'''Optional read / write pitch for pitched trills.

                ::

                    >>> t = Staff("c'8 d'8 e'8 f'8")
                    >>> trill = spannertools.TrillSpanner()
                    >>> attach(trill, t[:2])
                    >>> trill.pitch = pitchtools.NamedPitch('cs', 4)

                ..  doctest::

                    >>> f(t)
                    \new Staff {
                        \pitchedTrill c'8 \startTrillSpan cs'
                        d'8 \stopTrillSpan
                        e'8
                        f'8
                    }

            Set pitch.
            '''
            return self._pitch
        def fset(self, expr):
            if expr is None:
                self._pitch = expr
            else:
                pitch = pitchtools.NamedPitch(expr)
                self._pitch = pitch
        return property(**locals())

    @apply
    def written_pitch():
        def fget(self):
            return self.pitch
        def fset(self, arg):
            self.pitch = arg
        return property(**locals())