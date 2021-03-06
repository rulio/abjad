# -*- encoding: utf-8 -*-
from abjad.tools.abctools import AbjadValueObject


class TupletSpellingSpecifier(AbjadValueObject):
    r'''Tuplet spelling specifier.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_avoid_dots',
        '_is_diminution',
        '_simplify_tuplets',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        avoid_dots=False,
        is_diminution=True,
        simplify_tuplets=False,
        ):
        self._avoid_dots = bool(avoid_dots)
        self._is_diminution = bool(is_diminution)
        self._simplify_tuplets = bool(simplify_tuplets)

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from ide import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='avoid_dots',
                command='ad',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='is_diminution',
                command='id',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='simplify_tuplets',
                command='st',
                editor=idetools.getters.get_boolean,
                ),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def avoid_dots(self):
        r'''Is true when tuplet spelling should avoid dotted rhythmic values.
        Otherwise false.

        Defaults to false.

        Returns boolean.
        '''
        return self._avoid_dots

    @property
    def is_diminution(self):
        r'''Is true when tuplet should be spelled as diminution. Otherwise
        false.

        Defaults to true.

        Returns boolean.
        '''
        return self._is_diminution

    @property
    def simplify_tuplets(self):
        r'''Is true when tuplets should be simplified. Otherwise false.

        Defaults to false.

        Returns boolean.
        '''
        return self._simplify_tuplets