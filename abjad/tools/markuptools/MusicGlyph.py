# -*- encoding: utf-8 -*-
from abjad.tools import schemetools
from abjad.tools.markuptools.MarkupCommand import MarkupCommand


class MusicGlyph(MarkupCommand):
    r'''Abjad model of a LilyPond \musicglyph command:

    ::

        >>> markuptools.MusicGlyph('accidentals.sharp')
        MusicGlyph('accidentals.sharp')
        >>> print _
        \musicglyph #"accidentals.sharp"

    Return `MusicGlyph` instance.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(self, glyph_name):
        from abjad.ly import music_glyphs
        assert glyph_name in music_glyphs, 'Not a valid LilyPond glyph name.'
        glyph_scheme = schemetools.Scheme(glyph_name, force_quotes=True)
        MarkupCommand.__init__(self, 'musicglyph', glyph_scheme)

    ### SPECIAL METHODS ###

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.args[0]._value)