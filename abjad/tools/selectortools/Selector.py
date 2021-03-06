# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.abctools import AbjadValueObject
from abjad.tools.topleveltools import select


class Selector(AbjadValueObject):
    r'''A selector.

    Selectors select components.

    Selectors aggregate a sequence of callable classes which describe the
    process of component selection.

    Selectors provide methods for configuring and making new selectors.

    Composers may chain selectors together.

    ..  container:: example

        Score for examples:

        ::

            >>> string = r"c'4 \times 2/3 { d'8 r8 e'8 } r16 f'16 g'8 a'4"
            >>> staff = Staff(string)
            >>> show(staff) # doctest: +SKIP

    ..  container:: example

        **Example 1.** Selects a component:

        ::

            >>> selector = selectortools.Selector()
            >>> for x in selector(staff):
            ...     x
            ...
            <Staff{6}>

    ..  container:: example

        **Example 2.** Selects all of the leaves in a component:

        ::

            >>> selector = selector.by_leaves()
            >>> for x in selector(staff):
            ...     x
            ...
            Selection(Note("c'4"), Note("d'8"), Rest('r8'), Note("e'8"), Rest('r16'), Note("f'16"), Note("g'8"), Note("a'4"))

    ..  container:: example

        **Example 3.** Selects runs of notes:

        ::

            >>> selector = selector.by_run(Note)
            >>> for x in selector(staff):
            ...     x
            ...
            Selection(Note("c'4"), Note("d'8"))
            Selection(Note("e'8"),)
            Selection(Note("f'16"), Note("g'8"), Note("a'4"))

    ..  container:: example

        **Example 4.** Selects subselections with lengths equal to ``3``:

        ::

            >>> selector = selector.by_length(3)
            >>> for x in selector(staff):
            ...     x
            ...
            Selection(Note("f'16"), Note("g'8"), Note("a'4"))

    ..  container:: example

        **Example 5.** Selects the first item in each subselection:

        ::

            >>> selector = selector[0]
            >>> for x in selector(staff):
            ...     x
            ...
            ContiguousSelection(Note("f'16"),)

    ..  container:: example

        **Example 6.** Flattens all subselections and containers:

        ::

            >>> selector = selector.flatten()
            >>> for x in selector(staff):
            ...     x
            ...
            Note("f'16")

        ::

            >>> print(format(selector))
            selectortools.Selector(
                callbacks=(
                    selectortools.PrototypeSelectorCallback(
                        prototype=scoretools.Leaf,
                        ),
                    selectortools.RunSelectorCallback(
                        prototype=scoretools.Note,
                        ),
                    selectortools.LengthSelectorCallback(
                        length=3,
                        ),
                    selectortools.ItemSelectorCallback(
                        item=0,
                        apply_to_each=True,
                        ),
                    selectortools.FlattenSelectorCallback(
                        depth=-1,
                        ),
                    ),
                )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_callbacks',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        callbacks=None,
        ):
        if callbacks is not None:
            callbacks = tuple(callbacks)
        self._callbacks = callbacks

    ### SPECIAL METHODS ###

    def __call__(self, expr, seed=None):
        r'''Selects components from component or selection `expr`.

        Returns a selection of selections or containers.
        '''
        if seed is None:
            seed = 0
        seed = int(seed)
        prototype = (
            scoretools.Component,
            selectiontools.Selection,
            )
        if not isinstance(expr, prototype):
            expr = select(expr)
        expr = (expr,)
        assert all(isinstance(x, prototype) for x in expr), repr(expr)
        callbacks = self.callbacks or ()
        for i, callback in enumerate(callbacks, seed):
            try:
                expr = callback(expr, seed=i)
            except TypeError:
                expr = callback(expr)
        return selectiontools.Selection(expr)

    def __getitem__(self, item):
        r'''Gets `item` from selector.

        Returns another selector.
        '''
        from abjad.tools import selectortools
        if isinstance(item, slice):
            callback = selectortools.SliceSelectorCallback(
                start=item.start,
                stop=item.stop,
                apply_to_each=True,
                )
        elif isinstance(item, int):
            callback = selectortools.ItemSelectorCallback(
                item=item,
                apply_to_each=True,
                )
        else:
            raise ValueError(item)
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from ide import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='callbacks',
                display_string='callbacks',
                command='c',
                editor=idetools.getters.get_list,
                ),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def callbacks(self):
        r'''Gets selector callbacks.
        '''
        return self._callbacks

    ### PUBLIC METHODS ###

    def by_class(
        self,
        prototype=None,
        ):
        r'''Configures selector to select components of class `prototype`.

        ..  todo:: Maybe add a depth=None keyword.

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.PrototypeSelectorCallback(prototype)
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def by_duration(self, *args):
        r'''Configures selector to selector containers or selections of
        duration `duration`.

        ..  container:: example

            **Example 1.** Selects all runs of notes with duration equal to
            ``2/8``:

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.by_duration(Duration(2, 8))

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("d'8"), Note("e'8"))

        ..  container:: example

            **Example 2.** Selects all runs of notes with duration shorter than
            ``3/8``:

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.by_duration(
                ...     selectortools.DurationInequality(
                ...          duration=Duration(3, 8),
                ...          operator_string='<',
                ...          ),
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("c'8"),)
                Selection(Note("d'8"), Note("e'8"))

        ..  container:: example

            **Example 3.** Selects all runs of notes with duration longer than
            or equal to ``1/4``:

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.by_duration(
                ...     selectortools.DurationInequality(
                ...          duration=Duration(1, 4),
                ...          operator_string='>=',
                ...          ),
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("d'8"), Note("e'8"))
                Selection(Note("f'8"), Note("g'8"), Note("a'8"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        if len(args) == 1:
            duration = args[0]
            if not isinstance(duration, selectortools.DurationInequality):
                duration = durationtools.Duration(duration)
        elif len(args) == 2:
            duration = selectortools.DurationInequality(
                duration=args[1],
                operator_string=args[0],
                )
        else:
            raise ValueError(args)
        callback = selectortools.DurationSelectorCallback(
            duration=duration,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def by_leaves(self):
        r'''Configures selector to select leaves.

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.PrototypeSelectorCallback(scoretools.Leaf)
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def by_length(self, *args):
        r'''Configures selector to selector containers or selections of length
        `length`.

        ..  container:: example

            **Example 1.** Selects all runs of more than ``1`` note:

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.by_length(
                ...     selectortools.LengthInequality(
                ...          length=1,
                ...          operator_string='>',
                ...          ),
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("d'8"), Note("e'8"))
                Selection(Note("f'8"), Note("g'8"), Note("a'8"))

        ..  container:: example

            **Example 1.** Selects all runs ``3`` or fewer notes:
            ``3``:

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.by_length(
                ...     selectortools.LengthInequality(
                ...          length=3,
                ...          operator_string='<',
                ...          ),
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("c'8"),)
                Selection(Note("d'8"), Note("e'8"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        if len(args) == 1:
            length = args[0]
            if not isinstance(length, selectortools.LengthInequality):
                length = int(length)
        elif len(args) == 2:
            length = selectortools.LengthInequality(
                length=args[1],
                operator_string=args[0],
                )
        else:
            raise ValueError(args)
        callback = selectortools.LengthSelectorCallback(
            length=length,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def by_logical_measure(self):
        r'''Configures selector to group components by logical measure.

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.LogicalMeasureSelectorCallback()
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def by_logical_tie(
        self,
        flatten=True,
        only_with_head=False,
        only_with_tail=False,
        pitched=False,
        trivial=True,
        ):
        r'''Configures selector to select logical ties.

        ..  container:: example

            **Example 1.** Selects all logical ties:

            ::

                >>> staff = Staff("c'8 d' ~ { d' e' r f'~ } f' r")
                >>> container = staff[2]
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("c'8"),)
                LogicalTie(Note("d'8"), Note("d'8"))
                LogicalTie(Note("e'8"),)
                LogicalTie(Rest('r8'),)
                LogicalTie(Note("f'8"), Note("f'8"))
                LogicalTie(Rest('r8'),)

            ::

                >>> for x in selector(container):
                ...     x
                ...
                LogicalTie(Note("d'8"), Note("d'8"))
                LogicalTie(Note("e'8"),)
                LogicalTie(Rest('r8'),)
                LogicalTie(Note("f'8"), Note("f'8"))

        ..  container:: example

            **Example 2.** Selects pitched logical ties:

            ::

                >>> staff = Staff("c'8 d' ~ { d' e' r f'~ } f' r")
                >>> container = staff[2]
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(
                ...     pitched=True,
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("c'8"),)
                LogicalTie(Note("d'8"), Note("d'8"))
                LogicalTie(Note("e'8"),)
                LogicalTie(Note("f'8"), Note("f'8"))

            ::

                >>> for x in selector(container):
                ...     x
                ...
                LogicalTie(Note("d'8"), Note("d'8"))
                LogicalTie(Note("e'8"),)
                LogicalTie(Note("f'8"), Note("f'8"))

        ..  container:: example

            **Example 3.** Selects pitched nontrivial logical ties:

            ::

                >>> staff = Staff("c'8 d' ~ { d' e' r f'~ } f' r")
                >>> container = staff[2]
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(
                ...     pitched=True,
                ...     trivial=False,
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("d'8"), Note("d'8"))
                LogicalTie(Note("f'8"), Note("f'8"))

            ::

                >>> for x in selector(container):
                ...     x
                ...
                LogicalTie(Note("d'8"), Note("d'8"))
                LogicalTie(Note("f'8"), Note("f'8"))

        ..  container:: example

            **Example 4.** Selects pitched nontrivial logical ties whose head
            is contained in the expression to be selected from:

            ::

                >>> staff = Staff("c'8 d' ~ { d' e' r f'~ } f' r")
                >>> container = staff[2]
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(
                ...     only_with_head=True,
                ...     pitched=True,
                ...     trivial=False,
                ...     )

            ::

                >>> for x in selector(container):
                ...     x
                ...
                LogicalTie(Note("f'8"), Note("f'8"))

        ..  container:: example

            **Example 5.** Selects pitched nontrivial logical ties whose tail
            is contained in the expression to be selected from:

            ::

                >>> staff = Staff("c'8 d' ~ { d' e' r f'~ } f' r")
                >>> container = staff[2]
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(
                ...     only_with_tail=True,
                ...     pitched=True,
                ...     trivial=False,
                ...     )

            ::

                >>> for x in selector(container):
                ...     x
                ...
                LogicalTie(Note("d'8"), Note("d'8"))

        ..  container:: example

            **Example 5.** Selects logical ties whose head and tail is
            contained in the expression to be selected from:

            ::

                >>> staff = Staff("c'8 d' ~ { d' e' r f'~ } f' r")
                >>> container = staff[2]
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(
                ...     only_with_head=True,
                ...     only_with_tail=True,
                ...     )

            ::

                >>> for x in selector(container):
                ...     x
                ...
                LogicalTie(Note("e'8"),)
                LogicalTie(Rest('r8'),)

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.LogicalTieSelectorCallback(
            flatten=flatten,
            pitched=pitched,
            trivial=trivial,
            only_with_head=only_with_head,
            only_with_tail=only_with_tail,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def by_run(
        self,
        prototype=None,
        ):
        r'''Configures selector to select runs of `prototype`.

        ..  container:: example

            **Example 1.** Selects run of notes and chords at any depth:

            ::

                >>> staff = Staff(r"c'8 d' r \times 2/3 { e' r f' } g' a' r")
                >>> selector = selectortools.Selector()
                >>> prototype = (Note, Chord)
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(prototype)

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("c'8"), Note("d'8"))
                Selection(Note("e'8"),)
                Selection(Note("f'8"), Note("g'8"), Note("a'8"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.RunSelectorCallback(prototype)
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def first(self):
        r'''Configures selector to select first selection.

        ..  container:: example

            **Example 1.** Selects first pitched logical tie:

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.first()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("c'4"),)

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.ItemSelectorCallback(
            item=0,
            apply_to_each=False,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def flatten(self, depth=-1):
        r'''Configures selector to flatten its selections to `depth`.

        ..  container:: example

            **Example 1.** Selects all pitched logical ties (except the first
            and last) and then flattens the pitch logical ties:

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.middle()
                >>> selector = selector.flatten()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Note("d'4")
                Note("d'4")
                Note("e'4")
                Note("e'4")
                Note("e'4")

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.FlattenSelectorCallback(depth=depth)
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def get_item(self, item, apply_to_each=True):
        r'''Configures selector to select `item`.

        Maps the callback to each item in sequence when `apply_to_each` is
        true.

        Applies the callback to the entire sequence when `apply_to_each` is
        false.

        ..  container:: example

            **Example 1.** Selects the first note of each logical tie:

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.get_item(0, apply_to_each=True)

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                ContiguousSelection(Note("c'4"),)
                ContiguousSelection(Note("d'4"),)
                ContiguousSelection(Note("e'4"),)
                ContiguousSelection(Note("f'4"),)

        ..  container:: example

            **Example 2.** Selects logical tie at index ``1``:

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.get_item(1, apply_to_each=False)

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("d'4"), Note("d'4"))

        '''
        from abjad.tools import selectortools
        callback = selectortools.ItemSelectorCallback(
            item=item,
            apply_to_each=apply_to_each,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def get_slice(self, start=None, stop=None, apply_to_each=True):
        r'''Configures selector to select `start`:`stop`.

        Maps the callback to each item in sequence when `apply_to_each` is
        true.

        Applies the callback to the entire sequence when `apply_to_each` is
        false.

        ..  container:: example

            **Example 1.** Gets all notes (except the first) in each
            pitched logical tie:

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.get_slice(
                ...     start=1,
                ...     stop=None,
                ...     apply_to_each=True,
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("d'4"),)
                LogicalTie(Note("e'4"), Note("e'4"))

        ..  container:: example

            **Example 2.** Gets all pitched logical ties (except the last):

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.get_slice(
                ...     start=None,
                ...     stop=-1,
                ...     apply_to_each=False,
                ...     )

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("c'4"),)
                LogicalTie(Note("d'4"), Note("d'4"))
                LogicalTie(Note("e'4"), Note("e'4"), Note("e'4"))

        '''
        from abjad.tools import selectortools
        callback = selectortools.SliceSelectorCallback(
            start=start,
            stop=stop,
            apply_to_each=apply_to_each,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def last(self):
        r'''Configures selector to select the last selection.

        ..  container:: example

            **Example 1.** Selects the last pitched logical tie:

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.last()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("f'4"),)

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.ItemSelectorCallback(
            item=-1,
            apply_to_each=False,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def middle(self):
        r'''Configures selector to select all but the first or last selection.

        ..  container:: example

            **Example 1.** Selects all pitched logical ties (except the first
            and last):

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.middle()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("d'4"), Note("d'4"))
                LogicalTie(Note("e'4"), Note("e'4"), Note("e'4"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.SliceSelectorCallback(
            start=1,
            stop=-1,
            apply_to_each=False,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def most(self):
        r'''Configures selector to select all but the last selection.

        ..  container:: example

            **Example 1.** Selects all pitched logical ties (except the last):

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.most()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("c'4"),)
                LogicalTie(Note("d'4"), Note("d'4"))
                LogicalTie(Note("e'4"), Note("e'4"), Note("e'4"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.SliceSelectorCallback(
            stop=-1,
            apply_to_each=False,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def rest(self):
        r'''Configures selector to select all but the first selection.

        ..  container:: example

            **Example 1.** Selects all pitched logical ties (except the first):

            ::

                >>> staff = Staff(r"c'4 d'4 ~ d'4 e'4 ~ e'4 ~ e'4 r4 f'4")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_logical_tie(pitched=True)
                >>> selector = selector.rest()

            ::

                >>> for x in selector(staff):
                ...     x
                ...
                LogicalTie(Note("d'4"), Note("d'4"))
                LogicalTie(Note("e'4"), Note("e'4"), Note("e'4"))
                LogicalTie(Note("f'4"),)

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.SliceSelectorCallback(
            start=1,
            apply_to_each=False,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def with_callback(self, callback):
        r'''Configures selector with arbitrary `callback`.

        Returns new selector.
        '''
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def with_next_leaf(self):
        r'''Configures selector to select the next leaf after each selection.

        ..  container:: example

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.with_next_leaf()
                 
            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("c'8"), Rest('r8'))
                Selection(Note("d'8"), Note("e'8"), Rest('r8'))
                Selection(Note("f'8"), Note("g'8"), Note("a'8"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.ExtraLeafSelectorCallback(
            with_next_leaf=True,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)

    def with_previous_leaf(self):
        r'''Configures selector to select the previous leaf before each
        selection.

        ..  container:: example

            ::

                >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
                >>> selector = selectortools.Selector()
                >>> selector = selector.by_leaves()
                >>> selector = selector.by_run(Note)
                >>> selector = selector.with_previous_leaf()
                 
            ::

                >>> for x in selector(staff):
                ...     x
                ...
                Selection(Note("c'8"),)
                Selection(Rest('r8'), Note("d'8"), Note("e'8"))
                Selection(Rest('r8'), Note("f'8"), Note("g'8"), Note("a'8"))

        Returns new selector.
        '''
        from abjad.tools import selectortools
        callback = selectortools.ExtraLeafSelectorCallback(
            with_previous_leaf=True,
            )
        callbacks = self.callbacks or ()
        callbacks = callbacks + (callback,)
        return type(self)(callbacks)