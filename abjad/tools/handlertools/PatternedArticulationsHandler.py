# -*- encoding: utf-8 -*-
import copy
from abjad.tools import datastructuretools
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import select
from abjad.tools.handlertools.ArticulationHandler import ArticulationHandler


class PatternedArticulationsHandler(ArticulationHandler):
    r'''Patterned articulations handler.
    '''

    ### CLASS ATTRIBUTES ###

    __slots__ = (
        '_articulation_lists',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        articulation_lists=None,
        minimum_duration=None,
        maximum_duration=None,
        minimum_written_pitch=None,
        maximum_written_pitch=None,
        ):
        ArticulationHandler.__init__(
            self,
            minimum_duration=minimum_duration,
            maximum_duration=maximum_duration,
            minimum_written_pitch=minimum_written_pitch,
            maximum_written_pitch=maximum_written_pitch,
            )
        if articulation_lists is not None:
            for articulation_list in articulation_lists:
                prototype = (tuple, list)
                if not isinstance(articulation_list, (tuple, list)):
                    message = 'not articulation list: {!r}.'
                    message = message.format(articulation_list)
                    raise TypeError(message)
                for articulation in articulation_list:
                    if not isinstance(articulation, str):
                        message = 'not articulation: {!r}.'
                        message = message.format(articulation)
                        raise TypeError(message)
        self._articulation_lists = articulation_lists

    ### SPECIAL METHODS ###

    #def __call__(self, expr, offset=0, skip_first=0, skip_last=0):
    def __call__(
        self, 
        expr, 
        timespan=None, 
        offset=0, 
        skip_first=0, 
        skip_last=0,
        ):
        r'''Calls handler on `expr` with keywords.

        Returns none.
        '''
        articulation_lists = datastructuretools.CyclicTuple(
            self.articulation_lists)
        prototype = (scoretools.Note, scoretools.Chord)
        notes_and_chords = list(iterate(expr).by_class(prototype))
        notes_and_chords = notes_and_chords[skip_first:]
        if skip_last:
            notes_and_chords = notes_and_chords[:-skip_last]
        for i, note_or_chord in enumerate(notes_and_chords):
            logical_tie = inspect_(note_or_chord).get_logical_tie()
            duration = logical_tie.get_duration()
            articulation_list = articulation_lists[offset+i]
            articulation_list = [
                indicatortools.Articulation(_)
                for _ in articulation_list
                ]
            if self.minimum_duration is not None:
                if duration <= self.minimum_duration:
                    continue
            if self.maximum_duration is not None:
                if self.maximum_duration < duration:
                    continue
            if self.minimum_written_pitch is not None:
                if isinstance(note_or_chord, scoretools.Note):
                    minimum_written_pitch = note_or_chord.written_pitch
                else:
                    minimum_written_pitch = note_or_chord.writen_pitches[0]
                if minimum_written_pitch < self.minimum_written_pitch:
                    continue
            if self.maximum_written_pitch is not None:
                if isinstance(note_or_chord, scoretools.Note):
                    maximum_written_pitch = note_or_chord.written_pitch
                else:
                    maximum_written_pitch = note_or_chord.written_pitches[-1]
                if self.maximum_written_pitch < maximum_written_pitch:
                    continue
            for articulation in articulation_list:
                # TODO: make new(articulation) work
                articulation = copy.copy(articulation)
                attach(articulation, note_or_chord)
        return expr

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from ide import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='articulation_lists',
                command='al',
                editor=idetools.getters.get_lists,
                ),
            systemtools.AttributeDetail(
                name='minimum_duration',
                command='nd',
                editor=idetools.getters.get_duration,
                ),
            systemtools.AttributeDetail(
                name='maximum_duration',
                command='xd',
                editor=idetools.getters.get_duration,
                ),
            systemtools.AttributeDetail(
                name='minimum_written_pitch',
                command='np',
                editor=idetools.getters.get_named_pitch,
                ),
            systemtools.AttributeDetail(
                name='maximum_written_pitch',
                command='xp',
                editor=idetools.getters.get_named_pitch,
                ),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def articulation_lists(self):
        r'''Gets articulation lists of handler.

        Returns tuple or none.
        '''
        return self._articulation_lists