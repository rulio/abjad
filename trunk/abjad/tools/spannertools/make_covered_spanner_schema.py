from abjad.tools import componenttools
from abjad.tools.spannertools.get_spanners_covered_by_components import get_spanners_covered_by_components
from abjad.tools.spannertools.get_spanners_attached_to_component import get_spanners_attached_to_component


def make_covered_spanner_schema(components):
    r'''.. versionadded:: 2.0

    Make schema of spanners covered by `components`::

        >>> voice = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
        >>> pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(voice)
        >>> beam = beamtools.BeamSpanner(voice.leaves[:4])
        >>> slur = spannertools.SlurSpanner(voice[-2:])

    ::

        >>> f(voice)
        \new Voice {
            {
                \time 2/8
                c'8 [
                d'8
            }
            {
                e'8
                f'8 ]
            }
            {
                g'8 (
                a'8
            }
            {
                b'8
                c''8 )
            }
        }

    ::

        >>> spannertools.make_covered_spanner_schema([voice]) # doctest: +SKIP
        {BeamSpanner(c'8, d'8, e'8, f'8): [2, 3, 5, 6], SlurSpanner(|2/8(2)|, |2/8(2)|): [7, 10]}

    Return dictionary.
    '''

    schema = {}
    spanners_covered_by_components = get_spanners_covered_by_components(components)
    for spanner in spanners_covered_by_components:
        schema[spanner] = []

    for i, component in enumerate(componenttools.iterate_components_forward_in_expr(components)):
        attached_spanners = get_spanners_attached_to_component(component)
        for attached_spanner in attached_spanners:
            try:
                schema[attached_spanner].append(i)
            except KeyError:
                pass

    return schema
