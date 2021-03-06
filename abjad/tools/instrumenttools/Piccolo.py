# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class Piccolo(Instrument):
    r'''A piccolo.

    ::

        >>> staff = Staff("c'4 d'4 e'4 fs'4")
        >>> piccolo = instrumenttools.Piccolo()
        >>> attach(piccolo, staff)
        >>> show(staff) # doctest: +SKIP

    ..  doctest::

        >>> print(format(staff))
        \new Staff {
            \set Staff.instrumentName = \markup { Piccolo }
            \set Staff.shortInstrumentName = \markup { Picc. }
            c'4
            d'4
            e'4
            fs'4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        instrument_name='piccolo',
        short_instrument_name='picc.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range='[D5, C8]',
        sounding_pitch_of_written_middle_c='C5',
        ):
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
            'flautist',
            'flutist',
            ])

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets piccolo's allowable clefs.

        ..  container:: example

            ::

                >>> piccolo.allowable_clefs
                ClefInventory([Clef(name='treble')])

            ::

                >>> show(piccolo.allowable_clefs) # doctest: +SKIP

        Returns clef inventory.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets piccolo's name.

        ..  container:: example

            ::

                >>> piccolo.instrument_name
                'piccolo'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets piccolo's instrument name markup.

        ..  container:: example

            ::

                >>> piccolo.instrument_name_markup
                Markup(contents=('Piccolo',))

            ::

                >>> show(piccolo.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets piccolo's range.

        ..  container:: example

            ::

                >>> piccolo.pitch_range
                PitchRange(range_string='[D5, C8]')

            ::

                >>> show(piccolo.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets piccolo's short instrument name.

        ..  container:: example

            ::

                >>> piccolo.short_instrument_name
                'picc.'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets piccolo's short instrument name markup.

        ..  container:: example

            ::

                >>> piccolo.short_instrument_name_markup
                Markup(contents=('Picc.',))

            ::

                >>> show(piccolo.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def sounding_pitch_of_written_middle_c(self):
        r'''Gets sounding pitch of piccolo's written middle C.

        ..  container:: example

            ::

                >>> piccolo.sounding_pitch_of_written_middle_c
                NamedPitch("c''")

            ::

                >>> show(piccolo.sounding_pitch_of_written_middle_c) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.sounding_pitch_of_written_middle_c.fget(self)
