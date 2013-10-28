# -*- encoding: utf-8 -*-
from abjad.tools import contexttools
from abjad.tools import datastructuretools
from abjad.tools import iterationtools
from abjad.tools import marktools
from experimental.tools.handlertools.DynamicHandler import DynamicHandler


class TerracedDynamicsHandler(DynamicHandler):
    r'''Terraced dynamics.
    '''

    def __init__(self, dynamics=None, minimum_duration=None):
        DynamicHandler.__init__(self, minimum_duration=minimum_duration)
        if dynamics is None:
            dynamics = []
        self.dynamics = dynamics

    ### SPECIAL METHODS ###

    def __call__(self, expr, offset=0):
        dynamics = datastructuretools.CyclicList(self.dynamics)
        for i, note_or_chord in enumerate(
            iterationtools.iterate_notes_and_chords_in_expr(expr)):
            dynamic_name = dynamics[offset+i]
            if self.minimum_duration <= note_or_chord._get_duration():
                #contexttools.DynamicMark(dynamic_name)(note_or_chord)
                command = marktools.LilyPondCommandMark(dynamic_name, 'right')
                command.attach(note_or_chord)
        return expr

    ###  PUBLIC PROPERTIES ###

    @apply
    def dynamics():
        def fget(self):
            return self._dynamics
        def fset(self, dynamics):
            if dynamics is None:
                self._dynamics = dynamics
            elif all(
                contexttools.DynamicMark.is_dynamic_name(x) for x in dynamics):
                self._dynamics = dynamics
            else:
                raise TypeError(dynamics)
        return property(**locals())