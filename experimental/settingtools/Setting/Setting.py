import abc
from abjad.tools.abctools.AbjadObject import AbjadObject
from experimental import selectortools


class Setting(AbjadObject):
    r'''.. versionadded:: 1.0

    Abstract setting class from which concrete settings inherit.
    '''

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self, attribute, source, selector, fresh=True, persist=True, truncate=None):
        assert isinstance(attribute, str)
        assert isinstance(selector, (selectortools.Selector, type(None)))
        assert isinstance(fresh, bool)
        assert isinstance(persist, bool)
        assert isinstance(truncate, (bool, type(None)))
        self._attribute = attribute
        self._source = source
        self._selector = selector
        self._fresh = fresh
        self._persist = persist
        self._truncate = truncate

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if not isinstance(expr, type(self)):
            return False
        if not self._mandatory_argument_values == expr._mandatory_argument_values:
            return False
        return self._keyword_argument_values == expr._keyword_argument_values

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def attribute(self):
        '''Setting attribute.

        Return string.
        '''
        return self._attribute

    @property
    def fresh(self):
        '''True when setting results from explicit composer command.
        Otherwise false.

        Return boolean.
        '''
        return self._fresh

    @property
    def persist(self):
        '''True when setting should persist.
         
        Return boolean.
        '''
        return self._persist

    @property
    def selector(self):
        '''Setting selector.

        Return selector or none.
        '''
        return self._selector

    @property
    def source(self):
        '''Setting source.

        Many different return types are possible.
        '''
        return self._source

    @property
    def truncate(self):
        '''True when setting should truncate.

        Return boolean.
        '''
        return self._truncate
