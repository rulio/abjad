# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class ContrabassSaxophone(Instrument):
    r'''A bass saxophone.

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> sax = instrumenttools.ContrabassSaxophone()
        >>> attach(sax, staff)
        >>> show(staff) # doctest: +SKIP

    ..  doctest::

        >>> print format(staff)
        \new Staff {
            \set Staff.instrumentName = \markup { Contrabass saxophone }
            \set Staff.shortInstrumentName = \markup { Cbass. sax. }
            c'8
            d'8
            e'8
            f'8
        }

    The contrabass saxophone is pitched in E-flat.

    The contrabass saxophone targets staff context by default.
    '''

    ### INITIALIZER ###

    def __init__(
        self,
        instrument_name='contrabass saxophone',
        short_instrument_name='cbass. sax.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range=None,
        sounding_pitch_of_written_middle_c='ef,,',
        ):
        pitch_range = pitch_range or pitchtools.PitchRange(-36, -4)
        Instrument.__init__(
            self,
            instrument_name=instrument_name,
            short_instrument_name=short_instrument_name,
            instrument_name_markup=instrument_name_markup,
            short_instrument_name_markup=short_instrument_name_markup,
            allowable_clefs=allowable_clefs,
            pitch_range=pitch_range,
            sounding_pitch_of_written_middle_c=\
                sounding_pitch_of_written_middle_c,
            )
        self._performer_names.extend([
            'wind player',
            'reed player',
            'single reed player',
            'saxophonist',
            ])
