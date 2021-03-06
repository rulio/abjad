# -*- encoding: utf-8 -*-


def mask_none():
    r'''Makes boolean pattern equal to all ones.

    ..  container:: example

        **Example 1.** Makes mask:

        ::

            >>> mask = rhythmmakertools.mask_none()

        ::

            >>> print(format(mask))
            rhythmmakertools.BooleanPattern(
                indices=(),
                period=1,
                )

    ..  container:: example

        **Example 2.** Makes note rhythm-maker. Effectively applies no mask:

        ::

            >>> mask = rhythmmakertools.mask_none()
            >>> maker = rhythmmakertools.NoteRhythmMaker(
            ...     output_masks=[mask],
            ...     )

        ::

            >>> print(format(maker))
            rhythmmakertools.NoteRhythmMaker(
                output_masks=(
                    rhythmmakertools.BooleanPattern(
                        indices=(),
                        period=1,
                        ),
                    ),
                )

    Returns boolean pattern.
    '''
    from abjad.tools import rhythmmakertools

    return rhythmmakertools.BooleanPattern(
        indices=[],
        period=1,
        )