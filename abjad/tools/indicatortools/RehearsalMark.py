# -*- encoding: utf-8 -*-
from abjad.tools import mathtools
from abjad.tools.abctools.AbjadObject import AbjadObject


class RehearsalMark(AbjadObject):
    r'''A rehearsal mark.

    ..  container:: example

        ::

            >>> staff = Staff("c'4 d' e' f'")
            >>> score = Score([staff])
            >>> mark = indicatortools.RehearsalMark(number=2)
            >>> attach(mark, staff[0])
            >>> scheme = schemetools.Scheme('format-mark-box-alphabet')
            >>> set_(score).markFormatter = scheme

        ::

            >>> show(score) # doctest: +SKIP

        ..  doctest::

            >>> print(format(score))
            \new Score \with {
                markFormatter = #format-mark-box-alphabet
            } <<
                \new Staff {
                    \mark #2
                    c'4
                    d'4
                    e'4
                    f'4
                }
            >>

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_default_scope',
        '_markup',
        '_number',
        )

    ### INITIALIZER ###

    def __init__(self, number=None, markup=None):
        from abjad.tools import markuptools
        from abjad.tools import scoretools
        # TODO: make default scope work
        #self._default_scope = scoretools.Score
        if markup is not None:
            assert isinstance(markup, markuptools.Markup)
        self._markup = markup
        if number is not None:
            assert mathtools.is_positive_integer(number)
        self._number = number

    ### SPECIAL METHODS ###

    def __copy__(self, *args):
        r'''Copies rehearsal mark.

        ..  container:: example

            ::

                >>> import copy
                >>> markup = Markup(r'\bold { \italic { mark } }')
                >>> mark_1 = indicatortools.RehearsalMark(markup=markup)
                >>> mark_2 = copy.copy(mark_1)

            ::

                >>> str(mark_1) == str(mark_2)
                True

            ::

                >>> mark_1 == mark_2
                True

            ::

                >>> mark_1 is mark_2
                False

        Returns new rehearsal mark.

        '''
        return type(self)(markup=self.markup)

    def __eq__(self, expr):
        r'''Is true when `expr` is another rehearsal mark with `number` and 
        `markup` equal to those of this rehearsal mark. Otherwise false.

        ..  container:: example

            ::

                >>> mark_1 = indicatortools.RehearsalMark(number=None)
                >>> mark_2 = indicatortools.RehearsalMark(number=None)
                >>> mark_3 = indicatortools.RehearsalMark(number=2)

            ::

                >>> mark_1 == mark_1
                True
                >>> mark_1 == mark_2
                True
                >>> mark_1 == mark_3
                False

            ::

                >>> mark_2 == mark_1
                True
                >>> mark_2 == mark_2
                True
                >>> mark_2 == mark_3
                False

            ::

                >>> mark_3 == mark_1
                False
                >>> mark_3 == mark_2
                False
                >>> mark_3 == mark_3
                True

        Returns boolean.
        '''
        if isinstance(expr, type(self)):
            if self.number == expr.number:
                if self.markup == expr.markup:
                    return True
        return False

    def __hash__(self):
        r'''Hashes rehearsal mark.

        Required to be explicitly redefined on Python 3 if __eq__ changes.

        Returns integer.
        '''
        return super(RehearsalMark, self).__hash__()

    def __str__(self):
        r'''Gets string representation of rehearsal mark.

        ..  container:: example

            ::

                >>> mark = indicatortools.RehearsalMark()
                >>> print(str(mark))
                \mark \default

        Returns string.
        '''
        return self._lilypond_format

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from ide import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='number',
                command='n',
                editor=idetools.getters.get_positive_integer,
                ),
            systemtools.AttributeDetail(
                name='markup',
                command='m',
                editor=idetools.getters.get_markup,
                ),
            )

    @property
    def _contents_repr_string(self):
        return str(self)

    @property
    def _lilypond_format(self):
        if self.markup is not None:
            result = r'\mark {}'.format(self.markup)
        elif self.number is not None:
            result = r'\mark #{}'.format(self.number)
        else:
            result = r'\mark \default'
        return result

    @property
    def _lilypond_format_bundle(self):
        from abjad.tools import systemtools
        lilypond_format_bundle = systemtools.LilyPondFormatBundle()
        lilypond_format_bundle.opening.commands.append(str(self))
        return lilypond_format_bundle
        
    ### PUBLIC PROPERTIES ###

    @property
    def markup(self):
        r'''Gets markup of rehearsal mark.

        ..  container:: example

            ::

                >>> markup = Markup(r'\bold { \italic { B } }')
                >>> mark = indicatortools.RehearsalMark(markup=markup)
                >>> print(str(mark.markup))
                \markup {
                    \bold
                        {
                            \italic
                                {
                                    B
                                }
                        }
                    }

        Returns markup or none.
        '''
        return self._markup

    @property
    def number(self):
        r'''Gets number of rehearsal mark.

        ..  container:: example

            ::

                >>> mark = indicatortools.RehearsalMark()
                >>> mark.number is None
                True

        Returns positive integer or none.
        '''
        return self._number